"""
URL mappings for the user api
"""

from django.urls import path

from user import views

app_name = "user"
# for reverse look up reverse(user:create)
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
