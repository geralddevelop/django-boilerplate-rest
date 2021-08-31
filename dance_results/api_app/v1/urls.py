# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'competitions', views.CompetitionViewSet)
router.register(r'adjudicators', views.AdjudicatorViewSet)
router.register(r'dances', views.DanceViewSet)
router.register(r'events', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
