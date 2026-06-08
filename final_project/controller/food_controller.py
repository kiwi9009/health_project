from domains.exceptions.food_exception import FoodNotFoundError
class FoodController:
    def __init__(self,service):
        self.service = service

    def search_food(self,keyword):

            try:
                return self.service.search_food(keyword)

            except FoodNotFoundError:
                raise

