# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:04:29 2023

@author: jade annalise
"""
#programme to randomly select songs of certain genres as chosen by the user
#reads from csv file to get all the genres and songs 
#uses lists to store songs in certain genre
#uses function and while loop to remove and replace duplicates in lists 

#importing needed libraries
import pandas as pd 
import random 


#converts data in csv file to dateframe 
songDF = pd.read_csv("songs.csv")

#converts each genre column in dataframe to its own appropriately named list
#and removes any empty cells from each 
rockGenreList = songDF["rockGenre"].dropna()
metalGenreList = songDF["metalGenre"].dropna()
gothGenreList = songDF["gothGenre"].dropna()
ostGenreList = songDF["ostGenre"].dropna()

#creates a list to hold the randomly chosen songs later 
listOfSongs = []

#creates function to check whether there are any duplicates in the list, y is used to parse lists
def listFromDict(y):
    j = 0                                           #creates variable to use in while loop
    global listOfSongs
    listOfSongs = list(dict.fromkeys(listOfSongs))  #converts list to dictionary and then back to a list
    if len(listOfSongs) < int(songNumber):          #checks if no of items in list == user's no of songs
        #print(len(listOfSongs))
        x = int(songNumber) - len(listOfSongs)      #calucaltes diff between no of items and user's no 
        while j < x:                                #adds new songs to list while j < x 
            songsNew = random.choice(y)
            listOfSongs.append(songsNew.replace("'", "£").replace(", ", "$"))
            j += 1 
            listFromDict(y)                         #does function again to ensure no new duplicates

def addToList(y):
     global i
     songChoices = random.choice(y)
     listOfSongs.append(songChoices.replace("'","£").replace(", ", "$"))
     i += 1
      
def welcomeMenu():
    print("Welcome to the song selector! If you let me know what genre you want to listen to, I'll give you a song suggestion from that genre!")
    print("Here is the list of genres: \n1. Rock\n2. Metal\n3. Goth\n4. OSTs")
    global i 
    i = 0 
    global songNumber
    songNumber = input("How many songs do you want?: ")
    choice = input("Please make your selection using the corresponding numbers: ")
    
    while i < int(songNumber):
        if choice == "1":
            genreName = "Rock"
            y = rockGenreList
            addToList(rockGenreList)
        elif choice == "2":
            genreName = "Metal"
            y = metalGenreList
            addToList(metalGenreList)
        elif choice == "3":
            genreName = "Goth"
            y = gothGenreList
            addToList(gothGenreList)
        elif choice == "4":
            genreName = "OSTs"
            y = ostGenreList
            addToList(ostGenreList)
        else: 
            print("Please use the correct inputs of 1, 2, 3, or 4!")
    
    listFromDict(y)
    print("\nYou have chosen " + genreName + ". Here is your random selection:\n")
    print(str(listOfSongs).replace("[","").replace("]","").replace("'","").replace(", ","\n").replace("£", "'").replace("$", ", "))

        
welcomeMenu()