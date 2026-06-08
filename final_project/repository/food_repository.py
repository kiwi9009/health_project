
#storage management
import json

class FoodRepository:
    def __init__(self,client):
        self.client = client
        
    def search_food(self,keyword)->json:
        return self.client.search_food(keyword)
        