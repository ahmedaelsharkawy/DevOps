# -*- coding: utf-8 -*-
"""
Created on Fri Nov  11 10:00:42 2022

@author: Ahmed ElSharkawy
"""
import sys
import re



file_name = './users.txt'

def find_first_name(text):
    '''
    This function extract the first name from each line
    Parameters
    ----------
    text : string
        DESCRIPTION.

    Returns
    -------
    TYPE :string
        return first user name.

    '''
    x_list = []
    x_list = text.split(" ") # parse the input line into group of item in list
    return x_list[0]

def find_email(text):
    '''
    this function use regular expression package to exctract email form text

    Parameters
    ----------
    text : string
        DESCRIPTION.

    Returns
    -------
    newmail : string
        return email or empty string.

    '''
    email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+", text)
    
    # use this to exclude emails without domain like @localhost
    # email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text) 
    try:
        email = email[0]
    except:
        pass
    return email


def check_odd_even(num):
    '''
    this function check the input number and return the (odd or even) string. 
    Parameters
    ----------
    num : int
        the number to check if it is odd or even.

    Returns
    -------
    num_type : string
        odd or even.

    '''
    if not num%2:
        num_type = 'even'
        #print('even:',num%2)
    else:
        num_type = 'odd'
        #print('odd:',num%2)
    return num_type
            
def find_id(text):
    '''
    Parameters
    ----------
    text : string
        text need to be parsed to found the id.

    Returns
    -------
    uid : integer
        the user id number.
    uid_type : string
        the type of the id: even or odd.

    '''
    uid = ''
    uid_type = ''
    x_list = []
    x_list = text.split(" ") # parse the input line into group of item in list
    for item in x_list:
        # verifiy that the item is intger 
        try:
            uid = int(item)
        except:
            pass
                   
    if uid:
        uid_type = check_odd_even(uid)
    return uid, uid_type


def parse_line(new_line):
    first_name = find_first_name(new_line)
    email = find_email(new_line)
    user_id, id_type = find_id(new_line)
    if user_id and email:
        print("The {} of {} is {}".format(user_id,email,id_type))



with open(file_name) as file_in:
    for line in file_in:
        if not line.strip():  # to ignore empty lines 
            pass
        else:
            parse_line(line.rstrip('\n'))

