import time
from os import system
from random import sample

# Open Notepad
def RunNotepad():
    print('Opening Notepad...')
    time.sleep(1)
    system('notepad')
    
# Generate 5 random, non-reoccuring programming words (using .sample) from idea_lists_combined
def GenerateIdeas():
    list_randomized = sample(idea_lists_combined, k=5)
    list_randomized.sort()
    print ('Here are some helpful programming keywords: ', '[%s]' % ', '.join(map(str, list_randomized)))
    print('')
    idea_input = input('What is your program idea(s)? ')
    idea_input = idea_input.title()
    idea_list.append(idea_input)
    print('')
    print ('Program idea(s):', '[%s]' % ', '.join(map(str, idea_list)))    

idea_list = []

# List of lists
idea_list_1 = ['Health', 'Automation', 'PDF', 'Scraping', 'Transfer']
idea_list_2 = ['Tech', 'GUI', 'Money' ,'School', 'Work']
idea_list_3 = ['Positive', 'Dashboard', 'Email', 'Algorithm', 'Bandwidth']
idea_list_4 = ['Browser', 'CD-R', 'Link', 'Template', 'Website']
idea_list_5 = ['Notepad', 'Login', 'Beginner', 'Intermediate', 'Advanced']
idea_lists_combined = idea_list_1 + idea_list_2 + idea_list_3 + idea_list_4 + idea_list_5

# Opening statement
print('Welcome to ProIdeagram!')
print('')
print('Start generating program ideas?')
print('')
start_exit = input('Press (Enter) to start or (e) to exit: ')
start_exit = start_exit.lower()
if start_exit == 'e':
    quit()
print('')

# Body
while start_exit != 'e':
    GenerateIdeas()
    print('')
    print('Make another idea(s)?')
    print('')
    start_exit = input('Press (Enter) to start or (e) to open Notepad and exit: ')
    start_exit = start_exit.lower()
    print('')

# Open Notepad before exiting to transpose ideas 
if start_exit == 'e':
    for index, value in enumerate(idea_list, 1):
        print(f'{index}. {value}')      
    print('')
    sort_list = input('Sort list? (y) or (n): ')
    print('')
    if sort_list == 'y':
        idea_list.sort()
        for index, value in enumerate(idea_list, 1):
            print(f'{index}. {value}') 
    print('')
    RunNotepad()
