from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

#「ModelViewSet」を継承しているクラス
router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('post', views.PostViewSet)
router.register('comment', views.CommentViewSet)

#「generics.___APIView」を継承しているクラス
urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('', include(router.urls))
]
