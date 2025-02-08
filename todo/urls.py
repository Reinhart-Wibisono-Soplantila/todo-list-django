from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet
from .views import ToDoAPIView

# Menggunakan router untuk ViewSet
router=DefaultRouter()
router.register(r'todos',ToDoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
    path('todoapi/', ToDoAPIView.as_view()),
    path('todoapi/<int:todo_id>', ToDoAPIView.as_view())
]


