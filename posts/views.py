from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)


from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy




# Create your views here.
class PostListView(ListView):# a GET request ----> List
    #template_name attribute renders a specific html file
    template_name = "list.html"
    # model attribute let django know from which model (table) we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the name on how we call it inside of the templates
    context_object_name = "posts"

class PostDetailView(DetailView): #GET request ----> Single Object
    template_name = "detail.html"
    model = Post
    context_object_name = "single_post"


class PostCreateView(CreateView): # POST request ---> New Object ?empty form HTML
    template_name = "new.html"
    model = Post
    # fields attribute is a list that allows us to enable/disable the inputs to render in the html
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        print(form)
        print(form.instance)
        print(form.instance.author)
        return super().form_valid(form)


class PostUpdateView(UpdateView):# POST request --> a;ter an existing object? filled from html
    template_name = "edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]


class PostDeleteView(DeleteView):# POST reuqest ---> a form to delete the object.
    template_name = "delete.html"
    model = Post
    success_url = reverse_lazy("post_list") #used to redirect the user to any other view if the request is successful

