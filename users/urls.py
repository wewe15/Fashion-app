from django.urls import path
from .views import SignupPageView
from .api.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('api/create/', CreateUserView.as_view(), name='create'),
    path('api/token/', CreateTokenView.as_view(), name='token'),
    path('api/me/', ManageUserView.as_view(), name='me'),
]
