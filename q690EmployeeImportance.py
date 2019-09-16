# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        queue = []
        for emp in employees:
            if emp.id == id:
                queue.append(emp)
        
        importance = 0
        while len(queue) != 0:
            e = queue.pop(0)
            importance += e.importance
            for sub in e.subordinates:
                for emp in employees:
                    if sub == emp.id:
                        queue.append(emp)
        
        return importance
