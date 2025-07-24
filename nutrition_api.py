import requests
from dotenv import load_dotenv
import os

def get_nutrition_from_api(meal_name):
   load_dotenv()
   API_KEY = os.getenv("SPOONACULAR_API_KEY")
   url = "https://api.spoonacular.com/recipes/guessNutrition"

   params = {
   "title": meal_name,
   "apiKey": API_KEY
   }

   try:
     response = requests.get(url, params=params)
     print("API Status:", response.status_code)

     if response.status_code == 200:
       data = response.json()
       print("\nNutrition Info:")
       print(f"  Calories: {data['calories']['value']} kcal")
       print(f"  Fat:      {data['fat']['value']} g")
       print(f"  Carbs:    {data['carbs']['value']} g")
       print(f"  Protein:  {data['protein']['value']} g\n")
       return {
            "Calories": data["calories"]["value"],
            "Protein": data["protein"]["value"],
            "Fat": data["fat"]["value"],
            "Carbohydrates": data["carbs"]["value"]
       }
     else:
         print("API Error:", response.status_code)
         print("Response text:", response.text)
         return None

   except Exception as e:
     print("Exception occurred:", e)
     return None