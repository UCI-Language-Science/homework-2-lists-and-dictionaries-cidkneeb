# Write a program that asks the user to input a string and then
# prints out the counts of each character used in the string.
#
# For example, if the input string is 'hello, world!' the output
# should be something like
#
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ',': 1
# ' ': 1
# 'w': 1
# 'r': 1
# 'd': 1
# '!': 1
#
# You don't have to match this format exactly, but it's important
# for the autograder that the message you print contains
# each of the character/count pairs in the following format.
# 
# '<character>': <count>
#
# You should get input from the user using the input function. Your
# code should work for arbitrary strings, including the empty string.

def char_counter():
    # YOUR CODE GOES HERE
    # You can delete the line below when you start adding code
    str = input('Enter a string: ')
    lst = list(str)
    d = {}
    for letter in lst:
        d[letter] = d.get(letter, 0) + 1
    for letter, count in d.items():
        print(f"'{letter}'': {count}")
        
if __name__ == "__main__":
    char_counter()