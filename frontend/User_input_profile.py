class User:
    def __init__(self, name = "Default User", height = 170, weight = 70, sex = "male", age = 20, active_level = 2, goal_weight = 70):
        self.name = name
        self.height = float(height) 
        self.weight = float(weight)
        self.sex = sex
        self.age = int(age)
        self.active_level = active_level
        self.goal_weight = float(goal_weight)
        self.set_user_DRI()


    def BMI(self):
        height_cm = self.height
        weight_kg = self.weight 
        self.BMI = round(weight_kg / (height_cm/100)**2,2)

    def set_user_DRI(self):
        # Set the user's diatery reference intakes
        self.DRI = {'Carbohydrate': 0, 'Unsaturated fats': 0, 'Vitamin B-6': 1.3,
                    'Trans fats': 2.2,'Saturated fats': 15, 'Total lipid (fat)': 0, 'Calcium, Ca': 1000,
                    'Iron, Fe': 8, 'Protein': 0, 'Energy':  0,'Sugars': 0, 'Sodium, Na': 1500, 'Cholesterol': 300, 
                    'Potassium, K': 3400, 'Fiber': 0, 'Vitamin A': 900,'Vitamin C': 90}
        
        # Calculate User's desired daily calorie intake
        # Calculate Base Metabolism Rate (BMR)
        if self.sex == "Male":
            BMR = round(66.47 + (13.75 * self.weight) + (5.003 * self.height) - (6.755 * self.age), 2)
        elif self.sex == "Female":
            BMR = round(655.1 + (9.563 * self.weight) + (1.850 * self.height) - (4.676 * self.age), 2)

        # Calculate Active Metabolism Rate (AMR)
        AMR_scale = (1.2, 1.375, 1.55, 1.725, 1.9)
        AMR = BMR * AMR_scale[self.active_level]
        self.DRI['Energy'] = round(AMR,2)

        self.set_objective(self.weight, self.goal_weight)


        # Calculate Carbohydrates DRI (45%-65% of calorie intake, 1 gram carb. = 4 KCAL)
        self.DRI['Carbohydrate'] = round(self.DRI['Energy'] * 0.55 / 4, 2)
        
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
        self.DRI['Fiber'] = round(self.DRI['Energy'] * 14 / 1000, 2)

        # Calculate unsaturated fat DRI
        self.DRI['Unsaturated fats'] = round(self.DRI['Total lipid (fat)'] - self.DRI['Saturated fats'] \
                                                            - self.DRI['Trans fats'], 2)
        
        # Calculate sugar DRI
        if self.age >= 18:
            self.DRI['Sugars'] = 100
        else:
            self.DRI['Sugars'] = 80

    def set_objective(self, weight, goal_weight):
        if goal_weight > weight:
            self.objective = "gain"
            self.DRI['Energy'] += 500
        elif goal_weight < weight:
            self.objective = "lose"
            self.DRI['Energy'] -= 500
        else:
            self.objective = "maintain"
            self.DRI['Energy'] = self.DRI['Energy']
    

        

        

