from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy

urlpatterns = [
    path('', ProductListCreate.as_view()),
    path('<int:pk>/', ProductRetrieveUpdateDestroy.as_view()),
]