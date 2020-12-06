from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    """
    We are gonna test the init method
    """
    def test_create_user(self):
        user = UserModel('test', 'password123')

        self.assertEqual(user.username, 'test', "Custom message")
        self.assertEqual(user.password, 'password123', "Custom error message password")