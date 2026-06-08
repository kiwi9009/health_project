from domains.models.user_model import UserProfile


class UserService:
    def __init__(self,user):
        self.user = user

    def user_metric(self)->UserProfile:
        weight = self.user.weight
        height = self.user.height
        self.user.bmi = round(weight / ((height * 0.01) ** 2),1)

        if self.user.gender == "male":
            bmr_index = (
                66+ (13.7 * self.user.weight)+ (5 * self.user.height)- (6.8 * self.user.age)
            )
        elif self.user.gender == "female":
            bmr_index = (
                655+ (9.6 * self.user.weight)+ (1.8 * self.user.height)- (4.7 * self.user.age)
            )

        self.user.tdee = round(bmr_index * self.user.active_points,1)
        return self.user
