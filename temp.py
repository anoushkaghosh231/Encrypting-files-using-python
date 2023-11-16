# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
from cryptography.fernet import Fernet
import random
import pickle
import os
from pathlib import Path


print("    ⢀⣀⣤⣤⣤⣤⣤⣤⣤⣀  ⣠⣤⣤⣤⣀⡠   ")
print("  ⢀⣴⠟⠉⣀⣀⣀⣀⣀⣀⡀⠉⣷⢿⣭⣽⠿⢿⣿⣿⣦⡀ ")
print("  ⣾⠁⢠⣾⠋⠉⠉⠉⠉⠉⠙⣾⠇⠛⣿⠁   ⢹⠞⣷⣷ ")
print("  ⣿ ⢸⡇         ⢸⣆⢠⣯⣷⣵⣴⣟⣶⣿⣿⠇")
print("  ⣿ ⢸⡇         ⢸⢯⣿⡈⠛⠛⢋⡿⢻⣿⡿ ")
print("⣴⠗⠛⠛⠛⠛⠚⠛⠛⠛⠛⠛⠒⠚⠛⠛⠺⣤⣼⣿⣷⡿⠋  ")
print("⡇                     ⣿⣿⣟⣇    ")
print("⡇                     ⣿⣿⣿⣿⡆   ")
print("⡇   CRYPTO MANIA      ⣿⣿⣿⣟ ")
print("⡇                     ⣿⣿⣿⣿⠇   ")
print("⡇                     ⣿⣿⣿⡄   ")
print("⡇                     ⣿⣿⣿⠋   ")
print("⠿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⠋    ")
print('Welcome to Crypto mania!!')
print("Your one stop destination for encryption and decryption services!")
print()
print("For file:\nInput the file directory. If found valid, the file would be rewritten in encrypted format and you will be provided with a token. For Decryption, input the token first to decrypt.\nFor message(words or sentences):\nJust encrypt and decrypt with one click!")
print("Following are the services available and their corresponding number to be entered:\n(1)Encryption: text file(.txt)\n(2) Decryption: text file(.txt)")
print("(3) Encryption: csv file/excel file (.csv)")
print("(4) Decryption: csv file/excel file (.csv)")
print("(5) Message encryption")
print("(6) Message decryption")
print("**************")
print()


def e3(filename):
    key = Fernet.generate_key()  
    with open('filekey.key', 'wb') as filekey: 
       filekey.write(key)        
    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 
    fernet = Fernet(key)     
    with open(filename, 'rb') as file: 
        original = file.read() 
    encrypted = fernet.encrypt(original) 
    with open(filename, 'wb') as encrypted_file: 
        encrypted_file.write(encrypted)
    print("Encryption of",filename," successful")
    file.close()
    encrypted_file.close()
    #generating token
    mylist = ["1", "2", "3","4","5","6","7","8","9"]
    random.shuffle(mylist)
    pw="".join(mylist)
    print("Here's the token:",pw,"\nSave it for decryption")
    
    db=[filename,pw,key,fernet]
    dbfile = open('pw.dat', 'ab')
    pickle.dump(db, dbfile)                     
    dbfile.close()
    
    
def e4():
    l=str(input("Enter token:"))
    dbfile = open('pw.dat', 'rb')
    o=False
    try:
        while True:
            b = pickle.load(dbfile)
            if b[1]==l:
                o=True
                filename=Path(b[0])
                key=b[2]
                fernet = b[3]
                with open(filename, 'rb') as enc_file: 
                    encrypted = enc_file.read() 
                decrypted = fernet.decrypt(encrypted)
                with open(filename, 'wb') as dec_file: 
                    dec_file.write(decrypted)
                print("Decryption of ",filename," successful")
                enc_file.close()
                dec_file.close()
            
    except EOFError:
        if o==False:
                print("token not found")
        dbfile.close()
    

