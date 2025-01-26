# MCHACKS12_2025

NOTE: To run the application in its current state from a github repository clone, the sqlite3 database must be downloaded separately. Currently, it can be found here: https://drive.google.com/file/d/1kMPsr0lEPwkSUyMaPHKJWjK0_DbCnLIh/view?usp=sharing

### Inspiration  
Our desire to live healthier lifestyles and track our fitness journeys inspired us to create a user-friendly application that simplifies nutrition tracking and helps users meet their health goals.

### What it Does  
Our app allows users to log the food items they consume throughout the day and provides detailed nutritional information, including macronutrients and micronutrients. Users can search for food items either by type (e.g., chicken) or brand (e.g., Sprite). Additionally, the app calculates personalized daily allowances for calories and nutrients based on the user’s health goals, guiding them toward healthier eating habits.

### How We Built It  
The app was developed using Python and leverages SQLite3 to create a local database that stores comprehensive nutritional information for various food items. By hosting the database locally, the app can function offline, making it highly accessible. The backend was implemented to process user inputs, calculate nutritional values, and update records efficiently. For the frontend, we utilized the Kivy Python library to build an intuitive and responsive user interface. Kivy’s cross-platform capabilities allowed us to design a modern, touch-friendly UI that ensures a smooth and engaging user experience.

### Challenges We Ran Into  
Integrating SQLite3 to efficiently search and retrieve food item information presented a steep learning curve, particularly in optimizing queries to handle large datasets. Additionally, working with Kivy posed challenges in designing a clean and user-friendly UI due to its unique syntax and layout management system, which required additional time to learn and implement effectively. Ensuring the frontend seamlessly integrated with the backend while maintaining performance and responsiveness also proved challenging.

### Accomplishments That We’re Proud Of  
We successfully built a functional app that provides users with an easy way to track their dietary intake and meet their health goals. One of our key achievements was enabling offline functionality by hosting the database locally. We are also proud of our progress with Kivy, as we overcame its initial learning curve to create an intuitive interface with interactive elements. The app's smooth integration of frontend and backend components highlights our team's ability to deliver a cohesive product.

### What We Learned  
We gained valuable experience in building and managing SQLite3 databases, optimizing database queries, and integrating backend logic with a responsive frontend. Through working with Kivy, we learned how to design and implement cross-platform UIs, overcoming layout challenges and fine-tuning the app's responsiveness and aesthetics. The project also taught us the importance of balancing functionality with user experience in app development.

### What’s Next for the Health Care App  
Future improvements include adding a calendar feature to track previous daily entries and providing a section for users to manage dietary restrictions. We also aim to implement recommendation features, offering tailored dietary advice and exercise suggestions based on users’ health profiles. Furthermore, we plan to enhance the UI using Kivy’s advanced features to make the app more visually appealing and user-friendly. Ultimately, our vision is for the Health Care App to become a comprehensive health companion, supporting users in achieving their diet and fitness goals.