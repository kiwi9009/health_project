import pytest
from domains.models.user_model import UserProfile
from services.user_service import UserService
from services.rules import RuleBmi
from services.food_service import FoodService
from domains.exceptions.food_exception import FoodNotFoundError
from repository.food_repository import FoodRepository
from controller.food_controller import FoodController


def test_user_service():

    mock_user = UserProfile(
                name='dung',
                gender='male',
                age=35,
                weight=70,
                height=175,
                region_key='SAS',
                active_points=1.2,
                bmi=0,
                tdee=0)

    user_service =  UserService(mock_user)
    result= user_service.user_metric()
    assert result.bmi == 22.9
    assert result.tdee >0
    assert result.name == 'dung'

def test_bmi_level():
    mork_user = UserProfile(
        name='dung',
                gender='male',
                age=35,
                weight=70,
                height=175,
                region_key='SAS',
                active_points=1.2,
                bmi=23.0,
                bmi_level = '',
                tdee=0
    )

    rule_bmi = RuleBmi(mork_user)
    assert rule_bmi.check_bmi_level() =='Overweight'

def test_food_service():

    fake_client = {
                   'foods':[]}

    class FakeRepository:
        def __init__(self,client):
            self.client = client

        def search_food(self,keyword:str)->list:
            return self.client


    fake_repo = FakeRepository(fake_client)

    food_service = FoodService(fake_repo)

    food_controller = FoodController(food_service)


    with pytest.raises(FoodNotFoundError):
        food_controller.search_food('ffff')

