# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:06:57 2018

@author: Ezekiel Marvin
"""
#Dictionary Log In Program
username={ 'fireman':'match', 'woodman':'sal', 'elecman':'countzap', 'coloredman':'maddy', 'shadowman':'dark', 'magicman':'yahoot', 'gutsman':'dex', 'roll':'mayl', 'glide':'yai', 'megaman':'lan'}
user=input("Input your username: ")
if user in username: 
    passw=input("Input your password: ")
    if passw == username[user]:
        print("You are now logged in.")
    else:
        print("Password is invalid.")
else: 
    print('Username is invalid')