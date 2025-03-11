from FunctionChoices import InputFunctions

class TextInterface:
    def __init__(self):
        self.InputFunctions = InputFunctions()
        self.quit = 'quit'

    def start(self):
        while True:
            print("Program functions:")
            print("1 - Odd or even")
            print("2 - Vowel or consonant")
            print("3 - Is special character")
            print("4 - All in one")
            print("Stop - Exit program")
            userInput=input("\nInput: ")

            if userInput=="stop" or userInput=="STOP":
                break

            self.programOptions(userInput)

    def programOptions(self, userInput):
        try:
            newInput = int(userInput)
        except ValueError:
            print("Invalid input!\n")
            return

        if newInput==1:
            self.programOne()
        elif newInput==2:
            self.programTwo()
        elif newInput==3:
            self.programThree()
        elif newInput==4:
            self.programFour()
        else:
            print("Invalid input!\n")

    def programOne(self):
        while True:
            userInput = input("\nInput (input 'quit' to return to main menu): ")
            if userInput.lower() in self.quit:
                break
            self.InputFunctions.isOddOrEven(userInput)
        print()

    def programTwo(self):
        while True:
            userInput = input("\nInput (input 'quit' to return to main menu): ")
            if userInput.lower() in self.quit:
                break
            self.InputFunctions.isVowelOrConsonant(userInput)
        print()

    def programThree(self):
        while True:
            userInput = input("\nInput (input 'quit' to return to main menu): ")
            if userInput.lower() in self.quit:
                break
            self.InputFunctions.isSpecialCharacter(userInput)
        print()

    def programFour(self):
        while True:
            userInput = input("\nInput (input 'quit' to return to main menu): ")
            if userInput.lower() in self.quit:
                break
            self.InputFunctions.allInOne(userInput)
        print()