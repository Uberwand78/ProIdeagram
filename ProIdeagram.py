import os
import random

# Open Notepad
def RunNotepad():
    os.system("notepad")

# Generate 5 random, non-reoccuring programming words (using .sample) from idea_gen_list
def Reload():
    print(" ")
    print("Here are some helpful programming keywords: ", random.sample(idea_gen_list, k=5))
    print(" ")
    x = input("What is your program idea(s)? ")
    print(" ")
    print("----- Program idea(s): " + x.title() + " -----")

# List of lists
idea_list_1 = ["Health", "Automation", "pdf", "Scraping", "Transfer"]
idea_list_2 = ["Tech", "GUI", "Money" ,"School", "Work"]
idea_list_3 = ["Positive", "Dashboard", "Email", "Algorithm", "Bandwidth"]
idea_list_4 = ["Browser", "CD-R", "Link", "Template", "Website"]
idea_list_5 = ["Notepad", "Login", "Beginner", "Intermediate", "Advanced"]
idea_gen_list = idea_list_1 + idea_list_2 + idea_list_3 + idea_list_4 + idea_list_5

# Opening statement
print(" ")
repeat = input("Start generating program ideas? Press (Enter) to start or (e) to exit: ")
repeat = repeat.lower()

# Body
while repeat != "e":
    Reload()
    print(" ")
    repeat = input("Try making another idea(s)? Press (Enter) to start or (e) to exit: ")
    repeat.lower()
    
# Exit and open Notepad
if repeat == "e":
    RunNotepad()
