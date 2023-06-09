import socket
import string
import time

# Alfabeto para decodificar/codificar:
'''
 ['{', 'C', 'g', 'r', '/', 'U', 'a', 'W', 'z', 'L', ',', '$', 'n', 'V', 'A', 'k', 'X', 
 '`', 'w', ')', 'ñ', '(', 'J', '<', 'E', 'B', '_', '#', 'u', 'P', 'p', 'I', '[', 'M', ']', 
 'Q', '"', 'l', '|', 'T', '}', '!', 'j', 'm', '=', 'F', '\\', '+', 'o', '.', 'y', '-', 
 'G', 'q', '?', '>', ';', 'O', 'f', '*', ' ', 'S', 'R', ':', 't', '^', "'", 'b', 's', 
 'c', 'Z', 'd', 'x', '~', '@', 'K', 'h', 'N', 'D', 'e', '%', 'v', '&', 'H', 'i', 'Y']
'''
alphabet = "".join([" ",string.ascii_letters,string.punctuation,"ñ"])
alphabet2=['{', 'C', 'g', 'r', '/', 'U', 'a', 'W', 'z', 'L', ',', '$', 'n', 'V', 'A', 'k', 'X', '`', 'w', ')', 'ñ', '(', 'J', '<', 'E', 'B', '_', '#', 'u', 'P', 'p', 'I', '[', 'M', ']', 'Q', '"', 'l', '|', 'T', '}', '!', 'j', 'm', '=', 'F', '\\', '+', 'o', '.', 'y', '-', 'G', 'q', '?', '>', ';', 'O', 'f', '*', ' ', 'S', 'R', ':', 't', '^', "'", 'b', 's', 'c', 'Z', 'd', 'x', '~', '@', 'K', 'h', 'N', 'D', 'e', '%', 'v', '&', 'H', 'i', 'Y']
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

def client_program():
    file = open("logs_client.txt","a")
    file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + " SE INICIA CONEXIÓN\n")
    host = socket.gethostname()  
    port = 5000 

    client_socket = socket.socket()
    client_socket.connect((host, port)) 

    message = input("(" +time.strftime("%H:%M:%S")+ ")" + " Ingrese mensaje -> ")  

    while message.lower().strip() != 'chao':
        client_socket.send(encrypt(message,alphabet,encode_alphabet).encode())  
        file.write(time.strftime("%d/%m/%y") + " " +time.strftime("%H:%M:%S") +" Mensaje enviado\n")
        data = decrypt(client_socket.recv(1024).decode(),alphabet,encode_alphabet)  # receive response
        file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") +" Mensaje recibido\n")

        print('Received from server: ' + data) 

        message = input("(" +time.strftime("%H:%M:%S")+ ")" + " Ingrese mensaje -> ")  
    
    file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + " Mensaje de cierre conexión\n")
    client_socket.close() 
    file.write(time.strftime("%d/%m/%y") + " " + time.strftime("%H:%M:%S") + " SE CIERRA CONEXIÓN\n")
    file.write("---------------------------------------------------------------------------------------\n")
    file.close()

if __name__ == '__main__':
    client_program()
