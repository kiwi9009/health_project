import requests,json
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

#Data reciceper
class UsdaFood:
    
    def __init__(self):
        self.api_key = os.getenv('USDA_API_KEY')
    
    def search_food(self,keyword)->json:
        try:
            url = URL

            params = {
                "api_key": self.api_key,
                "query": keyword,
                "pagesize": 10,
            }
            
            headers = {"Accept": "application/json", "User-Agent": "Mozilla/5.0"}
            response = requests.get(url, params=params, headers=headers, timeout=15)

            response.raise_for_status()
            
            data = response.json()
            
            return data
        
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error{errh}")

        except requests.exceptions.ConnectionError as errc:
            print(f"Error connecting to Server {errc}")

        except requests.exceptions.RequestException as err:
            print(f"Unknow Error Occurred {err}")
    

    
