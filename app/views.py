from django.shortcuts import render, redirect
from .models import Contact, Project
import requests


def home_view(request):
    data = request.GET

    project = Project.objects.all()

    p = {

        'projects': project,
        'home': 'active'

    }
    return render(request, 'home.html', context=p)


def service_view(request):
    s = {
        'service': 'active'
    }
    return render(request, 'services.html', context=s)


def about_view(request):
    a = {
        'about': 'active'
    }
    return render(request, "about.html", context=a)


def project_view(request):
    data = request.GET

    projects = Project.objects.all()

    p = {
        'projects': projects,
        'project': 'active'
    }
    return render(request, 'projects.html', context=p)


def project_single_view(request, pk):
    project = Project.objects.get(id=pk)
    more_projects = Project.objects.all()

    d = {
        'project': project,
        'more_projects': more_projects,
        'project1': 'active'

    }

    return render(request=request, template_name="projects-single.html",
                  context={'project': project, 'more_projects': more_projects, 'project1': 'active'})


def contact_view(request):
    if request.method == "POST":
        data = request.POST
        obj = Contact.objects.create(name=data['name'], phone_number=data['number'], message=data['message'])

        obj.save()
        url = f"https://api.telegram.org/bot6298724589:AAHQn4M1fxewf_9bSlDQAkPi5jvS2GzPGnk/sendMessage?chat_id=748076346&text=you have a notification from UMA construction: " \
              f" Phone number of a sender is {data['number']}, message : {data['message']}"
        requests.get(url)
        return redirect('/')
    c = {
        'contact': 'active'
    }

    return render(request, "contact.html", context={'contact': 'active'})


# views.py


# def home(request):
#     active_page = 'home'  # Assuming the home page is active
#     return render(request, 'home.html', {'active_page': active_page})
#
#
# def services(request):
#     active_page = 'services'
#     return render(request, 'services.html', {'active_page': active_page})
#
#
# def projects(request):
#     active_page = 'projects'
#     return render(request, 'projects.html', {'active_page': active_page})
#
#
# def about(request):
#     active_page = 'about'
#     return render(request, 'about.html', {'active_page': active_page})
#
#
# def contact(request):
#     active_page = 'contact'
#     return render(request, 'contact.html', {'active_page': active_page})
