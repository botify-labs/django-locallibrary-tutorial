import json
from rest_framework.test import APIClient

from django.test import TestCase
from django.urls import reverse
from catalog.models import Author


class AuthorListTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create(self):
        response = self.client.post(
            reverse('author_list'),
            data={
                "first_name": "Jules",
                "last_name": "Verne",
                "date_of_birth": "1828-02-08",
                "date_of_death": "1905-03-24",
            },
            format='json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.content), {
            "id": 1,
            "first_name": "Jules",
            "last_name": "Verne",
            "date_of_birth": "1828-02-08",
            "date_of_death": "1905-03-24",
        })

    def test_list(self):
        jules_verne = Author.objects.create(
            first_name="Jules",
            last_name="Verne",
            date_of_birth="1828-02-08",
            date_of_death="1905-03-24",
        )
        george_orwell = Author.objects.create(
            first_name="George",
            last_name="Orwell",
            date_of_birth="1903-06-25",
            date_of_death="1950-01-21",
        )

        response = self.client.get(
            reverse('author_list'),
            format='json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [{
            "id": jules_verne.pk,
            "first_name": "Jules",
            "last_name": "Verne",
            "date_of_birth": "1828-02-08",
            "date_of_death": "1905-03-24",
        }, {
            "id": george_orwell.pk,
            "first_name": "George",
            "last_name": "Orwell",
            "date_of_birth": "1903-06-25",
            "date_of_death": "1950-01-21",
        }])


class AuthorDetailTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Add an author into the DB:
        self.jules_verne = Author.objects.create(
            first_name="Jules",
            last_name="Verne",
            date_of_birth="1828-02-08",
            date_of_death="1905-03-24",
        )

    def test_retrieve(self):
        response = self.client.get(
            reverse(
                'author_detail',
                kwargs={'pk': self.jules_verne.pk}
            ),
            format='json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "id": self.jules_verne.pk,
            "first_name": "Jules",
            "last_name": "Verne",
            "date_of_birth": "1828-02-08",
            "date_of_death": "1905-03-24",
        })

    def test_update(self):
        response = self.client.put(
            reverse(
                'author_detail',
                kwargs={'pk': self.jules_verne.pk}
            ),
            data={
                "first_name": "Jules",
                "last_name": "TOTO",
                "date_of_birth": "1828-02-08",
                "date_of_death": "1905-03-24",
            },
            format='json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "id": self.jules_verne.pk,
            "first_name": "Jules",
            "last_name": "TOTO",
            "date_of_birth": "1828-02-08",
            "date_of_death": "1905-03-24",
        })

    def test_patch(self):
        response = self.client.patch(
            reverse(
                'author_detail',
                kwargs={'pk': self.jules_verne.pk}
            ),
            data={
                "last_name": "TOTO",
            },
            format='json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {
            "id": self.jules_verne.pk,
            "first_name": "Jules",
            "last_name": "TOTO",
            "date_of_birth": "1828-02-08",
            "date_of_death": "1905-03-24",
        })

    def test_destroy(self):
        response = self.client.delete(
            reverse(
                'author_detail',
                kwargs={'pk': self.jules_verne.pk}
            ),
            format='json',
        )
        self.assertEqual(response.status_code, 204)
