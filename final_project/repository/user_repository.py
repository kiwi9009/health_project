from domains.models.user_model import UserProfile

class UserRepository:
    def __init__(self,user):
        self.user=user

    def user_profile(self)->UserProfile:
        return self.user
