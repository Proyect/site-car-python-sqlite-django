from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from Site import views
from .views import AutoAPIView, ImgAPIView, DescriptionAPIView

router = routers.DefaultRouter()
#router.register(r'autos', views.AutosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('autos/', AutoAPIView.as_view(), name='autos_api'),
    path('imagenes/', ImgAPIView.as_view(), name='imagenes_api'),
    path('publicaciones/', DescriptionAPIView.as_view(), name='publicaciones_api'),
]
