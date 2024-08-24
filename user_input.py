import sys
from typing import List

class UserInput:
    
    def __init__(self) -> None:
        self.userInput: str = ""
        self.skills: List[str] = []
    
    def getUserInput(self) -> List[str]:
            self.userInput = input("Please enter character separated by spaces: ")
            if " " not in self.userInput and len(self.userInput) !=1:
                print("Error: You did not enter spaces between characters. Exiting program.")
                sys.exit(1)
            self.skills = self.userInput.split()
            return self.skills

        