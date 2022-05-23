import sys
import json
import random
import os
import colorama

listEmployees = []
listSentence = []

def randomColorStr():
    return "\033[1;" + str(random.randint(31, 37)) + "m"

def clearCmd():
    clear = lambda: os.system('cls')
    clear()

def readJson():
    with open('Data.json') as fJson:
        data = json.load(fJson)
        global listEmployees, listSentence
        listEmployees = data['employees']
        listSentence = data['sentences']

def callEverybody():
    clearCmd()

    readJson()

    random.shuffle(listEmployees)
    for employee in listEmployees:
        print(randomColorStr() + employee + random.choice(listSentence))
        input()

    print(randomColorStr() + "Everyone talked, morning meeting is finished !")
    input("\033[1;37m")

def showListOfEmployees():
    readJson()
    for employee in listEmployees:
        print(employee)

def addOrDeleteSomeone():
    readJson()
    clearCmd()
    print("===========================================")
    showListOfEmployees()
    print("\nTape the name that you want to add or remove from the list of employees")
    print("***if it's in the list, it will be add else it will be deleted")
    print("***Press entry to exit without doing anything\n")

    userInput = input()

    if userInput == "":
        return

    data = {
        "employees" : listEmployees,
        "sentences" : listSentence
    }
    
    if userInput in data['employees']:
        data['employees'].remove(userInput)
        print(userInput + " has been removed !")
    else:
        data['employees'].append(userInput)
        print(userInput + " has been added !")

    with open('Data.json', 'w') as fJson:
        json.dump(data, fJson, sort_keys=True, indent=4)
    input()

def homePage():
    clearCmd()
    print("===========================================")
    print("Enter : Start to call everyone.")
    print("1 : See the list of employees")
    print("2 : Add or delete someone from the list")
    print("3 : To exit")
    return input()


def main() -> int:
    clearCmd()
    userInput = homePage()
    while(True):
        if userInput == "":
            callEverybody()
            break

        elif userInput == "1":
            print()
            showListOfEmployees()
            input("\nPress Enter")
            clearCmd()
            userInput = homePage()

        elif userInput == "2":
            addOrDeleteSomeone()
            clearCmd()
            userInput = homePage()

        elif userInput == "3":
            break

        else:
            print("Invalid input")
            userInput = input()
    return 0

    

if __name__ == '__main__':
    sys.exit(main())