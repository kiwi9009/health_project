
from tabulate import tabulate
import textwrap
from shared.helper.utils import cls

class Display:
    @staticmethod
    def show_menu():
        print('Select Option:')
        print('1) Test Body Metric.')
        print('2) Show food inventory')
    
    
    @staticmethod
    def raw_food_table(foods,max_width=50):
        table = []
        for food in foods:
            wrapped_name = textwrap.fill(food.name,width=max_width)
            table.append({
                'Name':wrapped_name,
                'Calo':food.calories,
                'Protein':food.protein,
                'Carbon':food.carbs,
                'Fiber':food.fiber,
                'Fat':food.fat
            })    
           
        
        print(tabulate(table,
                       headers='keys',
                       tablefmt='fancy_grid',
                       colalign=('left','left','left','left','left','left')
                       ))
    @staticmethod
    def user_table(user):
        print(tabulate(
            [user.__dict__],
            headers='keys',
            tablefmt='fancy_grid'
        ))
        
    @staticmethod
    def region(regions_menu):
        cls()
        print('LIST OF REGION')
        data = list(regions_menu.items())
        print(tabulate(data,
                       headers=['Selection','Region Code'],
                       tablefmt='fancy_grid',
                       colalign=('center','center')))
    
    def active_points(ap):
        cls()
        print('LIST OF WORKOUT')
        data = list(ap.items())
        print(tabulate(data,
                       headers =['Action Level','Active Points'],
                       tablefmt='fancy_grid',
                       colalign=('center','center')))
                                                    
                
                        