from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Tree


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_thing = Tree.objects.create(author=test_user, tree_name="Redwoods", tree_facts="Tall and Beautiful")
        test_thing.save()

    def test_things_model(self):
        thing = Tree.objects.get(id=1)
        actual_author = str(thing.author)
        actual_tree_name = str(thing.tree_name)
        actual_tree_facts = str(thing.tree_facts)
        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_tree_name, "Redwoods")
        self.assertEqual(actual_tree_facts, "Tall and Beautiful")
