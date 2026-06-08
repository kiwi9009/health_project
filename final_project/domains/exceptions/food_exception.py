


class FoodNotFoundError(Exception):
    def __init__(self,keyword):
        super().__init__(
            f'Cant not find food name {keyword}'
        )


