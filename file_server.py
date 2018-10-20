import socket
import sys
import json
import os, os.path

server_folder = './server/'
if not os.path.exists(server_folder):
    os.system("mkdir " + server_folder)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)


while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print(sys.stderr, 'connection from', client_address)
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
            connection.sendall("upload Ok")
            filename_list = file_name.split("/")
            file_folder = command_from_client[2]
            print(file_folder)
            foldername_list = file_folder.split("/")
            print(foldername_list)
            # file_folder = "./uploaded_file/"
            filename_with_folder = file_folder + filename_list[-1]
            print(filename_with_folder)
            if not os.path.exists(file_folder):
                os.system("mkdir " + file_folder)
                print("the folder is not exist...")

            print(filename_list[-1])
            with open(filename_with_folder, 'wb+') as to_write_file:
                while True:
                    recv_data_file = connection.recv(32)
                    # print("New message is received")
                    if recv_data_file:
                        # init_json_file = json.dumps("")
                        # init_json_file.update(json.loads(json_data))
                            # file_data = json.loads(init_json_file)
                            to_write_file.write(recv_data_file)
                            # file_data.update()
                        # file_data = json_data
                    else:
                        break
        elif command_from_client[0] == "rename":
            print("The rename operation is captured")
            ack_message = json.dumps("rename Ok")
            print(command_from_client[1])
            print(command_from_client[2])
            os.rename(command_from_client[1], command_from_client[2])
        elif command_from_client[0] == "delete":
            print("The delete operation is captured")
            os.remove(command_from_client[1])
        elif command_from_client[0] == "download":
            print("Capture the download operation")
            connection.sendall("download Ok")
            with open(command_from_client[1], 'rb') as to_read_file:
                download_file_data = to_read_file.read()
                connection.sendall(download_file_data)
        else:
            connection.sendall(json.dumps("Cannot recognize command"))
            break
    finally:
        connection.close()











