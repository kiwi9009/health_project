from dataclasses import dataclass


@dataclass
class FoodItems:
            foodname:str
            value:float
            unit:str
                       
@dataclass
class Nutrient:
        food : FoodItems
        nutrient:str


@dataclass
class Food:
        id:int
        name:str
        calories:float=0
        protein:float=0
        fat:float=0
        carbs:float=0
        fiber:float=0