# -*- coding: utf-8 -*-
"""Decrypter

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YQzyAAc7J8ol-7hHr9CluHHhfY5fpDnt
"""

# ------ RANDOM ENCRYPTION ------
print("\n\nRandom Encrypter")
word = input("Enter a word/phrase to be encrypted with a random cipher: ")
def Random_Encrypter():
  # choose random number
  cipher_chooser = [1, 2, 3, 4, 5]
  selected_cipher = random.choice(cipher_chooser)
  # perform differnet cipher for each number that can be chosen
  if (selected_cipher == 1):
    print("The randmom encryption will be performed with the Atbash Cipher")
    Atbash_Cipher()
  elif (selected_cipher == 2):
    print("The randmom encryption will be performed with the Caesar Cipher")
    Caesar_Cipher()
  elif (selected_cipher == 3):
    print("The randmom encryption will be performed with the Baconian Cipher")
    Baconian_Cipher()
  elif (selected_cipher == 4):
    print("The randmom encryption will be performed with the Columnar Transposition Cipher")
    Columnar_Transposition_Cipher()
  elif (selected_cipher == 5):
    print("The randmom encryption will be performed with the Four Square Cipher")
    Four_Square_Cipher()

Random_Encrypter()

# ------ DECRYPTION ------
word = input("\n\nEnter a word/phrase that will be decrypted, which has been encrypted with any cipher: ")
def Atbash_Cipher_Decryption():
  # original alphabet list
  alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  # reversed alphabet list
  reversed_alphabet_list = [x for x in reversed(alphabet_list)]
  # encrypted word
  decrypted_word = ""
  #for each letter in the inputted word
  for letter in word:
    # add space to encryption
    if (letter == " "):
      decrypted_word += " "
    else:
      # variable index = the index of the element
      index = alphabet_list.index(letter)
      # add corresponding letter from flipped list to word
      decrypted_word += reversed_alphabet_list[index]
  # check if decryption has meaning using spellchecker package
  spell = SpellChecker()
  if (decrypted_word == ""):
    print("No valid encryption can be formed")
    # .correction returns the most probable result for the misspelled word
  elif (spell.correction(decrypted_word) == decrypted_word):
    print("The Atbash Cipher was used to encrypt this phrase. The decrypted plaintext is: ", decrypted_word)
    return True
 
def Caesar_Cipher_Decryption():
  decrypted_word = ""
  # original alphabet list
  alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  key = 0
  for key in range(1, 27):
    for letter in word:
      # add space to encryption
      if (letter == " "):
        decrypted_word += " "
      else:
        # variable index = the index of the element
        index = alphabet_list.index(letter)
        # if the index is less than max index-key
        if ((index + 1) >= key):
          #  append letter shifted right by key
          decrypted_word += alphabet_list[index-key]
        else:
          # handle index out of range
          decrypted_word += alphabet_list[(index-key) + len(alphabet_list)]
    # check if decryption has meaning using spellchecker package
    spell = SpellChecker()
    if (spell.correction(decrypted_word) == decrypted_word):
      if (decrypted_word == ""):
        print("No valid encryption can be formed")
      else:
        print("The Caesar Cipher was used to encrypt this phrase. The key used was", key, "and the decrypted plaintext is: ", decrypted_word)
        return True
    else:
      decrypted_word = ""
 
 
def Baconian_Cipher_Decryption():
  # original alphabet list
  alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  # binary alphabet list
  binary_alphabet_list = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 'bbaaa', 'bbaab']
  # encrypted word
  decrypted_word = ""
  index = 0
  while index <= len(word) - 1:
    # Joining every 5 elements to create binary code
    binary_code = word[index:index+5]
    # jump to start of next code
    index += 5
    # get index of chunk in the binary list
    if (binary_code in binary_alphabet_list):
      binary_code_index = binary_alphabet_list.index(binary_code)
      # find and append corresppodning element in plaintext alphabet
      plaintext_letter = alphabet_list[binary_code_index]
      decrypted_word += plaintext_letter
    else:
      break

  # check if decryption has meaning using spellchecker package
  spell = SpellChecker()
  if (decrypted_word == ""):
    print("No valid encryption can be formed for the Baconian Cipher")
    # .correction returns the most probable result for the misspelled word
  elif (spell.correction(decrypted_word) == decrypted_word):
    print("The Baconian Cipher was used to encrypt this phrase. The decrypted plaintext is: ", decrypted_word)
    return True
 
def Decrypter():
 Atbash_Cipher_Decryption()
 Caesar_Cipher_Decryption()
 Baconian_Cipher_Decryption()
   
 
Decrypter()
word = input("\n\nEnter a word/phrase that will be decrypted, which has been encrypted with any cipher: ")
Decrypter()
word = input("\n\nEnter a word/phrase that will be decrypted, which has been encrypted with any cipher: ")
Decrypter()