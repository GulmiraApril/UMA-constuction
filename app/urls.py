from django.urls import path
from .views import home_view, contact_view, about_view, service_view, project_view, projects_single_view

urlpatterns = [
    path("", home_view),
    path("about/", about_view),
    path("contact/", contact_view),
    path("services/", service_view),
    path("projects/", project_view),
    path("projects/<int:pk>", projects_single_view)
]
