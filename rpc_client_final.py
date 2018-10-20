
# Create a RPC client module
import socket
import json
import inspect
import numpy as np
import random as rd


def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 10000)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    return sock


def add(num_a, num_b):
    add_sock = create_socket()
    arg_list = []
    arg_list.append(num_a)
    arg_list.append(num_b)
    # print(arg_list)
    # print(type(inspect.stack()[0][3]))
    payload = {
        "function": inspect.stack()[0][3],
        "arg_list": arg_list,
    }
    # print("The function running on server: %s(%.3f,%.3f)" % (payload["function"], arg_list[0], arg_list[1]))
    payload_json = json.dumps(payload)
    add_sock.sendall(payload_json.encode('utf-8'))
    result_json = add_sock.recv(1024)
    result = json.loads(result_json)
    ret = result["result"]
    add_sock.close()
    return ret


def calculate_pi():
    calculate_pi_sock = create_socket()
    arg_list = []
    # print(arg_list)
    payload = {
        "function": inspect.stack()[0][3],
        "arg_list": arg_list,
    }
    payload_json = json.dumps(payload)
    calculate_pi_sock.sendall(payload_json.encode('utf-8'))
    result_json = calculate_pi_sock.recv(1024)
    result = json.loads(result_json)
    ret = result["result"]
    calculate_pi_sock.close()
    return ret


def sort(unsorted_list):
    sort_sock = create_socket()
    arg_list = []
    arg_list += unsorted_list
    # print(arg_list)

    payload = {
        "function": inspect.stack()[0][3],
        "arg_list": arg_list,
    }
    payload_json = json.dumps(payload)
    sort_sock.sendall(payload_json.encode('utf-8'))
    result_json = sort_sock.recv(1024)
    result = json.loads(result_json)
    ret = result["result"]
    sort_sock.close()
    return ret


def matrix_multiply(matrix_A, matrix_B, matrix_C):
    matrix_multiply_sock = create_socket()
    arg_list = []
    arg_list.append(matrix_A.tolist())
    arg_list.append(matrix_B.tolist())
    arg_list.append(matrix_C.tolist())

    payload = {
        "function": inspect.stack()[0][3],
        "arg_list": arg_list,
    }
    payload_json = json.dumps(payload)
    matrix_multiply_sock.sendall(payload_json.encode('utf-8'))
    result_json = matrix_multiply_sock.recv(1024)
    result = json.loads(result_json)
    ret = result["result"]
    ret_array = np.array([l for l in ret])
    ret_matrix = np.asmatrix(ret_array)
    matrix_multiply_sock.close()
    return ret_matrix


# The following codes are to test the function of RPC between client and server
# add function on client
s = add(1.5, 2.6)
print("The result obtained from server: %f \n" % s)

# calculate pi function on client
pi = calculate_pi()
print("The result obtained from server: %f \n" % pi)

# sort function on client
number_pool = np.arange(100)
unsorted_list = rd.sample(number_pool, 20)
print("unsorted_list:", unsorted_list)

sorted_list = sort(unsorted_list)
print("  sorted_list:", sorted_list)
print("")

# matrix_multipy function on client
matrix_A = np.matrix(np.arange(4).reshape((2, 2)))
matrix_B = np.matrix(np.arange(4).reshape((2, 2)))
matrix_C = np.matrix(np.arange(4).reshape((2, 2)))

product = matrix_multiply(matrix_A, matrix_B, matrix_C)
print(product)
