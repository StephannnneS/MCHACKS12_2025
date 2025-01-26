class User:
    def __init__(self, name = "Default User", height = 170, weight = 70, sex = "male", age = 20, active_level = 2, goal_weight = 70):
        self.name = name
        self.height = height
        self.weight = weight
        self.sex = sex
        self.age = age
        self.active_level = active_level
        self.goal_weight = goal_weight
        self.set_user_DRI()


    def BMI(self):
        height_cm = self.height
        weight_kg = self.weight 
        self.BMI = round(weight_kg / (height_cm/100)**2,2)

    def set_user_DRI(self):
        # Set the user's diatery reference intakes
        self.DRI = {'Energy':  0, 'Carbohydrate, by difference': 0, 'Sugars, Total': 0, 'Fiber, total dietary': 0, 'Total lipid (fat)': 0, 
                    'Fatty acids, total trans': 2.2, 'Fatty acids, total saturated': 15, 'Fatty acids, total monounsaturated': 0,
                    'Protein': 0,  'Sodium, Na': 1500, 'Cholesterol': 300, 'Calcium, Ca': 1000, 'Iron, Fe': 8, 'Potassium, K': 3400, 
                    'Vitamin A': 900, 'Vitamin B-6': 1.3, 'Vitamin C, total ascorbic acid': 90}
        
        # Calculate User's desired daily calorie intake
        # Calculate Base Metabolism Rate (BMR)
        if self.sex == "male":
            BMR = round(66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age), 2)
        elif self.sex == "female":
            BMR = round(655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age), 2)

        # Calculate Active Metabolism Rate (AMR)
        AMR_scale = (1.2, 1.375, 1.55, 1.725, 1.9)
        AMR = BMR * AMR_scale[self.active_level]
        self.DRI['Energy'] = AMR

        # Calculate Carbohydrates DRI (45%-65% of calorie intake, 1 gram carb. = 4 KCAL)
        self.DRI['Carbohydrate, by difference'] = round(self.DRI['Energy'] * 0.55 / 4, 2)
        
        # Calculate Protein DRI (Adult: 10%-35% of calorie intake, Child: 10%-30% of calorie intake, 1 gram protein = 4 KCAL)
        if self.age >= 18:
            self.DRI['Protein'] = round(self.DRI['Energy'] * 0.225 / 4, 2)
        else:
            self.DRI['Protein'] = round(self.DRI['Energy'] * 0.2 / 4, 2)

        # Calculate Lipid DRI (Adult: 20%-35% of calorie intake, Child: 25%-35% of calorie intake, 1 gram lipid = 9 KCAL)
        if self.age >= 18:
            self.DRI['Total lipid (fat)'] = round(self.DRI['Energy'] * 0.275 / 4, 2)
        else:
            self.DRI['Total lipid (fat)'] = round(self.DRI['Energy'] * 0.3 / 4, 2)

        # Calculate Fiber DRI (14 gram per 1000 KCAL)
        self.DRI['Fiber, total dietary'] = round(self.DRI['Energy'] * 14 / 1000, 2)

        # Calculate unsaturated fat DRI
        self.DRI['Fatty acids, total monounsaturated'] = round(self.DRI['Total lipid (fat)'] - self.DRI['Fatty acids, total saturated'] \
                                                            - self.DRI['Fatty acids, total trans'], 2)
        
        # Calculate sugar DRI
        if self.age >= 18:
            self.DRI['Sugars, Total'] = 100
        else:
            self.DRI['Sugars, Total'] = 80
   
user1 = User(weight=1000)
print(user1.DRI)