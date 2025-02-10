from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet
from .views import ToDoAPIView

# Menggunakan router untuk ViewSet
router=DefaultRouter()
router.register(r'todos',ToDoViewSet)

urlpatterns = [
    # Menggunakan Viewset
    # path('api/', include(router.urls)),
    
    # Menggunakan APIView
    path('api/', ToDoAPIView.as_view()),
    path('api/<int:todo_id>', ToDoAPIView.as_view())
]


