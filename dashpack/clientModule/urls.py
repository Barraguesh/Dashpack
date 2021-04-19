#Python/Django
from django.urls import include, path
from rest_framework import routers

from clientModule import views

from clientModule.api import viewSets

#API - Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'client', viewSets.ClientViewSet)
router.register(r'device', viewSets.DeviceViewSet)
router.register(r'ticket', viewSets.TicketViewSet)

urlpatterns = [
    path('', views.index_view, name='clientModule'),

    path('ticket/<ticket_id>', views.ticket_view, name='ticket'),
    path('device/<device_id>', views.device_view, name='device'),
    path('load_table/', views.load_table_view, name='load_table'),

    path('api/', include(router.urls)),
]