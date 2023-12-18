from django.urls import path
from .views import TriviaList, TriviaDetail

app_name = 'sadosma'

urlpatterns = [
    path('detail/<int:pk>/', TriviaDetail.as_view(), name='detail'),
    path('', TriviaList.as_view(), name='list'),
]