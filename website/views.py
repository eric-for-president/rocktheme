from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def blog_details(request):
    return render(request, "blog-details.html")


def contact(request):
    return render(request, "contact.html")


def error(request):
    return render(request, "error.html")


def notes(request):
    return render(request, "notes.html")


def pricing(request):
    return render(request, "pricing.html")


def project(request):
    return render(request, "project.html")


def project_details(request):
    return render(request, "project-details.html")


def review(request):
    return render(request, "review.html")


def services(request):
    return render(request, "services.html")


def service_details(request):
    return render(request, "service-details.html")


def team(request):
    return render(request, "team.html")
