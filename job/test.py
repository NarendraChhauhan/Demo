import requests 
import unittest
from unittest.mock import patch , Mock

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/user/{user_id}")
    return response.json()

class TestUserData(unittest.TestCase):
    @patch('requests.get')
    def test_user_data(self,get_mock):
        mock_response = Mock()
        response_dict = {'name':'John','email':'john@example'}
        mock_response.json.return_value = response_dict
        get_mock.return_value = mock_response

        user_data = get_user_data(1)
        get_mock.assert_called_with("https://api.example.com/user/1")
        self.assertEqual(user_data,response_dict)


if __name__ == '__main__':
    unittest.main()
