class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def teach(self, knowledge):
        self.knowledge.append(knowledge)
        return f"{self.get_full_name()} has taught {knowledge}"

    def get_taught_knowledge(self):
        return self.knowledge

# Example usage:
teacher = Teacher("Zilpah", "Mwaniki")
print(teacher.teach("Chemistry"))
print(teacher.teach("Biology"))

print(f"Teacher: {teacher.get_full_name()}")
print(f"Taught Knowledge: {', '.join(teacher.get_taught_knowledge())}")
