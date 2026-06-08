from shared.helper.utils import validate_input
from domains.models.user_model import UserProfile
from presentation.menu import REGIONS_MENU,ACTIVE_POINTS
from presentation.display import Display

class InputServices:
    @staticmethod
    def menu_select():
        return validate_input(
            prompt='Enter your selection [1-2]',
            pattern = r'^[1|2]$',
            error_message ='Invalid choice',
            convert = int,
            min_value =1,
            max_value=2
        )

    @staticmethod
    def keyword():
        return validate_input(
                prompt = "Enter name of food: ",
                pattern = r"[a-zA-Z0-9 ]+$",
                error_message ='Invalid foodname',
                strip = True,
                lower = True
                )

class GetUser:
    # Get user's name
    def user_profile()->UserProfile:
        return UserProfile (
            name = validate_input(
                prompt = 'Enter your [NAME]: ',
                pattern = r"^[a-zA-Z0-9 ]+$",
                error_message ='Invalid name [string only]',
                strip = True
                ),
            gender = validate_input(
                prompt = 'Enter your [GENDER]: ',
                pattern = r"(male|female)$",
                error_message='Enter male or female only!',
                strip=True,
                lower=True
                ),
            age = validate_input(
                prompt = 'Enter your [AGE]: ',
                pattern = r'^([1-9]|[1-9][0-9])$',
                error_message = 'Ivalid AGE, allow[] age from [ 1-99 ]',
                convert = int,
                min_value = 1,
                max_value = 99
                ),
            weight=validate_input(
                prompt = 'Enter your [Weight] Kilogram: ',
                pattern = r'^\d*\.?\d+$',
                error_message ='Invalid [Weight] allow[1.0~150.0kg]',
                convert=float,
                min_value = 1.0,
                max_value = 150.0
                ),
            height=validate_input(
                prompt='Ener your [Height] Centimet: ',
                pattern = r'^\d*\.?\d+$',
                error_message = 'Invalid [Height] allow[10~250cm]',
                convert=float,
                min_value = 10.0,
                max_value = 250.0
                ),
            region_key= validate_input(
                prompt = 'Enter your [Region Code]: ',
                pattern = r'^[1-5]$',
                convert=int,
                constant=REGIONS_MENU,
                min_value=1,
                max_value=5,
                error_message = 'Invalid [code], try again [1-5]',
                display=Display.region(REGIONS_MENU)
                ),
            active_points=validate_input(
                prompt = 'Enter your active points [float]',
                pattern = r'^\d*\.?\d+$',
                error_message ='Enter float active_points [1.2-1.9]',
                convert = float,
                min_value = 1.2,
                max_value = 1.9,
                display=Display.active_points(ACTIVE_POINTS)
                )
        )


