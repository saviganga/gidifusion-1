from django.test import TestCase
from account.models import MyUser, Team, Player, Fan

class MyUserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.test_user1 = MyUser.objects.create(
            email='testuser1@testuser.com', 
            name='testuser1',
            is_team=True
        )

        cls.test_user2 = MyUser.objects.create(
            email='testuser2@testuser.com',
            name='testuser2',
            is_player=True
        )

        cls.test_user3 = MyUser.objects.create(
            email='testuser3@testuser.com',
            name='testuser3',
            is_fan=True
        )

    def test_user1_type(self):
        self.assertEqual(self.test_user1.is_fan, False)
        self.assertEqual(self.test_user1.is_player, False)
        self.assertEqual(self.test_user1.is_team, True)

    def test_user2_type(self):
        self.assertEqual(self.test_user2.is_fan, False)
        self.assertEqual(self.test_user2.is_player, True)
        self.assertEqual(self.test_user2.is_team, False)

    def test_user3_type(self):    
        self.assertEqual(self.test_user3.is_fan, True)
        self.assertEqual(self.test_user3.is_player, False)
        self.assertEqual(self.test_user3.is_team, False)


# Create your tests here.
