# assignment: programming assignment 4
# author: shreya hiremath
# date: August 6, 2022
# file: cipher.py is a program that encoder-decoder program that uses a Caesar cipher.
# input: strings and files
# output: decrypted and encryted messages (strings)



def readfile():


   

      try:
         message = open(name_a, "r")
         
         
       


      except FileNotFoundError:
         print(f"The selected file cannot be open for reading!\n", end = "")
         raise ValueError("error")

      


      else:
         x = message.read()
         message.close()
         return x



def writefile(message):


    try:
        w = open(name_b, "w+")

    except FileNotFoundError:
       print(f"The selected file cannot be open for writing!\n")
       raise ValueError("error")

    else:
       w.write(message)
       w.close()


   

def encode(plaintext, shift = 3):

    cipherText = ""

    for n in plaintext:

        if n.isupper():

            n_unicode = ord(n)
            n_index = ord(n) - ord("A")
            new_index = (n_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            cipherText = cipherText + new_character

        else:
            cipherText += n

       

    print(f"Plaintext:\n{plaintext}Ciphertext:\n{cipherText}", end = "")

    to_list(cipherText)
    
    
    return cipherText



         
  

def decode(cipherText, shift = -3):

   plaintext = ""

   for n in cipherText:

      if n.isupper():

         n_unicode = ord(n)

         n_index = ord(n) + ord("A")

         new_index = (n_index + shift) % 26

         new_unicode = new_index + ord("A")

         new_character = chr(new_unicode)

         plaintext = plaintext + new_character

      else:
         plaintext += n


   print(f"Ciphertext:\n{cipherText}Plaintext:\n{plaintext}", end = "")

   to_list(plaintext)
   

   return plaintext


def to_string(text):
      s=""
      for i in text:
            s+=i
      return s


def to_list(string):
      return list(string)
cipherText = ""
string = cipherText
string_list = to_list(string)
print(to_string(string_list))




if __name__ == '__main__':
    while True:
        choice = input("Would you like to encode or decode the message?\nType E to encode, D to decode, or Q to quit: \n").upper()

        if choice == 'E':
            while True:
                try:
                   name_a = input("Please enter a file for reading: \n")
                   message = readfile()
                except ValueError:
                    continue
                try:
                    name_b = input("Please enter a file for writing: \n")
                    cipher=encode(message)
                    writefile(cipher)
                    break
                except ValueError:
                    continue

        if choice == 'D':
            while True:
                try:
                   name_a = input("Please enter a file for reading: \n")
                   message = readfile()

                except ValueError:
                    continue
                try:
                    name_b = input("Please enter a file for writing: \n")                    
                    plain=decode(message)
                    writefile(plain)
                    break
                except ValueError:
                    continue

                
        elif choice == 'Q':
            print("Goodbye!")

            break  

