from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from autos import views

router = routers.DefaultRouter()
#router.register(r'autos', views.AutosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
