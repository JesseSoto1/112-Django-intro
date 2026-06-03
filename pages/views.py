from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse







# Create your views here.
# classe based views
# This is in PASCAL NOTATION
class HomePageView(TemplateView):# OOP object oriented programming (inheritance)
    template_name = "home.html" # when variables are inside funtions they turn into attributes


    def get_context_data(self, **kwargs):########keyword arguments
        context = super().get_context_data(**kwargs)
        context["name"] = "Jesse"
        context["address"] = "Something 444, CA"
        context["email"] = "googs.googs" 
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"


# function based views
# Snake case Notations
def contact_me(request):
    # return HttpResponse("Hello World from a Function Based View")
    return render(request, "contact.html")
    






def get_contact_info(request):
    contact_info =  {
        "name": "John Wilkes Booth",
        "address":"123 Main St" ,
        "telephone": "123-123-1234",
        "email":"osok@gmail.com"
    }

    return render(request, "contact.html", contact_info)