from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from cards.models import Product

User = get_user_model()


class ApiURLTests(TestCase):
    """
    We create a test model of the product article and a test model of the user.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='niko',
            password='niko',
            email='Elnikit@rambler.ru'
        )
        cls.product = Product.objects.create(
            vendor_code=11112222,
            user=ApiURLTests.user
        )

    def setUp(self):
        """
        We create a guest client and a registered user.
        """

        self.guest_client = APIClient()
        self.authorized_client = APIClient()
        djoser_jwt_create_url = '/api/auth/jwt/create/'
        token_response = self.authorized_client.post(
            djoser_jwt_create_url,
            {'username': 'niko', 'password': 'niko'},
            format='json'
        )
        self.assertTrue('access' in token_response.data)
        token = token_response.data['access']
        self.authorized_client.credentials(
            HTTP_AUTHORIZATION='Bearer {}'.format(token)
        )

    def test_urls_response_guest(self):
        """
        Checking the status of pages for the guest.
        """

        url_status = {
            reverse('api:users-me'): HTTPStatus.UNAUTHORIZED,
            reverse('api:product-list'): HTTPStatus.UNAUTHORIZED,
            reverse(
                'api:product-detail',
                kwargs={'vendor_code': ApiURLTests.product.vendor_code}
            ): HTTPStatus.UNAUTHORIZED,
            (
                '/api/products/{}/cards/'.format(
                    ApiURLTests.product.vendor_code
                )
            ): HTTPStatus.UNAUTHORIZED
        }
        for url, status_code in url_status.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url)
                self.assertEqual(response.status_code, status_code)

    def test_urls_response_auth(self):
        """
        Checking the status of pages for an authenticated user.
        """

        url_status = {
            reverse('api:users-me'): HTTPStatus.OK,
            reverse('api:product-list'): HTTPStatus.OK,
            reverse(
                'api:product-detail',
                kwargs={'vendor_code': ApiURLTests.product.vendor_code}
            ): HTTPStatus.OK,
            (
                '/api/products/{}/cards/'.format(
                    ApiURLTests.product.vendor_code
                )
            ): HTTPStatus.OK
        }
        for url, status_code in url_status.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, status_code)