def e1(filename):
    key=7
    f1=open(filename,'r') 
    r_len=len(f1.readlines()) 
    f1.seek(0,0)
    r_=''
    for i in range(r_len): 
        r_+=f1.readline().replace('\n','')+'~'
    f1.close()

    string_encrypted='' 
    for i in r_:
        if i.isupper():
            if (ord(i)+key)<=ord('Z'):
                term=chr(ord(i)+key)
            else:
                ch=ord('Z')-ord(i) 
                term=chr(ord('A')-ch+key-1)
            string_encrypted+=term 
        elif i.islower():
            if (ord(i)+key)<=ord('z'): 
                term=chr(ord(i)+key)
            else:
                ch=ord('z')-ord(i)
                term=chr(ord('a')-ch+key-1)
            string_encrypted+=term 
        elif i.isdigit():
            if (int(i)+key)<=9:
                term=str(int(i)+key) 
            else:
                ch=9-int(i) 
                term=str(0-ch+key-1)
            string_encrypted+=term 
        elif i.isspace():
            string_encrypted+='|' 
        elif i=='~':
            string_encrypted+='~'
        else:
            string_encrypted+=i
    
    string_scramble=string_encrypted[0::2]+string_encrypted[1::2]
    string=''
    j=0
    for i in range(len(string_scramble)+len(string_scramble)//100):
        if i%100==0 and i!=0:
            string+='\n' 
        else:
            string+=string_scramble[j] 
            j+=1
    f2=open(filename,'w') 
    f2.write(chr(key+64)+'\n') 
    f2.write(string)
    
    mylist = ["1", "2", "3","4","5","6","7","8","9"]
    random.shuffle(mylist)
    pw="".join(mylist)
    print("Here's the token:",pw,"\nSave it for decryption")
    
    db=[filename,pw]
    dbfile = open('pw.dat', 'ab')
    pickle.dump(db, dbfile)                     
    dbfile.close()
    f2.close()


def e2():
    key=7
    l=str(input("Enter token:"))
    dbfile = open('pw.dat', 'rb')
    o=False    
    try:
        while True:
                b = pickle.load(dbfile)
                if b[1]==l:
                    o=True
                    filename=b[0]
                    f1=open(filename,'r')
                    key=ord((f1.readline()).replace('\n',''))-64 
                    r_=f1.read().split()
                    while '\n' in r_: 
                        r_.remove('\n')
                    string=''
                    for i in range(len(r_)):
                        string+=r_[i] 
                    f1.close()
                 
                    s_check='' 
                    s_1_check=0 
                    s_2_check=0
                    if len(string)%2==0: 
                        s_1=string[0:len(string)//2] 
                        s_2=string[len(string)//2:len(string)]
                    else:
                        s_1=string[0:(len(string)+1)//2]
                        s_2=string[(len(string)+1)//2:len(string)]
                    for i in range(len(string)): 
                        if i%2==0:
                            s_check+=s_1[s_1_check] 
                            s_1_check+=1
                        else:
                            s_check+=s_2[s_2_check] 
                            s_2_check+=1

                    string_decrypted='' 
                    for i in s_check:
                        if i.isupper():
                            if (ord(i)-key)>=ord('A'): 
                                term=chr(ord(i)-key)
                            else:
                                ch=ord('A')-ord(i) 
                                term=chr(ord('Z')-ch-key+1)
                            string_decrypted+=term 
                        elif i.islower():
                            if (ord(i)-key)>=ord('a'):
                                term=chr(ord(i)-key) 
                            else:
                                ch=ord('a')-ord(i) 
                                term=chr(ord('z')-ch-key+1)
                            string_decrypted+=term 
                        elif i.isdigit():
                            if (int(i)-key)>=0: 
                                term=str(int(i)-key)
                            else:
                                ch=0+int(i)
                                term=str(9+ch-key+1) 
                            string_decrypted+=term
                        elif i=='|':
                            string_decrypted+=' ' 
                        elif i=='~':
                            string_decrypted+='\n' 
                        else:
                            string_decrypted+=i
                    # Writing to File 
                    f2=open(filename,'w')
                    f2.write(string_decrypted)  
                    f2.close()
                    print("Decryption of ",filename," successful")    
    except EOFError:
        if o==False:
            print("token not found")
        
        dbfile.close()

def e5():
    r_=input("Enter string to be encrypted:")
    key=14
    string_encrypted='' 
    for i in r_:
        if i.isupper():
            if (ord(i)+key)<=ord('Z'):
                term=chr(ord(i)+key)
            else:
                ch=ord('Z')-ord(i) 
                term=chr(ord('A')-ch+key-1)
            string_encrypted+=term 
        elif i.islower():
            if (ord(i)+key)<=ord('z'): 
                term=chr(ord(i)+key)
            else:
                ch=ord('z')-ord(i)
                term=chr(ord('a')-ch+key-1)
            string_encrypted+=term 
        elif i.isdigit():
            if (int(i)+key)<=9:
                term=str(int(i)+key) 
            else:
                ch=9-int(i) 
                term=str(0-ch+key-1)
            string_encrypted+=term 
        elif i.isspace():
            string_encrypted+='|' 
        else:
            string_encrypted+=i
    print("encrypted string:",string_encrypted)

def e6():
    key=14
    s_check=input("Enter string to be decrypted:")
    string_decrypted=""
    for i in s_check:
        if i.isupper():
            if (ord(i)-key)>=ord('A'): 
                term=chr(ord(i)-key)
            else:
                ch=ord('A')-ord(i) 
                term=chr(ord('Z')-ch-key+1)
            string_decrypted+=term 
        elif i.islower():
            if (ord(i)-key)>=ord('a'):
                term=chr(ord(i)-key) 
            else:
                ch=ord('a')-ord(i) 
                term=chr(ord('z')-ch-key+1)
            string_decrypted+=term 
        elif i.isdigit():
            if (int(i)-key)>=0: 
                term=str(int(i)-key)
            else:
                ch=0+int(i)
                term=str(9+ch-key+1) 
            string_decrypted+=term
        elif i=='|':
            string_decrypted+=' '
        else:
            string_decrypted+=i
    print("decrypted string:",string_decrypted)
    


while 1:
    n=int(input("Enter the no.(1-6) for the service you want to avail. Enter 0 to stop input."))
    if n==1:
        print("Encryption text file")
        filename=input("input file direcory as absolute path")
        isFile=True
        isFile = os.path.isfile(filename)
        if isFile==False:
            print("enter valid directory")
            continue
        e1(filename)
    elif n==2:
        print("Decrytion text file")
        e2()
    elif n==3:
        print("Encryption csv file")
        filename=input("input file direcory as absolute path:")
        isFile=True
        isFile = os.path.isfile(filename)
        if isFile==False:
            print("enter valid directory")
            continue
        e3(filename)
    elif n==4:
        print("Decryption csv file")
        e4()
    elif n==5:
        print("MessageCryption \nMessage Ecryption")
        e5()
    elif n==6:
        print("MessageCryption \nMessage Decryption")
        e6()
    elif n==0:
        print("Thankyou for using")
        break
    else:
        print("Enter valid no.(0-6)")
            
            
