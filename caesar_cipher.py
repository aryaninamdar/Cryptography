# -*- coding: utf-8 -*-
"""Caesar Cipher

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ukg4SwvEW-TQRi0FcM61-G9zrmeAZpwP
"""

# Caesar Cipher: Takes each letter from original word and replaces it with the letter in the same list that is shifted from the original position by a certain amount (key)
def Caesar_Cipher():
  print("\n\nCAESAR CIPHER")
  # take inputted key from user
  key = int(input("Insert the key number for the Caesar Cipher: "))
  # original alphabet list
  alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  # alphabet list which will be shifted... shift list by a certain key
  shifted_alphabet_list = []
  # for each character/element in the alphabet list
  for char in alphabet_list:
    # variable index = the index of the element
    index = alphabet_list.index(char)
    # if the index is less than max index-key
    if (index <= (len(alphabet_list) - 1) - key):
      #  append letter shifted right by key
      shifted_alphabet_list.append(alphabet_list[index+key])
    else:
      # this is done to handle the letters that when shifted will yield an error. The error will be an out of range error.
      # for example, if we try to shift the letter x by 3 units, the new index will be out of range
      # this algorithm subtracts the length of the list from the new index to brring it back in range 
      shifted_alphabet_list.append(alphabet_list[(index+key) - len(alphabet_list)])

  # take input from the user
  word = input("Enter a word/phrase to be encrypted with the Caesar Cipher: ")
  # iterate through every letter in the word
  encrypted_word_list = []
  for letter in word:
    # if there is a space
    if (letter == " "):
      # append space to new word list
      encrypted_word_list.append(" ")
    # if lowercase version of letter is present in the alphabet_list
    if (letter.lower() in alphabet_list):
      # assign the index of the lowercase version of the letter in the list to a variable called letter_index
      letter_index = alphabet_list.index(letter.lower())
      # create variable corresponding_letter which equals the letter in the reversed_alphabet_list which has the same index as the original letter in the original list
      corresponding_letter = shifted_alphabet_list[letter_index]
      # if letter is uppercase
      if (letter.isupper() == True):
        # append the uppercase leter to list by using .upper()
        encrypted_word_list.append(corresponding_letter.upper())
      else:
        # append lowercase letter
        encrypted_word_list.append(corresponding_letter)

  # convert the new word list into a string
  encrypted_word = ''.join([str(elem) for elem in encrypted_word_list])
  # handle exception of no input or integer input
  if (encrypted_word == ""):
    print("No valid encryption can be formed")
  else:
    print("The encrypted word/phrase is: ")
    print(encrypted_word)