import sys
import math

operation = input()
pseudo_random_number = int(input())
rotors = []

for i in range(3):
    rotors.append(input())

message = input()
alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def crypt(operation, numb, rotors, message):

    if operation == "ENCODE":
        new_message = ""
        new_message_list = []
        for i in range(len(message)):
            code = ord(message[i]) - 65 + numb + i
            loop = int((code) / 26)
            new_message += chr(code + 65 - 26 * loop)
            new_message_list = list(new_message)

        for rotor in rotors:
            rotor_list = list(rotor)
            for j in range(len(new_message)):
                new_message_list[j] = rotor_list[alphabet_list.index(new_message_list[j])]
        new_message = "".join(new_message_list)
        print(new_message)
    else:
        new_message = ""
        new_message_list = list(message)
        for rotor in reversed(rotors):
            rotor_list = list(rotor)
            for j in range(len(message)):
                new_message_list[j] = alphabet_list[rotor_list.index(new_message_list[j])]

        for i in range(len(message)):
            shift = numb + i
            alphabet_reversed = alphabet_list[::-1]
            new_message_list[i] = alphabet_reversed[(alphabet_reversed.index(new_message_list[i]) + shift) % 26]
            new_message = "".join(new_message_list)
        print(new_message)


crypt(operation, pseudo_random_number, rotors, message)
