from database import init_db, insert_meal, get_all_meals, get_meals_by_date, delete_meal_by_id, update_meal_by_id
from nutrition_api import get_nutrition_from_api

init_db()
print("Choose an action: ")
print("1. Add a new meal")
print("2. View all meals")
print("3. View today`s meals")
print("4. Delete a meal by ID")
print("5. Update meal by ID")

choice = input("Enter your choice: ")

if choice == "1":
    print("Add a new meal: ")
    name = input("Meal name: ")
    nutrition = get_nutrition_from_api(name)
    if nutrition:
        calories = nutrition.get("Calories", 0)
        protein = nutrition.get("Protein", 0)
        fat = nutrition.get("Fat", 0)
        carbs = nutrition.get("Carbohydrates", 0)

        insert_meal(name, calories, protein, fat, carbs)
        print("Meal added successfully!")
    else:
        print("Failed to fetch nutrition info.")

elif choice == "2":
    meals = get_all_meals()

    print("\nAll meals: ")
    for meal in meals:
        print(meal)

elif choice == "3":
    meals = get_meals_by_date()
    if meals:
        print("\nMeals logged today: ")
        for meal in meals:
            print(meal)
    else:
        print("No meals logged today.")
elif choice == "4":
    try:
        meal_id = int(input("Enter the ID of the meal to delete: "))
        delete_meal_by_id(meal_id)
        print(f"Meal with ID {meal_id} deleted.")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
elif choice == "5":
    try:
        meal_id = int(input("Enter the ID of the meal to edit: "))
        name = input("Enter new meal name: ")
        calories = int(input("Enter new calories: "))
        protein = float(input("Enter new protein (g): "))
        fat = float(input("Enter new fat (g): "))
        carbs = float(input("Enter new carbs (g): "))

        update_meal_by_id(meal_id, name, calories, protein, fat, carbs)
        print(f"Meal with ID {meal_id} updated.")
    except ValueError:
        print("Invalid input. Please enter correct data types.")
else:
    print("Invalid choice.")
