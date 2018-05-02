'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''

def longest_substring(s):
    longest = s[0]
    for index, char in enumerate(s):
        temp = char
        for other_char in s[index + 1:]:
            if ord(other_char) >= ord(temp[len(temp) - 1]):
                temp += other_char
            else:
                break
        if len(temp) > len(longest):
            longest = temp
    print("Longest substring in alphabetical order is: " + longest)