from unittest import TestCase
from unittest.mock import patch


# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
from vl3.testing.mocking.Mock_Requests import Blog


class TestBlog(TestCase):

    @patch('vl3.testing.mocking.Mock_Requests.Blog')
    def test_blog_posts(self, MockBlog):
        mocked_blog = MockBlog()

        # setting the return value of the mocked class/method
        # Attention: don't use brackets to call the method!
        mocked_blog.get_posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Rixty Minutes',
                'body': 'Nobody exists on purpose. Nobody belongs anywhere. We’re all going to die. Come watch TV.'
            }
        ]

        response = mocked_blog.get_posts()
        self.assertIsNotNone(response)

        self.assertIsInstance(response[0], dict)
        self.assertEqual(response[0]["id"], 1)
        self.assertEqual(response[0]["userId"], 1)
        self.assertEqual(response[0]["title"], 'Rixty Minutes')
        self.assertIn("Come watch TV", response[0]["body"]) # second value contains first one

        # Additional assertions
        mocked_blog.get_posts.assert_called_with()  # We called the get_posts method with no arguments
        mocked_blog.get_posts.assert_called_once_with()  # We called the get_posts method once with no arguments
        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.get_posts() with no arguments

        mocked_blog.reset_mock()  # Reset the mock object
        mocked_blog.get_posts.assert_not_called()  # After resetting, posts has not been called.
