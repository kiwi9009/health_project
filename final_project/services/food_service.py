from mapper.mapper import FoodMapper
from domains.exceptions.food_exception import FoodNotFoundError

class FoodService:  # Xử lý dữ liệu và lọc kết quả
    def __init__(self,repository):
        self.repository = repository

    def search_food(self,keyword) -> list[list]:

        raw_data =  self.repository.search_food(keyword)
        foods = []

        if not raw_data['foods']:
            raise FoodNotFoundError(keyword)

        for item in raw_data['foods']:
            foods.append(FoodMapper.from_usda(item))

        return foods






