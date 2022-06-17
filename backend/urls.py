from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', views.TaskList.as_view()),
    path('api/tasks/<int:pk>', views.TaskDetail.as_view()),
    path('api/task/<int:pk>', views.TaskDetails.as_view()),
    path("api/user/get-details", views.UserDetailAPI.as_view()),
    path('api/user/register', views.RegisterUserAPIView.as_view()),
    # path('api-token-auth', views.obtain_auth_token),
]
