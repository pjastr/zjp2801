class Person:

    age = 49
    hair = "brown"
    eyes = "blue"
    weight = 98
    height = 183

    def get_bmi(self):
        return self.weight / (self.height * self.height)

    def get_eye_col(self):
        return f"masz kolor oczu {self.eyes}"


agata = Person()
print(agata.age)
print(agata.get_bmi())
print(agata.get_eye_col())
print(agata.eyes)
