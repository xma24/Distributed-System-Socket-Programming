import socket
import sys
import json # do not use the json package because you may not use the struct data
import os
from thread import *
import threading
from os.path import isfile, join
import time
from datetime import datetime

previous_file_dictionary = {}


def update_file(updated_file_name):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    command = "upload " + updated_file_name
    sock.sendall(command)
    recv_ack = sock.recv(1024)

    if recv_ack == "upload Ok":
        print("received the upload ack from the server")
        with open(updated_file_name, 'rb') as to_read_file:
            file_data = to_read_file.read()
            # json_file_data = json.dumps(file_data)
        sock.sendall(file_data)
        sock.close()


def delete_file(deleted_file_name):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    command = "delete " + deleted_file_name
    sock.sendall(command)
    recv_ack = sock.recv(1024)
    print(recv_ack)
    sock.close()

'''
def rename_file(pre_filename, current_filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    command = "rename " + pre_filename + " " + current_filename
    sock.sendall(command)
    recv_ack = sock.recv(1024)
    print(recv_ack)
    sock.close()
'''




def helper_thread():
    global synchronized_folder
    global previous_file_dictionary
    # threading.Timer(5.0, helper_thread).start()
    while True:
        # print("The helper thread is running ...")
        time.sleep(5)
        current_file_dictionary = file_dictionary_creat(synchronized_folder)
        if len(current_file_dictionary) == len(previous_file_dictionary):
            for key, value in current_file_dictionary.items():
                if key not in previous_file_dictionary.keys():
                    for key_n, value_n in previous_file_dictionary.items():
                        if key_n not in current_file_dictionary.keys():
                            previous_filename = synchronized_folder + key_n
                            current_filename = synchronized_folder + key
                            # rename_file(previous_filename, current_filename)
                            update_file(current_filename)
                            # delete_file(previous_filename)
                            previous_file_dictionary.pop(key_n)
                            previous_file_dictionary[key] = current_file_dictionary[key]
                            delete_file(previous_filename)
                if (current_file_dictionary[key] - previous_file_dictionary[key]).seconds > 0.5:
                    updated_file_path = synchronized_folder + key
                    # delete_file(updated_file_path)
                    update_file(updated_file_path)
                    previous_file_dictionary[key] = current_file_dictionary[key]
        elif len(current_file_dictionary) > len(previous_file_dictionary):
            for key, value in current_file_dictionary.items():
                if key not in previous_file_dictionary.keys():
                    created_file_name = synchronized_folder + key
                    update_file(created_file_name)
                    previous_file_dictionary[key] = current_file_dictionary[key]
        elif len(current_file_dictionary) < len(previous_file_dictionary):
            for key, value in previous_file_dictionary.items():
                if key not in current_file_dictionary.keys():
                    deleted_file_name = synchronized_folder + key
                    delete_file(deleted_file_name)
                    previous_file_dictionary.pop(key)


def file_dictionary_creat(path_to_folder):
    file_dictionary = {}
    file_list_sync = [f for f in os.listdir(path_to_folder) if isfile(join(path_to_folder, f))]
    for file_index in file_list_sync:
        path_to_file = path_to_folder + file_index
        stat = os.stat(path_to_file)
        file_dictionary[file_index] = datetime.strptime(time.ctime(os.path.getmtime(path_to_file)), "%a %b %d %H:%M:%S %Y")
    # for key, value in file_dictionary.items():
    #    print(key, ":", value)
    return file_dictionary


synchronized_folder = "./synchronized_folder_client/"
if not os.path.exists(synchronized_folder):
    os.mkdir(synchronized_folder)
# commands = raw_input()
# global file_list

previous_file_dictionary = file_dictionary_creat(synchronized_folder)
for key, value in previous_file_dictionary.items():
    print(key, ":", value)
    # init_file_path =

print("Start the helper thread ...")
# start_new_thread(helper_thread, ())
helper_thread = threading.Thread(target=helper_thread)
helper_thread.start()
helper_thread.join()


