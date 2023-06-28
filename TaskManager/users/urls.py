from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
	UserViewSet,
	ActivityViewSet,CommentViewSet
)
router = SimpleRouter()
router.register("users",UserViewSet,basename='users')
router.register("comments",CommentViewSet,basename='comments')
router.register("activities",ActivityViewSet,basename='activities')



urlpatterns = router.urls