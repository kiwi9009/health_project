
class RuleBmi:

    def __init__(self,user):
        self.user = user


    def check_bmi_level(self)->str:
        if self.user.bmi < 18.5:
            self.user.bmi_level = 'Underweight'
        elif 18.5 <= self.user.bmi <= 22.9:
            self.user.bmi_level ='Nomal'
        elif 23.0 <= self.user.bmi <= 24.9:
            self.user.bmi_level = 'Overweight'
        elif 25.0 <= self.user.bmi <= 29.9:
            self.user.bmi_level = 'Obese Class I'
        elif self.user.bmi > 30.0:
            self.user.bmi_level = 'Obese Class II'

        return self.user.bmi_level
