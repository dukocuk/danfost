from typing import List, Dict, Set

class Employee:
    
    def __init__(self) -> None:
        self.employees: Dict[str, Set[str]] = {
            "A": {"a", "b", "c", "d", "e", "f", "g", "h"},
            "B": {"d", "e", "f", "g", "h", "i", "j", "k"},
            "C": {"g", "h", "i", "j", "k", "l", "m", "n"},
            "D": {"k", "l", "m", "n", "o", "p", "q", "r"},
            "E": {"n", "o", "p", "q", "r", "s", "t", "u"},
            "F": {"a", "b", "c", "r", "s", "t", "u", "v", "w", "x", "y", "z"},
            "G": {"a", "e", "i", "o", "u", "y"},
            "H": {"b", "c", "e", "g", "k", "m", "q", "s", "x"},
            }
    

    def getEmployees(self) -> Dict[str, Set[str]]:
            return self.employees


