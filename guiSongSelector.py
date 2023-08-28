# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:40:30 2023

@author: jade annalise 
"""
#gui version of the songSelector program 
#uses pandas to get genres from csv file to lists 
#uses the random module to choose a song 
#uses Tkinter module to create gui, using buttons to activate the corresponding functions 5

#imports necessary modules 
import pandas as pd
from tkinter import *
import random 

#%% pandas/list
#converts csv file containing songs into dataframe
songDF = pd.read_csv("songs.csv")

#converts each column of dataframe into separate lists for each genre, uses dropna method to get rid of empty cells 
rockGenreList = songDF["rockGenre"].dropna()
metalGenreList = songDF["metalGenre"].dropna()
gothGenreList = songDF["gothGenre"].dropna()
ostGenreList = songDF["ostGenre"].dropna()

#creates empty list to hold random choices later
listOfSongs = []

#%% lotta functions
#creates function to check whether there are any duplicates in the list, y is used to parse lists
def listFromDict(y):
    j = 0                                          
    global listOfSongs
    listOfSongs = list(dict.fromkeys(listOfSongs))  #converts list to dictionary and then back to a list
    if len(listOfSongs) < int(numberEntry.get()):          #checks if no of items in list == user's no of songs
        x = int(numberEntry.get()) - len(listOfSongs)      #calucaltes diff between no of items and user's no 
        while j < x:                                #adds new songs to list while j < x 
            songsNew = random.choice(y)
            listOfSongs.append(songsNew.replace("'", "£").replace(", ", "$"))
            j += 1 
            listFromDict(y)                         #does function again to ensure no new duplicates
            
#creates function to make random song choice and append to the list to display later, replaces problem punctuation with other symbol for later
def addToList(y):
     global i
     i = 0
     global songNumber
     
     songNumber = numberEntry.get() 
     while i < int(songNumber):
             songChoices = random.choice(y)                 #makes random choice of songs in the genre list, saves to variable 
             listOfSongs.append(songChoices.replace("'","£").replace(", ", "$"))       #appends variable to list
             i += 1
        
#performs addtolist function using corresponding genre list, converts symbols back to original, puts new line in place of list commas     
def genRockSongs():
    listOfSongs.clear()
    y = rockGenreList
    addToList(rockGenreList)
    listFromDict(y)
    song.set(str(listOfSongs).replace("[","").replace("]","").replace("'","").replace(", ","\n").replace("£", "'").replace("$", ", "))
 
#performs addtolist function using corresponding genre list, converts symbols back to original, puts new line in place of list commas
def genMetalSongs():
    listOfSongs.clear()
    y = metalGenreList
    addToList(metalGenreList)
    listFromDict(y)
    song.set(str(listOfSongs).replace("[","").replace("]","").replace("'","").replace(", ","\n").replace("£", "'").replace("$", ", "))

#performs addtolist function using corresponding genre list, converts symbols back to original, puts new line in place of list commas
def genGothSongs():
    listOfSongs.clear()
    y = gothGenreList
    addToList(gothGenreList)
    listFromDict(y)
    song.set(str(listOfSongs).replace("[","").replace("]","").replace("'","").replace(", ","\n").replace("£", "'").replace("$", ", "))

#performs addtolist function using corresponding genre list, converts symbols back to original, puts new line in place of list commas
def genOSTSongs():
    listOfSongs.clear()
    y = ostGenreList
    addToList(ostGenreList)
    listFromDict(y)
    song.set(str(listOfSongs).replace("[","").replace("]","").replace("'","").replace(", ","\n").replace("£", "'").replace("$", ", "))

#%% frames
#creates the gui using frames and sets the main frame and other frames sizes, display text with instructions, text variables for displaying chosen songs     
root = Tk()
root.geometry("600x450")

mainWindow = Frame(root)
mainWindow.pack() 

leftside = Frame(root)                      #creates frame for the leftside, to hold buttons on the left
leftside.pack(side=LEFT, padx= 20)          #initiates the left frame, pads on the x axis by 80 pixels

rightside = Frame(root)                     #creates frame for the rightside, to hold buttons on the right
rightside.pack(side=RIGHT, padx = 20)       #initiates the right frame, pads on the x axis by 80 pixels

songDisplaySide = Frame(root)
songDisplaySide.pack(side=TOP, padx = 20)

#%% text labels and entry

#creates label to display the program instructions 
instruText = Label(mainWindow, font = "Congenial 12", text = "Welcome to the random song selector! \nPlease use the buttons below to select the genre of music you want to listen to.")
instruText.pack()

#creates label to display the program instructions 
boxText = Label(mainWindow, font = "Congenial 12", text = "\nPlease enter the number of songs below:")
boxText.pack()

numberEntry = Entry(mainWindow, width = 20, relief = "sunken")
numberEntry.insert(0,"1")
numberEntry.pack()

#%% buttons
#creates buttons for each of the genres, sets appearance of the buttons, sets command to the corresponding functions 
rockGenButton = Button(leftside, text = "Rock", font = "Congenial 12", width = 9, relief = "groove", command = genRockSongs)
rockGenButton.pack(padx = 10, pady = 5)
metalGenButton = Button(leftside, text = "Metal", font = "Congenial 12", width = 9, relief = "groove", command = genMetalSongs)
metalGenButton.pack(padx = 10, pady = 5)
gothGenButton = Button(rightside, text = "Goth", font = "Congenial 12", width = 9, relief = "groove", command = genGothSongs)
gothGenButton.pack(padx = 10, pady = 5)
ostGenButton = Button(rightside, text = "OSTs", font = "Congenial 12", width = 9, relief = "groove", command = genOSTSongs)
ostGenButton.pack(padx = 10, pady = 5)

#%% string variable for display
#creates the string variable to display the chosen song, sets variable to empty so that nothing displays until a button is pressed 
song = StringVar()
song.set("")
songsDisplay = Label(songDisplaySide, textvariable = song)
songsDisplay.pack(pady = 10)

#%% title and run 
#creates title for the window and calls the gui function to run 
root.title("Song Selector")
root.mainloop()