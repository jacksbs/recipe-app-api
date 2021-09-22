from django.urls import path

# from rest_framework.routers import DefaultRouter

from user import views


app_name = 'user'

# router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet,
# base_name='hello-viewset')
# router.register('profile', views.UserProfileViewSet)
# router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me')
    # path('login/', views.UserLoginApiView.as_view()),
    # path('', include(router.urls))
]
