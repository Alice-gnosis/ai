import unittest
from unittest.mock import patch
from main import get_new_thoughts

class TestGetNewThoughts(unittest.TestCase):
    @patch('main.openai.ChatCompletion.create')
    def test_get_new_thoughts(self, mock_create):
        # Mock the API response
        mock_create.return_value = {
            'choices': [{
                'message': {
                    'content': '1. Response 1\n2. Response 2\n3. Response 3\n4. Response 4\n5. Response 5\n6. Response 6\n7. Response 7\n8. Response 8\n9. Response 9\n10. Response 10\n'
                }
            }]
        }

        expected_output = [
            {'response': 'Response 1'},
            {'response': 'Response 2'},
            {'response': 'Response 3'},
            {'response': 'Response 4'},
            {'response': 'Response 5'},
            {'response': 'Response 6'},
            {'response': 'Response 7'},
            {'response': 'Response 8'},
            {'response': 'Response 9'},
            {'response': 'Response 10'},
        ]

        # Call the function and get the output
        output = get_new_thoughts()

        # Assert that the output is as expected
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()