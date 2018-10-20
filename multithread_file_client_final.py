import socket
import sys
import json # do not use the json package because you may not use the struct data
import os

client_folder = './client/'
if not os.path.exists(client_folder):
    os.system("mkdir " + client_folder)

while True:
    print("Input your operation:")
    commands = raw_input()

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10001)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:
        # Send data
        cmd_message = str(commands)
        command_list = cmd_message.split(" ")
        # print(sys.stderr, 'sending "%s"' % message)
        # json_message = json.dumps(message)
        # print(type(json_message))
        sock.sendall(cmd_message)

        recv_ack = sock.recv(1024)

        if recv_ack == "upload Ok":
            print("received the upload ack from the server")
            with open(command_list[1], 'rb') as to_read_file:
                file_data = to_read_file.read()
                # json_file_data = json.dumps(file_data)
            sock.sendall(file_data)
            sock.close()
        elif recv_ack == "The upload process is locked":
            print("The upload process is locked, try again later.")
            sock.close()
        elif recv_ack == "download Ok":
            print("received the download ack from the server")
            filename_list = command_list[1].split("/")
            #file_folder = "./downloaded_file/"
            file_folder = command_list[2]
            filename_with_folder = file_folder + filename_list[-1]
            if not os.path.exists(file_folder):
                os.mkdir(file_folder)

            with open(filename_with_folder, 'wb+') as to_write_file:
                while True:
                    recv_ack = sock.recv(32)
                    to_write_file.write(recv_ack)
                    to_write_file.flush()
                    if recv_ack == "":
                        sock.close()
                        break
            # print("finished downloading files ...")
            # sock.close()
    finally:
        print('closing socket')
        sock.close()
