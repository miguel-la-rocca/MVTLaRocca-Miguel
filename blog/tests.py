# Create your tests here.

import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post


class CourseTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345",
        )
        Post.objects.create(name="Python", code=123, owner=self.test_user)
        Post.objects.create(name="Docker", code=789, owner=self.test_user)

        Post_test_num = 20
        self.mock_names = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(Post_test_num)
        ]
        self.mock_codes = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(Post_test_num)
        ]

        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            Post.objects.create(name=mock_name, code=mock_code, owner=self.test_user)

    def test_post_model(self):
        """Posts creation are correctly identified"""
        python_post = Post.objects.get(name="Python")
        docker_post = Post.objects.get(name="Docker")
        self.assertEqual(python_post.owner.username, "testuser")
        self.assertEqual(docker_post.owner.username, "testuser")
        self.assertEqual(python_post.code, 123)
        self.assertEqual(docker_post.code, 789)

    def test_post_list(self):
        for mock_name, mock_code in zip(self.mock_names, self.mock_codes):
            post_test = Post.objects.get(name=mock_name)
            self.assertEqual(post_test.owner.username, "testuser")
            self.assertEqual(post_test.code, mock_code)