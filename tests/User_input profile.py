import sqlite3

# Setup sqlite db and cursor
connection = sqlite3.connect("food_db.db")
cursor = connection.cursor()

# print(cursor.execute('SELECT count(*) FROM food WHERE data_type IN ("sr_legacy_food", "foundation_food") and description like "Beef%";').fetchall())


class Food:
    def __init__(self, name, food_type, limit):
        self.food_type = food_type

        # Use given food name to locate potential (with a limit) database entries using SQLite
        if self.food_type == "Generic": # If search type is defined as "Generic" foods (Ex: "Chicken")
            food_choices = cursor.execute('SELECT fdc_id, description FROM food WHERE data_type IS ? and description like ? LIMIT ?;', 
                                          ("foundation_food", f"{name}%", limit)).fetchall()
            print(food_choices)
        if self.food_type == "Branded": # If search type is defined as "Branded" foods (Ex: "Sprite")
            food_choices = cursor.execute('SELECT fdc_id, description FROM food WHERE data_type IS ? and description like ? LIMIT ?;', 
                                          ("sr_legacy_food", f"%{name}%", limit)).fetchall()
            print(food_choices)

        # Let User pick one of the entries found and retrive name and food item id (fdc_id) TO BE INTEGRATED WITH FRONTEND LATER
        (self.fdc_id, self.name) = food_choices[int(input("choose 1-10: ")) - 1]
        print(self.name, self.fdc_id)

test1 = Food("Milk", "Generic",  4)
print((test1.fdc_id))
nutrients = cursor.execute('SELECT * from food_nutrient WHERE fdc_id IS "322228" LIMIT 5').fetchall()
print(nutrients)
nutrients = cursor.execute('SELECT nutrient_id FROM food_nutrient WHERE fdc_id IS ?', (str(test1.fdc_id),)).fetchall()
print(nutrients)

class User:
    def __init__(self, name = "", height = 0, weight = 0, gender = "", age = 0, active_level = 0, goal_weight = 0):

        if not self.is_valid_name(name):
            raise ValueError("Invalid name")
        self.name = name
        
        if not self.is_number(height):
            raise ValueError("Invalid input! Please enter a number.")
        self.height = height
        if not self.is_number(weight ):
            raise ValueError("Invalid input! Please enter a number.")
        self.weight = weight
        if not self.is_number(age):
            raise ValueError("Invalid input! Please enter a number.")
        
        if not self.is_valid_age(age): 
            raise ValueError("Invalid input! Please enter a number.")
        self.age = age
        
        self.gender = self.is_gender(gender)

        self.active_level = self.activity_level(active_level)


        self.goal_weight = self.is_valid_goal_weight(weight, goal_weight)

    def BMI(self):
        height_cm = self.height
        weight_kg = self.weight 
        bmi = weight_kg / (height_cm/100)**2
        bmi = round(bmi, 2)

        return bmi
    
    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    def is_valid_name(self, name):
        if name.isalpha():
            return True
        else:
            raise ValueError("Invalid name")
        

    def is_valid_goal_weight(self, weight, goal_weight):
        if not self.is_number(goal_weight):
            raise ValueError("Invalid input! Please enter a number.")

        

        goal_weight = float(goal_weight)

        if  abs(goal_weight - weight) > 1:
            if weight > goal_weight:
                return "You wish to lose weight!"
            elif weight < goal_weight:
                return "You wish to gain weight!"
            else:
                return "You want to maintain your weight!"

        return goal_weight

    def is_gender(self, gender):
        if gender.isalpha():
            if gender == "male":
                return "male"
            elif gender == "female":
                return "female"
            else:
                return "other"
    def is_valid_age(self, age):
        if not self.is_number(age):
            raise ValueError("Invalid input! Please enter a number.")
        if 0 <= age <= 130:
            return age
        
    def activity_level(self, active_level):
        if not self.is_number(active_level):
            raise ValueError("Invalid input! Please enter a number.")
        if not (0 <= round(float(active_level), 3) <= 5):
            raise ValueError("Invalid input! Outside the range of 0 to 5")
        return round(float(active_level), 3)





class Calorie_calculator:
    def __init__(self, food_name, quantity):
        self.food_name = food_name


        