'''
Alejandro Olmedo
ao2267
DataScience BootCamp Assignment Week 1
'''
# Run the following code

'''
1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word

2. Iterate through the following list of animals and print each one in all caps.
 animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.

4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
'''

# Function for Question 1 
def count_vowels(word):
    vowels = "aeiouAEIOU"     # List of vowels and their capital letters
    count = 0                 # Counter for vowels
    for letter in word:
        if letter in vowels:
            count += 1
    return count

# Function for Question 1 
def sum_of_integers(a, b):
  return (a + b)

# Main function
def main():
  ##### Test for Q1 #####
  print("----------------------------------------------------------------------------------------------------------------")
  print("1. Write a function  count_vowels(word) that takes a word as an argument and returns the number of vowels in the word. \n")
  inputword = input("Enter a word: ")
  numofVowels = count_vowels(inputword)
  print("Number of vowels in",'"', inputword ,'"',":" , numofVowels)
  print("\n")

  ##### Test for Q2 #####
  print("----------------------------------------------------------------------------------------------------------------")
  print("2. Iterate through the following list of animals and print each one in all caps. \n animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther'] \n ")
  animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
  for animal in animals:
    print(animal.upper(), end= ' ')
  print("\n")

  ##### Test for Q3 #####
  print("----------------------------------------------------------------------------------------------------------------")
  print("3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even. \n")
  for i in range(1, 21):
      print(i, end=' ')
  print("\n")

  ##### Test for Q4 #####
  print("----------------------------------------------------------------------------------------------------------------")
  print("4. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum. \n")
  a = int(input("Enter first integer: "))
  b = int(input("Enter second integer: "))
  sum = sum_of_integers(a, b)
  print("Sum of", a, "and", b, "is:", sum)
  print("\n")


if __name__ == "__main__":
    main()