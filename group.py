from itertools import combinations
from typing import List, Set, Dict
from employee import Employee

class Group:

    employees: Dict[str, Set[str]] = None
    projectSkills: Set[str] =  None
    
    def __init__(self, projectSkills:List[str]) -> None:
        self.employees = Employee().getEmployees()  
        self.projectSkills = set(projectSkills)

    def _generateValidGroups(self) -> List[List[str]]:
        valid_groups = []
        # Generate all possible combinations of employees
        for r in range(1, len(self.employees) + 1):
            for combination in combinations(self.employees.keys(), r):
                combined_skills = set()
                for employee in combination:
                    combined_skills.update(self.employees[employee])
                # Check if this combination covers all required skills
                if self.projectSkills.issubset(combined_skills):
                    valid_groups.append(list(combination))
        return valid_groups

    def _filterMinimalGroups(self, valid_groups: List[List[str]]) -> List[List[str]]:
        minimal_groups = []
        for group in valid_groups:
            is_minimal = True
            # Check if a smaller subset of this group can cover all required skills
            for smaller_group in combinations(group, len(group) - 1):
                combined_skills = set()
                for employee in smaller_group:
                    combined_skills.update(self.employees[employee])
                if self.projectSkills.issubset(combined_skills):
                    is_minimal = False
                    break
            if is_minimal:
                minimal_groups.append(group)
        return minimal_groups    
        
    def findMinimalGroups(self) -> List[List[str]]:
        valid_groups = self._generateValidGroups()
        min_groups = self._filterMinimalGroups(valid_groups)
        return min_groups
                
        
    def printMinimalGroups(self, min_groups:List[str]) -> None :
        print("OUTPUT:")
        for group in min_groups:
            print(" ".join(group))
