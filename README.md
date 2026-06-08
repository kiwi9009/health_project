# CS50 FINAL_PROJECT
### Video Demo: https://www.youtube.com/watch?v=Kyukdn2Is_k

### Description:
# HEATH APP
    This project aims to assess health status and promote a balanced diet.
    The project has basically completed 2 features:
    # Feature 1: BMI Calculation
    → Assesses the user's weight status and calculates their total daily calorie needs.
    → Future goal: Integrate with a Food API database to recommend personalized meal plans that support weight loss, weight gain, or weight maintenance.
    # Feature 2: Search and retrieve data from the USDA database to collect detailed nutritional information for each food item. This feature supports users in creating and maintaining a balanced diet

# Future Expansion / Scalability:
    The project has strong potential for expansion, aiming to advance toward health prediction based on the user’s diet and current health condition.
    Key future developments include:
    → Collecting additional data such as atrial fibrillation (AFib) levels and daily salt intake.
    → Providing health risk assessments, specifically the risks of stroke, cerebral stroke, and heart attack.
    → Integrating with Apple Watch to collect real-time health data and support these advanced features.

# Design Philosophy:
    Due to my personal intention and personality, I believe the project should have clear separation of concerns. Therefore, I will place all functional functions in their appropriate locations and will not group them together in main.py.

# Software Structure:
    # Folder structure

    final_project/
    |
    |---presentation/                   # This layer is where users interact with the application.
    |   |                                 It is responsible for displaying information and collecting input from the user.
    |   |
    |   |---display.py                      + The component where users can view information.
    |   |---input_handle.py                 + The component where users enter data.
    |   |---menu.py                         + This component is designed to create and display menus for user selection.
    |
    |
    |---controller/                     # Controller folder is responsible for handling and processing requests from the
    |   |                                   presentation layer (user interface).
    |   |---food_controller.py              + Handles food search and USDA nutritional data requests.
    |   |---user_controller.py              + Handles health calculation requests (BMI, calorie needs, etc.).
    |
    |---domains/                        # This is the core of the software.
    |   |                                   where the rules and validation logic for data objects are defined.
    |   |---contants/                   - This module contains fixed values (constants) that are used in many places throughout the system.
    |   |    |---region.py                  + World regions contant
    |   |
    |   |---exceptions/                 - This folder/module contains custom exceptions(user-defined exception classes)
    |   |    |                            declared for the project.
    |   |    |---food_exception.py          + Custom exception related to food
    |   |
    |   |---models/                     # Responsible for describing and defining the structure of the data (data models).
    |        |---food_model.py              + Describes the data structures transmitted between layers related to food
    |        |---user_model.py              + Describes the data structures transmitted between layers related to user metrics
    |
    |---services/                       # This layer contains business logic and data processing operations.
    |   |                              It is designed to be reused by many other components in the system.
    |   |---food_service.py            + Handles business logic related to food
    |   |---uer_service.py             + Handles business logic related to users
    |
    |
    |---repository/                     # This layer is responsible for data retrieval and data access operations
    |   |---food_repository.py          + Responsible for accessing and retrieving food-related data
    |   |---user_repository.py          + Responsible for accessing and managing user-related data
    |
    |---usda/
    |   |---usda_client.py              # We would like to express our sincere thanks to the USDA
    |                                      for providing highly detailed and valuable public nutritional data.
    |
    |---shared/                         # This module/folder contains shared resources used commonly across the entire system
    |   |                             (common utilities, helper functions, base classes, configurations, etc.).
    |   |---helper/
    |            |---utils.py
    |---mapper/                         # This module is responsible for converting and transforming data between different layers or formats
        |                              (e.g., from Domain models to DTOs, API responses to internal objects, etc.).
        |---mapper.py

