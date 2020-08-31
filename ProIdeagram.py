from os import system
from random import sample

# Open Notepad
def RunNotepad():
    system('notepad')
    
# Generate 5 random, non-reoccuring programming words (using .sample) from idea_lists_combined
def GenerateIdeas():
    listRandomized = sample(ideaListsCombined, k=5)
    listRandomized.sort()
    print ('Here are some helpful programming keywords: ', '[%s]' % ', '.join(map(str, listRandomized)))
    print('')
    ideaInput = input('What is your program idea(s)? ')
    ideaInput = ideaInput.title()
    ideaList.append(ideaInput)
    print('')
    print ('Program idea(s): ', '[%s]' % ', '.join(map(str, ideaList)))    

ideaList = []

# List of lists
ideaList1 = ['Health', 'Automation', 'PDF', 'Scraping', 'Transfer']
ideaList2 = ['Tech', 'GUI', 'Money' ,'School', 'Work']
ideaList3 = ['Positive', 'Dashboard', 'Email', 'Algorithm', 'Bandwidth']
ideaList4 = ['Browser', 'CD-R', 'Link', 'Template', 'Website']
ideaList5 = ['Notepad', 'Login', 'Beginner', 'Intermediate', 'Advanced']
ideaListsCombined = ideaList1 + ideaList2 + ideaList3 + ideaList4 + ideaList5

# Opening statement
print('Welcome to ProIdeagram!')
print('')
print('Start generating program ideas?')
print('')
startExit = input('Press (Enter) to start or (e) to exit: ')
startExit = startExit.lower()
if startExit == 'e':
    quit()
print('')

# Body
while startExit != 'e':
    GenerateIdeas()
    print('')
    print('Make another idea(s)?')
    print('')
    startExit = input('Press (Enter) to start or (e) to exit and open Notepad: ')
    startExit = startExit.lower()
    print('')

# Open Notepad before exiting to transpose ideas 
if startExit == 'e':
    for x in ideaList:
        print(x)
    print('')
    sortList = input('Sort list? (y) or (n): ')
    print('')
    if sortList == 'y':
        ideaList.sort()
        for x in ideaList:
            print(x)   
    print('')
    RunNotepad()
