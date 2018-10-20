# Create the server module of RPC
import socket
import json
import numpy as np

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)


def add(number_a, number_b):
    return number_a + number_b


def calculate_pi():
    return np.pi


def sort(unsorted_list):
    return np.sort(unsorted_list).tolist()


def matrix_multiply(matrix_A, matrix_B, matrix_C):
    matrix_A_array = np.array([l for l in matrix_A])
    matrix_A_real = np.asmatrix(matrix_A_array)

    matrix_B_array = np.array([l for l in matrix_B])
    matrix_B_real = np.asmatrix(matrix_B_array)

    matrix_C_array = np.array([l for l in matrix_C])
    matrix_C_real = np.asmatrix(matrix_C_array)

    result = np.matmul(np.matmul(matrix_A_real, matrix_B_real), matrix_C_real)
    return result.tolist()


while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        # print('connection from', client_address)
        # Receive the data in small chunks and retransmit it

        result_dictionary = {}

        recv_data = connection.recv(1024)
        # print(recv_data)

        command_dictionary = json.loads(recv_data)
        if command_dictionary["function"] == "add":
            num_a = command_dictionary["arg_list"][0]
            num_b = command_dictionary["arg_list"][1]
            print("The received function name from client: %s" % command_dictionary["function"])
            print("The received parameters from client:", command_dictionary["arg_list"])
            ret = add(num_a, num_b)
            result_dictionary["result"] = ret
        elif command_dictionary["function"] == "calculate_pi":
            print("The received function name from client: %s" % command_dictionary["function"])
            print("The received parameters from client:", command_dictionary["arg_list"])
            ret = calculate_pi()
            result_dictionary["result"] = ret
        elif command_dictionary["function"] == "sort":
            print("The received function name from client: %s" % command_dictionary["function"])
            print("The received parameters from client:", command_dictionary["arg_list"])
            ret = sort(command_dictionary["arg_list"])
            result_dictionary["result"] = ret
        elif command_dictionary["function"] == "matrix_multiply":
            print("The received function name from client: %s" % command_dictionary["function"])
            print("The received parameters from client:", command_dictionary["arg_list"])
            matrix_A_list = command_dictionary["arg_list"][0]
            matrix_B_list = command_dictionary["arg_list"][1]
            matrix_C_list = command_dictionary["arg_list"][2]
            print("matrix_A:", matrix_A_list)
            print("matrix_B:", matrix_B_list)
            print("matrix_C:", matrix_C_list)

            ret = matrix_multiply(matrix_A_list, matrix_B_list, matrix_C_list)
            result_dictionary["result"] = ret
        else:
            connection.sendall(json.dumps("Cannot recognize command"))
            break
        ret_json = json.dumps(result_dictionary)
        connection.sendall(ret_json.encode('utf-8'))
        connection.close()
        print("")
    finally:
        connection.close()












