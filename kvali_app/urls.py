from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    path('', views.index, name='kvali_index'),
    path('api/', include(router.urls), name='api')
]