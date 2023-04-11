import socket
import string

# Alfabeto para decodificar/codificar:
'''
 ['{', 'C', 'g', 'r', '/', 'U', 'a', 'W', 'z', 'L', ',', '$', 'n', 'V', 'A', 'k', 'X', 
 '`', 'w', ')', '(', 'J', '<', 'E', 'B', '_', '#', 'u', 'P', 'p', 'I', '[', 'M', ']', 
 'Q', '"', 'l', '|', 'T', '}', '!', 'j', 'm', '=', 'F', '\\', '+', 'o', '.', 'y', '-', 
 'G', 'q', '?', '>', ';', 'O', 'f', '*', ' ', 'S', 'R', ':', 't', '^', "'", 'b', 's', 
 'c', 'Z', 'd', 'x', '~', '@', 'K', 'h', 'N', 'D', 'e', '%', 'v', '&', 'H', 'i', 'Y']
'''
alphabet = "".join([" ",string.ascii_letters,string.punctuation])
alphabet2=['{', 'C', 'g', 'r', '/', 'U', 'a', 'W', 'z', 'L', ',', '$', 'n', 'V', 'A', 'k', 'X', '`', 'w', ')', '(', 'J', '<', 'E', 'B', '_', '#', 'u', 'P', 'p', 'I', '[', 'M', ']', 'Q', '"', 'l', '|', 'T', '}', '!', 'j', 'm', '=', 'F', '\\', '+', 'o', '.', 'y', '-', 'G', 'q', '?', '>', ';', 'O', 'f', '*', ' ', 'S', 'R', ':', 't', '^', "'", 'b', 's', 'c', 'Z', 'd', 'x', '~', '@', 'K', 'h', 'N', 'D', 'e', '%', 'v', '&', 'H', 'i', 'Y']
encode_alphabet="".join(alphabet2)

def decrypt(text, alphabet, encode_alphabet):
    original_text=""

    for letter in text:
        index= encode_alphabet.index(letter)
        original_text+= alphabet[index]
    
    return original_text

def encrypt(text, alphabet, encode_alphabet):
    encrypt_text=""

    for letter in text:
        index= alphabet.index(letter)
        encrypt_text+= encode_alphabet[index]
    
    return encrypt_text

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = decrypt(conn.recv(1024).decode(),alphabet,encode_alphabet)
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(encrypt(data,alphabet,encode_alphabet).encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()