from django.urls import path
from .views import post_view, course_view, post_create
urlpatterns = [
    path('', post_view),
    path('/create', post_create, name='post_create'),
    path('/courses', course_view, name='course_view')
]
