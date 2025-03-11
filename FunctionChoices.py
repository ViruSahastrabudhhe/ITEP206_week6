class InputFunctions:
    
    def isOddOrEven(self, userInput: str):
        numInput=0
        try:
            numInput = int(userInput)
        except ValueError:
            print("Input must be a number!")
            return

        if numInput==0:
            print(f"{numInput} is zero!")
        elif numInput%2==0:
            print(f"{numInput} is an even number!")
        else:
            print(f"{numInput} is an odd number!")

    def isVowelOrConsonant(self, userInput: str):
        if len(userInput)>1:
            print("Input must only be a single character!")
            return

        vowels='aeiouAEIOU'

        if not userInput.isalpha():
            print("Input must be a letter!")
            return

        if userInput in vowels:
            print(f"{userInput} is a vowel!")
        else:
            print(f"{userInput} is a consonant!")

    def isSpecialCharacter(self, userInput: str):
        if len(userInput)>1:
            print("Input must only be a single character!")
            return

        if userInput.isalnum() or userInput==' ':
            print(f"{userInput} is not a special character!")
            return

        print(f"{userInput} is a special character!")

    def allInOne(self, userInput: str):
        vowels='aeiouAEIOU'

        for char in userInput:
            if char.isalpha():
                if char in vowels:
                    print(f"{char} is a vowel!")
                else:
                    print(f"{char} is a consonant!")
            else:
                try:
                    if int(char)==0:
                        print(f"{char} is zero!")
                    elif int(char)%2==0:
                        print(f"{char} is an even number!")
                    else:
                        print(f"{char} is an odd number!")
                except:
                    if char==' ':
                        print(f"{char} is a space!")
                    else:
                        print(f"{char} is a special character!")
