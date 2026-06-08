from typing import Optional,Any
import re
import os


def validate_input(
        prompt:str,
        pattern:str,
        error_message:str,
        strip:bool=False,
        lower:bool=False,
        upper:bool=False,
        constant:Optional[callable]=None,
        convert:Optional[callable]=None,
        max_value:Optional[callable]=None,
        min_value:Optional[callable]=None,
        display:Optional[callable] = None,
        ) ->Any:
        if display:
            display

        while True:
            try:
                user_input = input(f'{prompt}').strip() if strip else input(f'{prompt}')
                user_input = user_input.upper() if upper else user_input
                user_input = user_input.lower() if lower else user_input

                if not re.match(pattern,user_input):
                    raise ValueError

                if convert:
                    value = convert(user_input)
                else:
                    value = user_input

                if min_value is not None and value < min_value:
                    raise ValueError(f'Value invalid! Value need to >= {min_value}')

                if max_value is not None and value > max_value:
                    raise ValueError(f'Value invalid! Value need to <= {max_value}')

                if constant:
                    return constant[f'{value}']

                return value

            except ValueError:
                print(f"{error_message}")
                continue

            except Exception as e:
                print(f"Error {e}")


def cls():
    os.system('clear')
