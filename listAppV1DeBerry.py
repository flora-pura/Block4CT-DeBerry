"""

Program Goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTs from StRs
3. We need to provide choices to the user
    a. Add more values to the list
    b. Return a value a speciftic index

"""
myList = []

def mainProgram():
    #build a while loop here!
    while True:
        try: 
            print("Hello, there! Lets work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to list ,
2. Return the value at an index,
3. Random search,
4. Exit program.  """)
            if choice == "1":
                addToList()
            elif choice == "2":
                indexValue()
            elif choice == "3":
                break
        except:
                print("You made a whoopsie!")

    #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition

def addToList():
    print("Adding to list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def indexValues():
    print("Ohhh! I heard you a particular piece of data!")
    indexPos = input("What index position are you curious about?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("RaNDoM SeaRCH!")
    print(myList [random.randint(0, len (myList)-1)])

#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
    mainProgram()
