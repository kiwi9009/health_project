from domains.models.user_model import UserProfile
from services.user_service import UserService
from controller.user_controller import UserController


def test_user_service():

    mock_user = UserProfile(
                name='dung',
                gender='male',
                age=35,
                weight=70,
                height=175,
                region_key='SAS',
                active_points=1.2,
                bmi=0,
                tdee=0)

    user_service =  UserService(mock_user)
    result= user_service.user_metric()
    assert result.bmi == 22.9
    assert result.tdee >0
    assert result.name == 'dung'

