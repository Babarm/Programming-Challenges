# Importing some libraries
import time
import math
import os
import platform


# I like to put multiple lines between each function, to make it easier to read
# But it is not required, feel free to remove

# This template is setup to run in python 3.X
# It may or may not work in python 2.X, no promises


# The main powerhouse of the program
# Use this to calculate the answer to the challenge
# It's a good idea to document the code as you write it (easier for debugging)
def run():
    # Initialize the ans variable with no value (Basically just declaring it, but not defining it)
    ans = None

    # Loading any additional data need for the program
    loadAdditional()

    # Iterate every value on the interval [1, 1000)
    # If it is divisible by (a multiple of) 3 or 5, add it to the ans value
    ans = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            ans += i

    # Returning the value of ans
    return ans



# Loads any additional data laid out by the challenge description
# Intentionally left empty to allow modular implementation
def loadAdditional():
    return None



# Loads the challenge description
def loadAboutTXT():
    with open('about.txt', 'r') as f:
        for line in f:
            # repeats until it finds the end of the description
            # this is in place so as to allow you to insert additional challenge data to the end of the about.txt file, or at least after the [END] tag
            if(line == '[END]\n'):
                break
            print(line, end='')
    print('')
    return None



# Clears the console screen to make it easier to read the program's output
def clear():
    # Linux / MacOSX and Windows have two different commands to clear the screen, so I use the platform library to detect what the user is running on their computer
    # MacOSX == Darwin
    if(platform.system() in ['Linux', 'Darwin']):
        os.system('clear')
    else:
        os.system('cls')
    return None




# Start of the program
# The above is merely function (method) definitions
# This is what calls all those functions and calculates the answer to the challenge
# Chances are you do not need to change anything from here on down
# This template is designed in such a way to allow you to only need to edit one or two functions and the program will do the rest for you
if __name__ == '__main__':

    # Clears the screen
    clear()

    # Displays the challenge description and waits for user to press [ENTER] / [RETURN]
    loadAboutTXT()
    input('Press ENTER to continue . . . ')
    print('\nCalculating...\n')
    
    # Marks the starting time of the program using the system's clock
    timeStarted = time.time()

    # Runs the challenge and calculates the answer
    ans = run()
    
    # Marks the ending time of the program using the system's clock (to be used later in data metrics)
    timeEnded = time.time()
    
    # Displays the answer to the screen
    if(isinstance(ans, int)):
        print('Answer: {0:,d}'.format(ans))
    elif(isinstance(ans, float)):
        print('Answer: {0:.10f}'.format(ans))
    else:
        print('Answer: {0}'.format(ans))

    # Formats the time taken to run the challenge in a pretty format
    # Accounts for programs that run in less than 1 second
    timeElapsed = timeEnded - timeStarted
    if(timeElapsed < 0.001):
        timeElapsed *= 1000000
        print('Completed in {0:.3f} microseconds'.format(timeElapsed))
    elif(timeElapsed < 1):
        timeElapsed *= 1000
        print('Completed in {0:.3f} milliseconds'.format(timeElapsed))
    else:
        print('Completed in {0:.3f} seconds'.format(timeElapsed))
