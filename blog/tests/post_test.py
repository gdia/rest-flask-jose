from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test','Abracadabra')
        self.assertEquals('Test',p.title)
        self.assertEquals('Abracadabra',p.content)