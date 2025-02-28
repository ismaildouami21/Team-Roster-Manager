MAX_MENU_CHOICE = 7
MAX_JERSEY_NUM = 99
MAX_RATING = 10
INPUT_FILENAME = 'roster.txt'
OUTPUT_FILENAME = 'update.txt'

def getRoster(fileName):
    '''
    Reads a file where each line of the file is a jersey number (int) and player rating (int)
    
    Params:
    fileName (str): the name of the file with info for the roster
    
    Returns:
    dictionary mapping jersey number to player rating
    '''
    rosterDict = {}
    try:
        with open(fileName, 'r') as f_in:
            for line in f_in:
                dataList = line.split()
                jerseyNum = int(dataList[0].strip())
                playerRating = int(dataList[1].strip())
                rosterDict[jerseyNum] = playerRating
    except FileNotFoundError:
        print(f"File {fileName} not found. Starting with an empty roster.")
    return rosterDict        

def saveRoster(rosterDict, fileName):
    '''
    Saves roster data to a file with jersey number and rating one pair each line separated by a space
    
    Params:
    rosterDict (dict): a dictionary mapping jersey numbers to ratings
    fileName (str): the name of the file to save data to
    '''
    with open(fileName, 'w') as f_out:
        for jerseyNum, rating in rosterDict.items():
            f_out.write(f'{jerseyNum} {rating}\n')

def getInt(prompt, lowNum, highNum):
    '''
    gets valid integer from user which must be lowNum to highNum inclusive

    Returns:
    valid entered integer
    '''
    while True:
        number = input(prompt)
        if number.isdigit() and lowNum <= int(number) <= highNum:
            return int(number)
        print('Invalid. Try again.')

def addPlayer(rosterDict):
    '''
    Prompts user to enter a jersey number and, if not already on the roster, a rating.
    If already on the roster, outputs "Cannot add player. Already on roster."
    '''
    jerseyNum = getInt('Enter jersey number to add: ', 1, MAX_JERSEY_NUM)
    if jerseyNum not in rosterDict:
        rating = getInt('Enter rating: ', 1, MAX_RATING)
        rosterDict[jerseyNum] = rating
        print('Added player', jerseyNum, 'with rating', rating, 'to roster.')
    else:
        print('Cannot add player. Already on roster.')

def removePlayer(rosterDict):
    '''
    Prompts user to enter a jersey number and removes player from the roster.
    If player not in roster, outputs "Player not on roster. Cannot remove."
    '''
    jerseyNum = getInt('Enter jersey number to remove: ', 1, MAX_JERSEY_NUM)
    if jerseyNum in rosterDict:
        del rosterDict[jerseyNum]
        print('Removed player', jerseyNum, 'from roster.')
    else:
        print('Player not on roster. Cannot remove.')

def updatePlayerRating(rosterDict):
    '''
    Prompts the user to enter a jersey number and rating.
    Updates the rating if the player is on the roster, otherwise outputs "Player not on roster. Cannot update."
    '''
    jerseyNum = getInt('Enter jersey number to update: ', 1, MAX_JERSEY_NUM)
    if jerseyNum in rosterDict:
        rating = getInt('Enter new rating: ', 1, MAX_RATING)
        rosterDict[jerseyNum] = rating
        print(f'Updated player {jerseyNum} to rating {rating}.')
    else:
        print('Player not on roster. Cannot update.')

def outputTopRated(rosterDict):
    '''
    Outputs the jersey numbers of the players with the highest rating.
    '''
    if rosterDict:
        max_rating = max(rosterDict.values())
        top_players = sorted(jerseyNum for jerseyNum, rating in rosterDict.items() if rating == max_rating)
        print(f'Players with highest rating of {max_rating}:')
        for player in top_players:
            print(player)
    else:
        print('No players in roster.')

def cutRoster(rosterDict):
    '''
    Prompts the user to enter a rating and removes all players with a rating lower than the entered rating.
    '''
    print('All players rated lower than the entered rating will be cut from the roster.')
    rating = getInt('Enter rating: ', 1, MAX_RATING)
    players_to_cut = [jerseyNum for jerseyNum, playerRating in rosterDict.items() if playerRating < rating]
    
    if players_to_cut:
        print('Players cut from roster:')
        for jerseyNum in players_to_cut:
            print(jerseyNum)
            del rosterDict[jerseyNum]
    else:
        print('No players were cut.')

def outputRoster(rosterDict):
    '''
    Outputs the jersey number and rating of each player on the roster in ascending jersey number order.
    '''
    if rosterDict:
        print('Number Rating')
        for jerseyNum in sorted(rosterDict):
            print(f'{jerseyNum:4} {rosterDict[jerseyNum]:6}')
    else:
        print('No players in roster.')

def printMenu():
    ''' Prints menu of choices '''
    print('Choose from the following options:')
    print('1  Add player')
    print('2  Remove player')
    print('3  Update player rating')
    print('4  Output top rated player')
    print('5  Cut roster')
    print('6  Output roster')
    print('7  Quit')
    print()

def main():
    rosterDict = getRoster(INPUT_FILENAME)     
    print('Team Roster Manager')
    print()
    printMenu()
    choice = getInt('Enter choice: ', 1, MAX_MENU_CHOICE)
    while choice != MAX_MENU_CHOICE:
        if choice == 1:
            addPlayer(rosterDict)
        elif choice == 2:
            removePlayer(rosterDict)
        elif choice == 3:
            updatePlayerRating(rosterDict)           
        elif choice == 4:
            outputTopRated(rosterDict)
        elif choice == 5:
            cutRoster(rosterDict)
        elif choice == 6:
            outputRoster(rosterDict)
        print()
        printMenu()
        choice = getInt('Enter choice: ', 1, MAX_MENU_CHOICE)
    
    saveRoster(rosterDict, OUTPUT_FILENAME)
    print('Roster saved. Goodbye!')

if __name__ == '__main__':
    main()
