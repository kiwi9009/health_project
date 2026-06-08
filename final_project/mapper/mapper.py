from domains.models.food_model import Food


class FoodMapper:

    @staticmethod
    def from_usda(item):
      
        calories = 0
        protein = 0
        carbs = 0
        fiber = 0
        fat = 0
        
        for nutrient in item.get('foodNutrients',''):
            name = nutrient.get('nutrientName','')
            value = nutrient.get('value',0)
            
            if name =='Energy':
                calories = value
            elif name =='Protein':
                protein = value
            elif name =='Total lipid (fat)':
                fat = value
            elif name =='Carbohydrate, by difference':
                carbs = value
            elif name =='Fiber, total dietary':
                fiber = value
             
            
        return Food(
            id = item['fdcId'],
            name = item['description'],
            calories = calories,
            protein = protein,
            fat = fat,
            carbs = carbs,
            fiber = fiber
        )
    