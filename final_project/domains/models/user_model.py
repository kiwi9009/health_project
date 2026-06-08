from dataclasses import dataclass

@dataclass
class UserProfile:
    name:str
    gender:str
    age:float
    weight:float
    height:float
    region_key:str
    active_points:float
    bmi:float=0
    bmi_level:str=''
    tdee:float=0

