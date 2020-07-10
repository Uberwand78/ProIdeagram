import random, os

# Open Notepad
def RunNotepad():
    os.system("notepad")

# Generate 5 random, non-reoccuring programming words (.sample) from idea_lists_combined
def GenerateIdeas():
    print("")
    list_randomized = random.sample(idea_lists_combined, k=5)
    list_randomized.sort()
    print("Here are some helpful programming keywords: ", list_randomized)
    print("")
    idea_input = input("What is your program idea(s)? ")
    idea_input = idea_input.title()
    print("")
    print("Program idea(s): ", idea_input)

# List of lists
idea_list_1 = ["Health", "Automation", "pdf", "Scraping", "Transfer"]
idea_list_2 = ["Tech", "GUI", "Money" ,"School", "Work"]
idea_list_3 = ["Positive", "Dashboard", "Email", "Algorithm", "Bandwidth"]
idea_list_4 = ["Browser", "CD-R", "Link", "Template", "Website"]
idea_list_5 = ["Notepad", "Login", "Beginner", "Intermediate", "Advanced"]
idea_lists_combined = idea_list_1 + idea_list_2 + idea_list_3 + idea_list_4 + idea_list_5

# Opening statement
print("Welcome to ProIdeagram!")
print("")
start_exit = input("Start generating program ideas? Press (Enter) to start or (e) to exit: ")
start_exit = start_exit.lower()

# Body
while start_exit != "e":
    GenerateIdeas()
    print("")
    start_exit = input("Try making another idea(s)? Press (Enter) to start or (e) to exit and open Notepad: ")
    start_exit.lower()
    
# Exit and open Notepad
if start_exit == "e":
    RunNotepad()
