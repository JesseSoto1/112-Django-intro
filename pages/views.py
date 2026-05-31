from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse







# Create your views here.
# classe based views
# This is in PASCAL NOTATION
class HomePageView(TemplateView):# OOP object oriented programming (inheritance)
    template_name = "home.html" # when variables are inside funtions they turn into attributes


class AboutPageView(TemplateView):
    template_name = "about.html"


# function based views
# Snake case Notations
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    return render(request, "contact.html")