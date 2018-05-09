#!/usr/bin/env python3

import collections
import os
import socket
import string
import random
import hashlib
import trivial_ddbef1dec8625b60d0ba03e3f3dd86388928a19d53c217df8968554df1068398 as td


TCP_IP = '127.0.0.1'
TCP_PORT = 5419
BUFFER_SIZE = 1024
CHARS = string.ascii_letters + string.digits

def str_gen(length, str_start):

    #return (str_start + ''.join(random.choice(CHARS) for _ in range(length)))
    return 'Hello123456'

def tryhard(str_start, remaining_len, hash_end):
    # get a string to try
    while 1:
        attempt = str_gen(remaining_len, str_start)
        print('Trying %s' % attempt)
        m = hashlib.sha256()
        m.update(attempt.encode())
        full_hash = m.hexdigest()
        print(full_hash[-6:])
        print(hash_end)
        if hash_end == full_hash[-6:]:
            print('Found it! %s' % attempt)
            return attempt


def foo():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (TCP_IP, TCP_PORT) )
    data = s.recv(BUFFER_SIZE)
    print(data)
    # data should look like this b'Give me a string starting with 0MFMOA6mci of length 16 so its sha256sum ends in ffffff.\n'
    msg = data.decode()
    str_start = msg.split()[6]
    str_len = int(msg.split()[9])
    hash_end = 'ef9980'
    print('String start: %s' % str_start)
    print('String len : %d' % str_len)
    print('Hash must end with: %s' % hash_end)

    remaining_len = str_len - len(str_start)
    answer = tryhard(str_start, remaining_len, hash_end)
    print('Answer: %s' % answer)
    s.send(answer.encode() + b'\n')
    data = s.recv(BUFFER_SIZE)
    print(data)
    # Now onto the next step!
    # Need to send...
    # b'keystream [iv] [number of bytes]
    # iv must be len(10)
    # number of bytes must be 1 - 16
    # Then I send...
    # guess [key]

    s.close()


def encrypt():
    index_not_affected = set([i for i in range(288)])

    for i in range(1000):
        key = os.urandom(10)
        init_list = td.bytestobits(key)
        init_list += [0]*205
        init_list += [1, 1, 1]
        state = collections.deque(init_list)

        for j in range(576):

            t_1 = state[65]  ^ state[92]
            t_2 = state[161] ^ state[176]
            t_3 = state[242] ^ state[287]

            out = t_1 ^ t_2 ^ t_3

            s_1 = t_1 ^ state[90]  & state[91]  ^ state[170]
            s_2 = t_2 ^ state[174] & state[175] ^ state[263]
            s_3 = t_3 ^ state[285] & state[286] ^ state[68]

            state.rotate(1)

            state[0] = s_3
            state[93] = s_1
            state[177] = s_2

            #return out
        for k in range(len(init_list)):
            if init_list[k] != state[k]:
                if k in index_not_affected:
                    index_not_affected.remove(k)
        print(index_not_affected)

    return index_not_affected



"""
Starting state:
    Initial state
[0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

State after the warmup (only 1 round)
[1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
"""

def determine_guess():

    return random.choice([0, 1])


def decrypt(prev_guesses, attempt_num):
    """
    The logic works for for reversing a state.
    The problem is that I don't know the state, so I am going to attempt to bring in a bit
    and knowing the number of rotations the state has used I'm going to try and weed
    out some initial states that arent possible
    lets assume the server gives me 'FF' back ([1, 1, 1, 1, 1, 1, 1, 1]).
    What can I do knowing this info?
    """
    # I asked for 1 byte, so the state machine went through 576 + 8 iterations.
    # That means that the return value is t_1 ^ t_2 ^ t_3
    # 577th iteration returned a 1 so...
    #     (state[65] ^ state[92]) ^ (state[161] ^ state[176]) ^ (state[242] ^ state[287]) = 1
    # so 1 of these 'groups' has to have different members
    # state[65] != state[92] and state[161] == state[176] and state[242] == state[287]
    #         1 != 0                      1 == 1                       1 == 1
    #         1 != 0                      1 == 1                       0 == 0
    #         1 != 0                      0 == 0                       1 == 1
    #         1 != 0                      0 == 0                       0 == 0
    #         0 != 1                      1 == 1                       1 == 1
    #         0 != 1                      1 == 1                       0 == 0
    #         0 != 1                      0 == 0                       1 == 1
    #         0 != 1                      0 == 0                       0 == 0
    # state[65] == state[92] and state[161] != state[176] and state[242] == state[287]
    #         1 == 1                      1 != 0                       1 == 1
    #         1 == 1                      1 != 0                       0 == 0
    #         0 == 0                      1 != 0                       1 == 1
    #         0 == 0                      1 != 0                       0 == 0
    #         1 == 1                      0 != 1                       1 == 1
    #         1 == 1                      0 != 1                       0 == 0
    #         0 == 0                      0 != 1                       1 == 1
    #         0 == 0                      0 != 1                       0 == 0
    # state[65] == state[92] and state[161] == state[176] and state[242] != state[287]
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0
    #         1 == 1                      1 == 1                       1 != 0

    # Round 1
    # Guess for 0, 93, 177
    # Guess for 66, 69, 91, 92, 162, 171, 175, 176, 243, 264, 286, 287
    # Do stuff and rotate left so now we have guesses at
    # Guesses: 65, 68, 90, 91, 92, 161, 170, 174, 175, 176, 242, 263, 285, 286, 287
    # Round 2
    # Additional guesses: 0, 93, 177, 171, 66, 264, 162, 69, 243
    # Do stuff and rotate left so now we have guesses at

    state = [None]*288

    # I think i want to do guesses = { 'guess_1' :{'round_0' : { 0 : 1,
    #                                                     93 : 1,
    #                                                    177 : 0, etc...
    #                                              'round_1' : { 0 : 1,
    #                                                     93 : 0,
    #                                                    177 : 1, etc...

    for i in range(575+1):

        req_indexes = ['0', '66', '69', '91', '92', '93', '162', '171', '175', '176', '177',
                       '243', '264', '286', '287']
        for index in req_indexes:
            if state[index] is None:
                # Make a guess and record it
                bit_guess = determine_guess()
                state[index] = bit_guess

        new_177 = state[177]
        new_93 = state[93]
        new_0 = state[0]

        #s_1 = (state[66] ^ state[93]) ^ ((state[91] & state[92]) ^ state[171])
        # solve for state[93]
        a = state[91] & state[92]
        b = a ^ state[171]
        c = new_93 ^ b
        orig_93 = c ^ state[66]

        # solve for state 177
        a = state[175] & state[176]
        b = a ^ state[264]
        c = new_177 ^ b
        orig_177 = c ^ state[162]

        #solve for state 0
        a = state[286] & state[287]
        b = a ^ state[69]
        c = new_0 ^ b
        orig_0 = c ^ state[243]

        # Write the old values back
        state[93] = orig_93
        state[177] = orig_177
        state[0] = orig_0

        # Now that we know the original values, rotate 1 to the right
        state.rotate(-1)

    return state
