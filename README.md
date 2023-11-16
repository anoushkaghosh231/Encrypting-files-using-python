# Encrypting-files-using-python



#INTRODUCTION

In present times, digitalization is promoted in all spheres. Therefore, data security is a priority for all. In line with this, we have developed a user-friendly software for encryption and decryption of files and records for ensuring that they are not vulnerable in case of a data breach.

Cryptography: Cryptography is the practice of securing useful information during the transmission of data from one computer to another or storing data on a computer. Cryptography deals with the encryption of plain text into ciphertext and decryption of ciphertext into plain text. Python provides support to the cryptography package that allows us to encrypt and decrypt data.

Encryption: a means of securing digital data using one or more mathematical techniques in non-human readable forms, along with a password unique to the specific data.

Decryption: the conversion of encrypted data into its original form.

 Salient Features of ‘Crypto Mania’
```
The software is capable of encrypting and decrypting text, CSV files and messages(strings).
```
The main algorithm used two methods of encryption and decryption, (1)Fernet method of cryptography module(for csv) and (2) Caesar Cipher(for text and message).

 Working of Fernet module: The fernet module of the cryptography package has inbuilt functions for the generation of the key, encryption of plaintext into ciphertext, and decryption of ciphertext into plaintext using the encrypt and decrypt methods respectively. The fernet module guarantees that data encrypted using it cannot be further manipulated or read without the key(A URL-safe base64-encoded 32-byte key). To encrypt the file, a Fernet object is created using the key created previously. Then the encrypt function is called, and the file is encrypted. 
To decrypt the file, we must again create a Fernet object using the same key that was used to encrypt the data. The decrypt function is called to get the decrypted file.



Working of Caesar Cipher: In this project, it works in the following manner: uppercase and lowercase alphabets as well as numerals are handled using Caesar Cipher. It basically rotates the characters by a specific integer. This integer is called the key. Spaces are converted to ‘|’, special characters remain the same and new line characters are converted to ~ at the time of encryption; and back for decryption. In order to make the encryption, a scrambling algorithm is added. Before decryption, data is unscrambled to subsequently get back the original text file. The key is set as 7 for text file characters and 14 for message. For eg: “A” would rotate to “H” when key=7.

 In between encryption and decryption:
After encryption of files, a token(10-digit code) will be generated, which must be entered by the user for decryption of files. No file directory will be required during decryption, and thus security of the file is ensured. The token generated, the key required during encryption as well as the file directory will be stored in a binary file as “pw.dat”. For message(string), no such token(code) is generated.
.



PACKAGES/ MODULES USED


```Cryptography(fernet)```: The fernet module of the cryptography package has inbuilt functions for the generation of the key, encryption of plaintext into ciphertext, and decryption of ciphertext into plaintext using the encrypt and decrypt methods respectively. It guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an implementation of symmetric (also known as “secret key”) authenticated cryptography. 

```OS```: This module provides functions for interacting with the operating system and provides functions like those for creating and removing directories.

```random```: An in-built module of Python, random is used to generate random numbers; give random output for a list of characters.

```pickle```: This module is used to handle binary files by serializing and de-serializing Python objects.

```path```: This module offers classes representing filesystem paths with semantics appropriate for different operating systems. Path classes are divided between pure paths, which provide purely computational operations without I/O, and concrete paths, which inherit from pure paths but also provide I/O operations.
