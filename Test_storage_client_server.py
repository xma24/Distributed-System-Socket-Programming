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



# run the multiple thread file transfer program on the server side
print("------------------------ Bonus Dropbox-like synchronized storage ------------------------")

sync_filelist = ["./synchronized_folder_client/", "./synchronized_folder_server/"]


for i in range(len(sync_filelist)):
    if os.path.exists(sync_filelist[i]):
        os.system("rm -R " + sync_filelist[i])

time.sleep(10)


process_dropbox_server = Popen(['python', 'storage_server.py'], stdin=PIPE, stdout=PIPE,
                                            stderr=PIPE)
process_dropbox_client = Popen(['python', 'storage_client.py'], stdin=PIPE, stdout=PIPE,
                                            stderr=PIPE)

for op_index in range(4):
    if op_index == 0:
        print(">> List files in each folder: ")
        for folder_index in range(len(sync_filelist)):
            if os.path.exists(sync_filelist[folder_index]):
                os.system("ls -la -LR " + sync_filelist[folder_index])
                print("")
        print("")

        print("------ Add two new file at the client ------ ")
        os.system("touch ./synchronized_folder_client/added_file1.txt")
        os.system("touch ./synchronized_folder_client/added_file2.txt")

        time.sleep(10)

        print(">> List files in each folder: ")
        for folder_index in range(len(sync_filelist)):
            if os.path.exists(sync_filelist[folder_index]):
                os.system("ls -la -LR " + sync_filelist[folder_index])
                print("")
        print("")

        print("------ Modify a file at the client ------ ")
        with open("./synchronized_folder_client/added_file1.txt", 'wb+') as f_modify:
            add_str = ""
            for i in range(1000):
                add_str += str(i)
            f_modify.write(add_str)

        time.sleep(10)

        print(">> List files in each folder: ")
        for folder_index in range(len(sync_filelist)):
            if os.path.exists(sync_filelist[folder_index]):
                os.system("ls -la -LR " + sync_filelist[folder_index])
                print("")
        print("")

        print("------ Rename a file at the client ------ ")
        os.system("mv ./synchronized_folder_client/added_file1.txt ./synchronized_folder_client/added_file_modified.txt")

        time.sleep(10)

        print(">> List files in each folder: ")
        for folder_index in range(len(sync_filelist)):
            if os.path.exists(sync_filelist[folder_index]):
                os.system("ls -la -LR " + sync_filelist[folder_index])
                print("")
        print("")

        print("------ Delete a file at the client ------ ")
        os.system("rm ./synchronized_folder_client/added_file_modified.txt")

        time.sleep(10)

        print(">> List files in each folder: ")
        for folder_index in range(len(sync_filelist)):
            if os.path.exists(sync_filelist[folder_index]):
                os.system("ls -la -LR " + sync_filelist[folder_index])
                print("")
        print("")



