class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, information):
        self.knowledge.append(information)

    def get_knowledge(self):
        return self.knowledge

# Example usage:
student = Student("Stephan", "Maina")
student.learn("Mathematics")
student.learn("History")

print(f"Student: {student.get_full_name()}")
print(f"Knowledge: {', '.join(student.get_knowledge())}")
