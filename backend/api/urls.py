from django.urls import path
from .views import *

app_name="api"

urlpatterns = [
  path('users/', UserListView.as_view(), name='users'), # Read
  path('users/<str:username>/', UserApiView, name='user'), # Read
  path('user/id/<int:pk>/', UserIDApiView, name='user_id'), # Updata
  path('users/updata/<int:pk>/', UpdataUserApiView, name='updata_user'), # Updata
  path('profiles/', ProfilesApiView, name='profiles'), #Read
  path('profiles/<int:user>/', ProfileApiView, name='profile'), #Read
  path('profiles/updata/<int:user>/', UpdataProfileApiView, name='updata_profile'), #Updata
]