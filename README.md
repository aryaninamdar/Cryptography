# Cryptography
A project which encrypts plaintext messages by implementing 5 different ciphers.

## What is a Cipher?

In cryptography, a cipher (or cypher) is an algorithm for performing encryption or decryption—a series of well-defined steps that can be followed as a procedure.

## Atbash Cipher

The Atbash Cipher is a very common, simple substitution cipher. It simply reverses the plaintext alphabet to create the ciphertext alphabet. That is, the first letter of the alphabet is encrypted to the last letter of the alphabet, the second letter to the second last letter and so forth.

Plaintext Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Ciphertext Alphabet: ZYXWVUTSRQPONMLKJIHGFEDCBA

Example Text: hello

Encryption: svool

## Caesar Cipher

The Caesar cipher, also known as the shift cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. This shift is determined by the value of the key of the cipher

Example key: 3

Plaintext Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Ciphertext Alphabet: DEFGHIJKLMNOPQRSTUVWXYZABC

Example text: hello

Encryption: khoor

## Baconain Cipher

The Baconian cipher is a substitution cipher in which each letter is replaced by a sequence of 5 characters. Each sequence consists of a's and b's that are meant to resemble binary codes (0's and 1's)

For a table of the ciphertext replacements for each alphabet and a deeper understanding of this cipher, please visit: https://www.geeksforgeeks.org/baconian-cipher/

## Columnar Transposition Cipher

In a Columnar Transposition Cipher, the message is written out in rows of a fixed length, and then read out again column by column, and the columns are chosen in some scrambled order. Both the width of the rows and the permutation of the columns are usually defined by a keyword.

For a visual and in-depth example of this cipher, please visit: https://www.youtube.com/watch?v=N2Lv2QcehTQ

## Four Square Cipher

The four-square cipher uses four 5 by 5 matrices arranged in a square. Each of the 5 by 5 matrices contains 25 letters, usually the letter 'j' is merged with 'i'. In general, the upper-left and lower-right matrices are the "plaintext squares" and each contain a standard alphabet. The upper-right and lower-left squares are the "ciphertext squares" and contain a mixed alphabetic sequence. The ciphertext squares can be generated using a keyword (dropping duplicate letters), then fill the remaining spaces with the remaining letters of the alphabet in order. Alternatively the ciphertext squares can be generated completely randomly. The four-square algorithm allows for two separate keys, one for each of the two ciphertext matrices.

For instructions on how to encrypt messages using the Four Square Cipher, please visit: http://practicalcryptography.com/ciphers/classical-era/four-square/
