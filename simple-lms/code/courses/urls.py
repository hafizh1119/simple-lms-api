from django.urls import path

from .apiv1 import apiv1

urlpatterns = [
    path('api/v1/', apiv1.urls),
]
