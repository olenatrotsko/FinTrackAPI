from django.urls import path

from categories.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CategoryListCreateAPIView.as_view(), name='categories'),
    path('<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
]
