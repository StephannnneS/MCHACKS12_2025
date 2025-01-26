import sqlite3
import User_input_profile

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



    
class Meal: 
    def __init__(self, Moment_of_meal, date = 0 ):

        """
        Initialize a Meal object with the given moment of meal and optional date.

        Parameters
        ----------
        Moment_of_meal : str
            The moment of the meal, e.g. breakfast, lunch, or dinner.
        date : int
            An optional date for the meal, defaults to 0.

        Attributes
        ----------
        Moment_of_meal : str
            The moment of the meal, e.g. breakfast, lunch, or dinner.
        foods : list
            A list of Food objects that are part of the meal.
        """
        self.Moment_of_meal = Moment_of_meal
        self.foods = []
        self.date = date
    

    def add_food(self, food_name,food_type, quantity):
        
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

        self.foods.append([Food(food_name, food_type), quantity])

    def remove_food(self, food_name):
        """
        Remove a food from the meal.

        Parameters
        ----------
        food_name : str
            The name of the food to be removed.

        Returns
        -------
        None
        """
        for food in self.foods:
            if food[0].name == food_name:
                self.foods.remove(food)


    def nutrients_counter(self):
        self.nutrients = {'Carbohydrate, by difference': 0, 'Fatty acids, total monounsaturated': 0, 'Vitamin B-6': 0,
                    'Fatty acids, total trans': 0,'Fatty acids, total saturated': 0, 'Total lipid (fat)': 0, 'Calcium, Ca': 0,
                    'Iron, Fe': 0, 'Protein': 0, 'Energy':  0,'Sugars, Total': 0, 'Sodium, Na': 0, 'Cholesterol': 0, 
                    'Potassium, K': 0, 'Fiber, total dietary': 0, 'Vitamin A': 0,'Vitamin C, total ascorbic acid': 0}

        for food_item, quantity in self.foods:
            for nutrient_name in food_item.nutrients:
                self.nutrients[nutrient_name] += round(float(food_item.nutrients[nutrient_name][0]) * quantity / 100, 2)



        


    

