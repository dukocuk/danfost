from typing import List
from group import Group
from user_input import UserInput

def main():
    skills_needed : List[str]  = UserInput().getUserInput()
    group: Group = Group(skills_needed)
    minimal_groups = group.findMinimalGroups()
    group.printMinimalGroups(minimal_groups)

if __name__ == "__main__":
    main()

