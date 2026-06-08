

class UserController:
    def __init__(self,service):
         self.service = service
         
    def get_user(self):
        return self.service.user_metric()