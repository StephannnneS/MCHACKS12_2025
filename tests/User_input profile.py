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
    
    def is_number():
        try:
            float(input)
            return True
        except ValueError:
            return False
        
    def is_valid_name():
        name = input("Enter your name: ")
        if name.isalpha():
            return True
        else:
            return False
