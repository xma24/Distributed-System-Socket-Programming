import socket
import sys
import json
import os
from thread import *
import threading
import time

server_folder = './server/'
if not os.path.exists(server_folder):
    os.system("mkdir " + server_folder)

print_lock = threading.Lock()
thread_counter = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)


def upload_threaded(upload_connection, filename, filefolder):
    global thread_counter
    thread_counter += 1

    '''
    # data received from client
    data = upload_connection.recv(1024)
    if not data:
        print('The upload thread is finished')

        # lock released on exit
        print_lock.release()
        break
    '''
    file_name = filename
    # reverse the given string from client
    filename_list = file_name.split("/")
    # file_folder = "./uploaded_file_with_lock/"
    file_folder = filefolder

    filename_with_folder = file_folder + filename_list[-1]
    if not os.path.exists(file_folder):
        os.mkdir(file_folder)
        print("the folder is not exist...")

    print(filename_list[-1])
    with open(filename_with_folder, 'wb+') as to_write_file:
        while True:
            recv_data_file = upload_connection.recv(32)
            # time.sleep(2)
            # print("New message is received")
            if recv_data_file:
                # init_json_file = json.dumps("")
                # init_json_file.update(json.loads(json_data))
                # file_data = json.loads(init_json_file)
                to_write_file.write(recv_data_file)
                # file_data.update()
                # file_data = json_data
                to_write_file.flush()
            else:
                print_lock.release()
                print("Released...")
                break

    upload_connection.close()
    thread_counter -= 1


def download_threaded(download_connection, download_file_name):
    with open(download_file_name, 'rb') as to_read_file:
        download_file_data = to_read_file.read()
        download_connection.send(download_file_data)
        download_connection.close()



def rename_threaded(rename_connection, source, destination):
    global thread_counter
    thread_counter += 1
    os.rename(source, destination)
    print_lock.release()
    print("Released...")
    rename_connection.close()
    thread_counter -= 1


def delete_threaded(delete_connection, delete_file_name):
    global thread_counter
    thread_counter += 1
    os.remove(delete_file_name)
    print_lock.release()
    print("Released...")
    delete_connection.close()
    thread_counter -= 1


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)
    # Receive the data in small chunks and retransmit it

    recv_data = connection.recv(1024)
    # data = json.loads(json_data)
    # print(sys.stderr, 'received "%s"' % json_data)
    # received_data = json.loads(recv_data)
    # print(recv_data)
    command_from_client = recv_data.split(" ")
    # command_from_client = recv_data
    print(command_from_client[0])
    # print(command_from_client[1])
    if command_from_client[0] == "upload":
        print("The upload operation is captured")
        file_name = command_from_client[1]
        file_folder = command_from_client[2]
        if thread_counter >= 1:
            connection.send("The upload process is locked")
        else:
            connection.sendall("upload Ok")
            print_lock.acquire()
            print("Locking...")
            start_new_thread(upload_threaded, (connection, file_name, file_folder))
    elif command_from_client[0] == "rename":
        print("The rename operation is captured")
        ack_message = json.dumps("rename Ok")
        print_lock.acquire()
        print("Locking...")
        start_new_thread(rename_threaded, (connection, command_from_client[1], command_from_client[2]))
        # print(command_from_client[1])
        # print(command_from_client[2])
        # os.rename(command_from_client[1], command_from_client[2])
    elif command_from_client[0] == "delete":
        print("The delete operation is captured")
        ack_message = json.dumps("delete Ok")
        print_lock.acquire()
        print("Locking...")
        start_new_thread(delete_threaded, (connection, command_from_client[1]))
        # os.remove(command_from_client[1])
    elif command_from_client[0] == "download":
        print("Capture the download operation")
        connection.sendall("download Ok")
        start_new_thread(download_threaded, (connection, command_from_client[1]))
    else:
        connection.sendall(json.dumps("Cannot recognize command"))
        break











