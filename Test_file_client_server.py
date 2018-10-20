from subprocess import Popen, PIPE, STDOUT
import subprocess
import os, os.path
import random
import string
import pickle as plk
import signal
from multiprocessing import Process, Queue
from thread import *
import threading
import time

file_folder = './test_files/'
server_folder = './server/'
client_folder = './client/'
folder_list = [file_folder, server_folder, client_folder]


for i in range(len(folder_list)):
    if os.path.exists(folder_list[i]):
        os.system("rm -R " + folder_list[i])



# create files
number_files = 5

# files_in_test = len([name for name in os.listdir(file_folder) if os.path.isfile(name)])
if not os.path.exists(file_folder):
    os.system("mkdir " + file_folder)
    for i in range(number_files):
        file_name = file_folder + "file" + str(i) + '.txt'
        os.system("touch " + file_name)
        digits = "".join([random.choice(string.digits) for i in xrange(10000)]) * 2000
        chars = "".join([random.choice(string.letters) for i in xrange(150000)]) * 2000
        text_content = digits + chars
        with open(file_name, 'wb') as f_random:
            f_random.write(text_content)
            f_random.flush()
    print("Files used to test the program have been created ...")
    # os.system("ls -LR " + file_folder)
else:
    print("Files have already been created ...")
    # os.system("ls -LR " + file_folder)


# run the signle thread file transfer program on the server side
process_file_server = Popen(['python', 'file_server.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

for operation_index in range(4):
    if operation_index == 0:
        print("------------------------ upload file ------------------------")
        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            if os.path.exists(folder_list[folder_index]):
                os.system("ls -LR " + folder_list[folder_index])
                print("")
        print("")

        input_file_client_upload = "upload " + file_folder + "file" + str(2) + '.txt' + " " + "./server/uploaded_files/"
        print(">> Command on Client: ")
        print(input_file_client_upload)
        print("")

        p_file_client = Popen(['python', 'file_client.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout_file_client_upload, stderr_file_client_upload = p_file_client.communicate(input=input_file_client_upload)
        print(stdout_file_client_upload)
        print("")

        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            os.system("ls -LR " + folder_list[folder_index])
            print("")
        p_file_client.stdout.close()
        # p_file_client.kill()
    elif operation_index == 1:
        print("------------------------ download file ------------------------")
        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            if os.path.exists(folder_list[folder_index]):
                os.system("ls -LR " + folder_list[folder_index])
                print("")
        print("")

        input_file_client_upload = "download ./test_files/file1.txt ./client/downloaded_files/"
        print(">> Command on Client: ")
        print(input_file_client_upload)
        print("")

        p_file_client = Popen(['python', 'file_client.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout_file_client_upload, stderr_file_client_upload = p_file_client.communicate(input=input_file_client_upload)
        print(stdout_file_client_upload)
        print("")

        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            os.system("ls -LR " + folder_list[folder_index])
            print("")
        p_file_client.stdout.close()
    elif operation_index == 2:
        print("------------------------ rename file ------------------------")
        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            if os.path.exists(folder_list[folder_index]):
                os.system("ls -LR " + folder_list[folder_index])
                print("")
        print("")

        input_file_client_upload = "rename ./server/uploaded_files/file2.txt ./server/uploaded_files/file_renamed.txt"
        print(">> Command on Client: ")
        print(input_file_client_upload)
        print("")

        p_file_client = Popen(['python', 'file_client.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout_file_client_upload, stderr_file_client_upload = p_file_client.communicate(input=input_file_client_upload)
        print(stdout_file_client_upload)
        print("")

        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            os.system("ls -LR " + folder_list[folder_index])
            print("")
        p_file_client.stdout.close()
    else:
        print("------------------------ delete file ------------------------")
        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            if os.path.exists(folder_list[folder_index]):
                os.system("ls -LR " + folder_list[folder_index])
                print("")
        print("")

        input_file_client_upload = "delete ./server/uploaded_files/file_renamed.txt"
        print(">> Command on Client: ")
        print(input_file_client_upload)
        print("")

        p_file_client = Popen(['python', 'file_client.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout_file_client_upload, stderr_file_client_upload = p_file_client.communicate(input=input_file_client_upload)
        print(stdout_file_client_upload)
        print("")

        print(">> List files in each folder: ")
        for folder_index in range(1, len(folder_list)):
            os.system("ls -LR " + folder_list[folder_index])
            print("")
        p_file_client.stdout.close()

# os.killpg(os.getpgid(process_file_server.pid), signal.SIGTERM)
