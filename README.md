# distributed_system
## This is realated to the socket programming.

### There are 4 assignments in this project.
    - Assignment 1 --> create a simple file upload program.
    - Assignment 2 --> use muliti-thread to create the file upload program.
    - Assignment 3 --> create a Remote Procedure Communication (RPC) program.
    - Assignment 4 --> create a dropbox-like file synchronization program.
    
#### 1. For each assignment, we also write the test codes to test our model. You can choose to directly run those test codes. The following is the relationship between our codes and test codes:
##### Assignment 1 
    - code: file_client.py; file_server.py
    - test: Test_file_client_server.py

##### Assignment 2
    - code: multithread_file_client_final.py; multithread_file_server_final.py
    - test: Test_multithread_file_client_server.py

##### Assignment 3 
    - code: rpc_client_final.py; rpc_server_final.py
    - test: rpc_client_final.py

##### Assignment 4 
    - code: storage_client.py; storage_server.py
    - test: Test_storage_client_server.py

### 2. You can also choose to run those codes instead of our test codes independently.
##### Assignment 1
- Client side: python file_client.py
- Server side: python file_server.py

Note: In the client side, you need to input the operations (i.e, upload, download, rename, delete). Examples:
- upload ./test_files/file1.txt ./server/uploaded_files/
- download ./test_file/file1.txt ./client/downloaded_files/
- rename ./server/uploaded_files/file2.txt ./server/uploaded_files/file_renamed.txt
- delete ./server/uploaded_files/file_renamed.txt

##### Assignment 2
- Client side: python multithread_file_client_final.py
- Server side: python multithread_file_server_final.py
    
Note: In the client side, you need to input the operations (i.e, upload, download, rename, delete). The operatins are the same with Assignment 1, however, you need to open several terminals to run the client program at the same time. Examples:
- upload ./test_files/file1.txt ./server/uploaded_files/
- download ./test_file/file1.txt ./client/downloaded_files/
- rename ./server/uploaded_files/file2.txt ./server/uploaded_files/file_renamed.txt
- delete ./server/uploaded_files/file_renamed.txt

##### Assignment 3
- Client side: python rpc_client_final.py
- Server side: python rpc_server_final.py

Note: The test cases are written in the rpc_client_final.py. You can add more cases. For more details, please refer the file "rpc_client_final.py". Examples:
- s = add(1.5, 2.6)
- pi = calculate_pi()
- sorted_list = sort(unsorted_list)
- product = matrix_multiply(matrix_A, matrix_B, matrix_C)

##### Assignment 4
- Client side: python storage_client.py
- Server side: python storage_server.py
    
Note: You can do those operations on the client. The synchornized folder on client is "./synchronized_folder_client/", while the synchornized folder on server is "./synchronized_folder_server/". Examples:
- You can directly drag files or modify files in the "./synchronized_folder_client/"" folder directly. You will see the corresponding change in the "./synchronized_folder_server/" folder.


