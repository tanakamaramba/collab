from frontend.views import index
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser

def test_if_frontend_app_view_returns_200():
    factory = RequestFactory()
    request = factory.get('')
    request.user = AnonymousUser()

    response = index(request)
    assert response.status_code == 200