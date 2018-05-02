'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def how_often(s):
    amount = 0
    end = 3
    for start in range(len(s)):
        if s[start:end] == "bob":
            amount += 1
        end += 1
    print("Number of times bob occurs is: " + str(amount))
        