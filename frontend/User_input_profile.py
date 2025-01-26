import sqlite3

# Setup sqlite db and cursor
connection = sqlite3.connect("food_db.db")
cursor = connection.cursor()

# print(cursor.execute('SELECT count(*) FROM food WHERE data_type IN ("sr_legacy_food", "foundation_food") and description like "Beef%";').fetchall())

ESSENTIAL_NUTRIENT_IDS = ("1008", "1005", "1063", "1079", "1093", "1003", "1253", "1004", 
                              "1257", "1292", "1258", "1087", "1092", "1089", "2067", "1162", "1175")

class Food:
    #Constants
    ESSENTIAL_NUTRIENT_IDS = ("1008", "1005", "1063", "1079", "1093", "1003", "1253", "1004", 
                              "1257", "1292", "1258", "1087", "1092", "1089", "2067", "1162", "1175")
    
    def __init__(self, name, food_type):
        """
        Initialize a Food object with the given name and food type, and use the name to locate 
        potential database entries using SQLite.

        Parameters
        ----------
        name : str
            The name of the food to search for.
        food_type : str
            The type of food to search for, either "Generic" or "Branded".

        Attributes
        ----------
        food_type : str
            The type of food to search for, either "Generic" or "Branded".
        food_choices : list
            A list of tuples, where each tuple contains the fdc_id and description of a potential 
            database entry that matches the given name and food type. The list is limited to a maximum 
            of 8 entries.

        Notes
        -----
        The SQLite query is constructed based on the given food type. If the food type is "Generic", 
        the query searches for descriptions that start with the given name. If the food type is "Branded", 
        the query searches for descriptions that contain the given name anywhere in the string. The 
        query is limited to a maximum of 8 entries.
        """
        LIMIT = 8
        self.food_type = food_type

        # Use given food name to locate potential (with a limit) database entries using SQLite
        if self.food_type == "Generic": # If search type is defined as "Generic" foods (Ex: "Chicken")
            self.food_choices = cursor.execute('SELECT fdc_id, description FROM food WHERE data_type IS ? and description like ? LIMIT ?;', 
                                          ("foundation_food", f"{name}%", LIMIT)).fetchall()
        if self.food_type == "Branded": # If search type is defined as "Branded" foods (Ex: "Sprite")
            self.food_choices = cursor.execute('SELECT fdc_id, description FROM food WHERE data_type IS ? and description like ? LIMIT ?;', 
                                          ("sr_legacy_food", f"%{name}%", LIMIT)).fetchall()
            
    def get_nutrient_info(self, food_choice_info):
        """
        Retrieve nutrient information for a selected food choice and store it in the instance.

        Parameters
        ----------
        food_choice_info : tuple
            A tuple containing the fdc_id and name of the selected food choice.

        Attributes
        ----------
        nutrients : dict
            A dictionary where the keys are nutrient names and the values are tuples containing
            the amount and the unit name of the nutrient.

        Notes
        -----
        Only nutrients whose IDs are in the ESSENTIAL_NUTRIENT_IDS list will be included.
        Nutrient information is obtained from the database using the fdc_id of the selected food.
        """

        self.nutrients = {}
        self.fdc_id = food_choice_info[0]
        self.name = food_choice_info[1]
        for nutrient in cursor.execute('SELECT nutrient_id, amount FROM food_nutrient WHERE fdc_id IS ?', (str(self.fdc_id),)).fetchall():
                if nutrient[0] in ESSENTIAL_NUTRIENT_IDS:
                    nutrient_info = cursor.execute('SELECT name, unit_Name FROM nutrient WHERE id IS ?', (nutrient[0],)).fetchall()
                    self.nutrients[nutrient_info[0][0]] = (nutrient[1], nutrient_info[0][1])

class User:
    def __init__(self, name = "", height = 0, weight = 0, sex = "", age = 0, active_level = 0, goal_weight = 0):

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
        
        self.sex = self.is_sex(sex)

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

    def is_sex(self, sex):
        if sex.isalpha():
            if sex == "male":
                return "male"
            elif sex == "female":
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
        pass


class Meal: 
    def _init__(self, Moment_of_meal, date = 0 ):

        Moment_of_meal = self.Moment_of_meal
        self.foods = []
    

    def add_food(self, food_name, quantity):
        
        """
        Add a food to the meal.

        Parameters
        ----------
        food_name : str
            The name of the food to be added.
        quantity : int
            The quantity of the food to be added.

        Returns
        -------
        None
        """
        
        self.foods.append(Food(food_name, quantity))
        
        


   