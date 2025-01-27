# Write a program that continuously prompts the user for a 
# temperture (in the scale of your choosing). Every time 
# the user inputs a temperature, the program should report 
# the mean of all the values entered so far. When the user
# types in 'quit' the program should terminate.
#
# An example interaction might look like
# Input a temperature
# >> 42
# The average temperature so far is 42
# Input a temperature
# >> 26
# The average temperature so far is 34.0
# Input a temperature
# >> 52
# The average temperature so far is 40.0
# >> quit
# Goodbye
#
# You can use the sum function to sum all the values in a list
# sum(<list>)

def temperature_calculator():
    # YOUR CODE GOES HERE
    # You can delete the line below when you start adding code
    has_input = True
    temp_list = []
    temp = input("Input a temperature\n")
    while has_input:
        if temp == 'quit' or temp == 'Quit':
            print("Goodbye")
            has_input = False
        else:
            temp_list.append(int(temp))
            if len(temp_list) == 1:
                print(f'The average temperature so far is {temp}')
            else:
                print(f'The average temperature so far is {sum(temp_list)/len(temp_list)}')
            temp = input("Input a temperature\n")

if __name__ == "__main__":
    temperature_calculator()