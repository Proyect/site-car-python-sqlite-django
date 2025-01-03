from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import AutoAPIView, ImgAPIView, DescriptionAPIView,home, detail

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('autos/', AutoAPIView.as_view(), name='autos_api'),
    path('imagenes/', ImgAPIView.as_view(), name='imagenes_api'),
    path('publicaciones/', DescriptionAPIView.as_view(), name='publicaciones_api'),
    path('sitio/', home, name='home'),
    path('detalle/<int:vehicle>', detail, name="detail"),
]
