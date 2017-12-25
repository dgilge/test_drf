from django.conf.urls import include, url
from rest_framework import routers
from myapp import views

router = routers.SimpleRouter()
router.register(r'testurl', views.TestViewSet, 'testview')

urlpatterns = [
    url(r'^', include(router.urls)),
]
