class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
        def __init__(self, firstName, lastname, idNumber, scores):
            super().__init__(firstName, lastName, idNumber)
            self.scores = scores
            
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
        def calculate(self):
            
            scores_sum = 0
            for i in self.scores:
                scores_sum = scores_sum + i
                
            scores_average = scores_sum/len(self.scores)
            
            if scores_average >= 90:
                grade_character = "O"
            elif scores_average >= 80:
                grade_character = "E"
            elif scores_average >= 70:
                grade_character = "A"
            elif scores_average >= 55:
                grade_character = "P"
            elif scores_average >= 40:
                grade_character = "D"
            else:
                grade_character = "T"
            
            return grade_character

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())