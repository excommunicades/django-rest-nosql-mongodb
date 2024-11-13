from django.urls import path

from publish.views import ProductActions

urlpatterns = [
    path('products/', ProductActions.as_view()),
    path('products/<int:pk>/', ProductActions.as_view())
]
