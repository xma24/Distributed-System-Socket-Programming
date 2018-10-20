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

time.sleep(10)

# run the multiple thread file transfer program on the server side
process_file_server_multiple_thread = Popen(['python', 'multithread_file_server_final.py'], stdin=PIPE, stdout=PIPE,
                                            stderr=PIPE)
# run the multiple thread file transfer program on the server side
# process_file_client_multiple_thread = Popen(['python', 'multithread_file_server_final.py'], stdin=PIPE, stdout=PIPE,stderr=PIPE)

# create files
number_files = 3

# files_in_test = len([name for name in os.listdir(file_folder) if os.path.isfile(name)])
if not os.path.exists(file_folder):
    os.system("mkdir " + file_folder)
    for i in range(number_files):
        file_name = file_folder + "file" + str(i) + '.txt'
        os.system("touch " + file_name)
        digits = "".join([random.choice(string.digits) for i in xrange(10000)]) * 1000
        chars = "".join([random.choice(string.letters) for i in xrange(150000)]) * 1000
        text_content = digits + chars
        with open(file_name, 'wb') as f_random:
            f_random.write(text_content)
            f_random.flush()
    print("Files used to test the program have been created ...")
    # os.system("ls -LR " + file_folder)
else:
    print("Files have already been created ...")
    # os.system("ls -LR " + file_folder)


def start_thread(p_file_client_local, command):
    stdout, stderr = p_file_client_local.communicate(input=command)
    print(stdout)
    print("")
    # p_file_client_local.stdout.close()


print("------------------------ Multithread upload file (LOCK) ------------------------")
print(">> List files in each folder: ")
for folder_index in range(1, len(folder_list)):
    if os.path.exists(folder_list[folder_index]):
        os.system("ls -LR " + folder_list[folder_index])
        print("")
print("")

input_file_client_upload = "upload " + file_folder + "file" + str(1) + '.txt' + " " + "./server/uploaded_files/"
print(">> Command on Client: ")
print(input_file_client_upload)
print("")


p_file_client_before = Popen(['python', 'multithread_file_client_final.py'], stdin=PIPE, stdout=PIPE,
                             stderr=PIPE)
stdout_client_before, stderr_client_before = p_file_client_before.communicate(
    input=input_file_client_upload)

p_file_client_after = Popen(['python', 'multithread_file_client_final.py'], stdin=PIPE, stdout=PIPE,
                            stderr=PIPE)
stdout_client_after, stderr_client_after = p_file_client_after.communicate(
    input=input_file_client_upload)
print(stdout_client_after)

# start_new_thread(start_thread, (p_file_client_before, input_file_client_upload,))
# start_new_thread(start_thread, (p_file_client_after, input_file_client_upload,))

# p_file_client_before.stdout.close()
# p_file_client_after.stdout.close()
time.sleep(10)

print(">> List files in each folder: ")
for folder_index in range(1, len(folder_list)):
    os.system("ls -LR " + folder_list[folder_index])
    print("")





print("------------------------ Multithread download file (UNLOCK) ------------------------")
print(">> List files in each folder: ")
for folder_index in range(1, len(folder_list)):
    if os.path.exists(folder_list[folder_index]):
        os.system("ls -LR " + folder_list[folder_index])
        print("")
print("")

input_file_client_download_1 = "download ./test_files/file2.txt ./client/downloaded_files_1/"
input_file_client_download_2 = "download ./test_files/file2.txt ./client/downloaded_files_2/"
print(">> Command on Client: ")
print(input_file_client_download_1)
print("")
print(input_file_client_download_2)
print("")

p_file_client_before_d = Popen(['python', 'multithread_file_client_final.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout_client_before_d, stderr_client_before_d = p_file_client_before_d.communicate(input=input_file_client_download_1)
print(stdout_client_before_d)

p_file_client_after_d = Popen(['python', 'multithread_file_client_final.py'], stdin=PIPE, stdout=PIPE,
                              stderr=PIPE)
stdout_client_after_d, stderr_client_after_d = p_file_client_after_d.communicate(
    input=input_file_client_download_2)
print(stdout_client_after_d)

# p_file_client_after_d = Popen(['python', 'multithread_file_client_final.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)

# start_new_thread(start_thread, (p_file_client_before_d, input_file_client_download_1,))
# start_new_thread(start_thread, (p_file_client_after_d, input_file_client_download_2,))

# p_file_client_before.stdout.close()
# p_file_client_after.stdout.close()

print(">> List files in each folder: ")
for folder_index in range(1, len(folder_list)):
    os.system("ls -LR " + folder_list[folder_index])
    print("")












