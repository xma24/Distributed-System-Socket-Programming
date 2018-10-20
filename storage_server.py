import socket
import sys
import json
import os
from os.path import isfile, join


synchronized_folder = "./synchronized_folder_server/"
if not os.path.exists(synchronized_folder):
    os.mkdir(synchronized_folder)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
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
            connection.sendall("upload Ok")
            filename_list = file_name.split("/")
            file_folder = synchronized_folder
            filename_with_folder = file_folder + filename_list[-1]
            if not os.path.exists(file_folder):
                os.mkdir(file_folder)
                print("the folder is not exist...")

            print(filename_list[-1])

            file_list_sync = [f for f in os.listdir(synchronized_folder) if isfile(join(synchronized_folder, f))]
            if filename_list[-1] not in file_list_sync:
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
                                to_write_file.flush()
                            # file_data = json_data
                        else:
                            break
            elif filename_list[-1] in file_list_sync:
                os.remove(filename_with_folder)
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
                                to_write_file.flush()
                            # file_data = json_data
                        else:
                            break
        elif command_from_client[0] == "delete":
            print("The delete operation is captured")
            filename_list = command_from_client[1].split("/")
            file_name_to_delete = synchronized_folder + filename_list[-1]
            os.remove(file_name_to_delete)
        else:
            connection.sendall(json.dumps("Cannot recognize command"))
            break
    finally:
        connection.close()










