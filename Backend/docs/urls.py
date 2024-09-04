from django.urls import path
from .views import LyhDocListCreateAPIView, LyhDocEditDeleteAPIView, LyhDocDetailAPIView

urlpatterns = [
    path('', LyhDocListCreateAPIView.as_view(), name='doc-list-create'),
    path('<int:pk>/', LyhDocEditDeleteAPIView.as_view(), name='doc-edit-delete'),
]
