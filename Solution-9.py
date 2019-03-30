# Kasia Connell, 2019
# Solution to Question 9
# The program will read in a text file and output every second line. The program should take the filename from an argument on the command line

# Refernces: 
# Ian's video tutorial about modules https://web.microsoftstream.com/video/b8925ffa-0cf5-4fff-bfb0-b4664f704879
# Ian's video about sys https://web.microsoftstream.com/video/65df155a-ac29-460b-869d-2de6ffc6c3fc
# Import sys to execute the filename from the command line
import sys
# for the program to take the filename from the command line I set the condition to == 1
if len(sys.argv) == 1: # the number of object to be entered on the command line in order to open the textfile is set to one, i.e. Solution-9 
    print ("Opening Sample.txt now") # Print confirmation the textfile is opening
    with open("Sample.txt", "r") as f:  # Open the text file 
        # To count the lines adopted the code from https://stackoverflow.com/a/30551984
            for count, line in enumerate(f, start=0):  
                if count % 2 == 0:      # if the line is even   
                    print(line)         # print the line

else:
    print("You should enter a single filename") # if other combnation objects on the command line the text will not open and the output will advise to enter single file name
