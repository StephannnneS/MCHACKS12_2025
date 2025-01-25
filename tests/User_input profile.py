

class User:
    def __init__(self, name, height, weight, age, gender, activity_level, goal, diet, goal_weight):
    
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.goal = goal
        self.diet = diet
        self.goal_weight = goal_weight

    def BMI(self):
        height_cm = self.height
        weight_kg = self.weight 
        bmi = weight_kg / (height_cm/100)**2

        return bmi
    
    
