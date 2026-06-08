from usda.usda_client import UsdaFood
from repository.food_repository import FoodRepository
from services.food_service import FoodService
from services.user_service import UserService
from services.rules import RuleBmi
from controller.food_controller import FoodController
from controller.user_controller import UserController
from presentation.input_handle import InputServices,GetUser
from presentation.display import Display
from domains.exceptions.food_exception import FoodNotFoundError


def main():
    Display.show_menu()
    menu_select = InputServices.menu_select()
    if menu_select == 2:
        menu_inventory()

    if menu_select == 1:
        menu_metric()


def bmi_level(user):
    rule_bmi = RuleBmi(user)
    return rule_bmi.check_bmi_level()


def menu_metric()->None:
    user_call = GetUser.user_profile()
    user_service = UserService(user_call)
    user_controller = UserController(user_service)
    user = user_controller.get_user()
    bmi_level(user)
    Display.user_table(user)


def menu_inventory()->None:
    client = UsdaFood()
    repository = FoodRepository(client)
    service = FoodService(repository)
    controller = FoodController(service)
    
    while True:
        keyword = InputServices.keyword()
        try:
            foods = controller.search_food(keyword)
            break

        except FoodNotFoundError as e:
            print(e)

    Display.raw_food_table(foods)


if __name__ == "__main__":
    main()



