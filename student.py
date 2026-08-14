class Student:

    def __init__(self, student_id, name, grades):
        self.id = student_id
        self.name = name
        self.grades = grades
        self.average = self.calculate_average()

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "grades": self.grades,
            "average": self.average
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["grades"]
        )