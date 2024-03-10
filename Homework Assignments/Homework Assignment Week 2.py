'''
Alejandro Olmedo
ao2267
DataScience BootCamp Assignment Week 2

QUESTIONS:
 1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
 df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
 2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).
 df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
 3) How to get the rows of a dataframe with row sum > 100?
 df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
 4)Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this array into two separate 2D arrays, 
 where one represents the rows and the other represents the columns. Write a function, preferably using a lambda function, 
 to calculate the sum of each row and each column separately, and return the results as two separate NumPy arrays
'''

# Importing libraries
import pandas as pd
import numpy as np

# Function for Question 1
def question1():
  print("1) From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).")
  df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
  print(df[['Manufacturer', 'Model', 'Type']].iloc[::20, :])
  print("----------------------------------------------------------------\n")

# Function for Question 2
def question2():
  print("2) Replace missing values in Min.Price and Max.Price columns with their respective mean (check documentation).")
  df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
  df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
  df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
  print(df)
  print("----------------------------------------------------------------\n")

# Function for Question 3
def question3():
  print("3) How to get the rows of a dataframe with row sum > 100?")
  df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
  print(df[df.sum(axis=1) > 100])
  print("----------------------------------------------------------------\n")

# Function for Question 4
def question4():
  print("4) Create a 4x4 NumPy array filled with random integers between 1 and 100. Then, reshape this array into two separate 2D arrays, where one represents the rows and the other represents the columns. Write a function, preferably using a lambda function, to calculate the sum of each row and each column separately, and return the results as two separate NumPy arrays.")
  np.random.seed(100)
  arr = np.random.randint(1, 100, 16).reshape(4, 4)
  print("Original Array:")
  print(arr)
  print("\n")
  print("Reshaped Array (Rows):")
  print(arr.reshape(2, 8))
  print("\n")
  print("Reshaped Array (Columns):")
  print(arr.reshape(8, 2))
  print("\n")
  print("Sum of each row:")
  print(np.apply_along_axis(lambda x: np.sum(x), axis=1, arr=arr))
  print("\n")
  print("Sum of each column:")
  print(np.apply_along_axis(lambda x: np.sum(x), axis=0, arr=arr))
  print("\n")


# Main function
def main():
    question1()
    question2()
    question3()
    question4()

if __name__ == "__main__":
    main()
