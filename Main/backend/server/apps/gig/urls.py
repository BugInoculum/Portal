from django.urls import path
from gig.views import CustomUserAPI

urlpatterns = [
    # your other url configs
    path('api/users/<user_id>/profile/', CustomUserAPI.as_view())
]



from django.conf.urls import url, include 
from rest_framework.routers import DefaultRouter
from apps.notes.views import NoteViewSet

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")
notes_urlpatterns = [url("api/v1/", include(router.urls))]