from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("blog-details/", views.blog_details, name="blog_details"),
    path("contact/", views.contact, name="contact"),
    path("error/", views.error, name="error"),
    path("notes/", views.notes, name="notes"),
    path("pricing/", views.pricing, name="pricing"),
    path("project/", views.project, name="project"),
    path("project-details/", views.project_details, name="project_details"),
    path("review/", views.review, name="review"),
    path("services/", views.services, name="services"),
    path("service-details/", views.service_details, name="service_details"),
    path("team/", views.team, name="team"),
]
