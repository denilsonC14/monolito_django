from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserView, TareaEscolarViewSet

router = DefaultRouter()
router.register(r'tareas', TareaEscolarViewSet, basename='tarea')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:pk>/', UserView.as_view(), name='user'),
    path('', include(router.urls)),
]