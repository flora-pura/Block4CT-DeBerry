"""

Program Goals:
1. Get input from the user (at multiple points)
2. We need to convert some of this input to INTs from StRs
3. We need to provide choices to the user
    a. Add more values to the list
    b. Return a value a speciftic index

"""

def mainProgram():
    myList = []
    print("Hello, there! Lets work with lists!")
    print("Choose from the following options. Type a number below!")
    choice = input("1. Add to list , 2. Return the value at index position!  ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValue()
    #TO ADD: 1. a way to loop the action, 2. a way to quit, 3. think of repetition

def addToList():
    print("Adding to list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def indexValues():

if __name__ == "__main__":
    mainProgram()
