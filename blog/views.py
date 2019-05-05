from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

dummy_posts=[
    {
        'author':'Sangamithra',
        'title':'Django web app',
        'content':'My first web site creation done using django',
        'date_posted':'February 10,2019'
    },
    {
        'author':'Thirugnanam',
        'title':'Django web app2',
        'content':'My second web app was personal portfolio',
        'date_posted':'February 20,2019'
    }
]
#posts={}
#posts=dummy_posts

# Create your views here.
def home(request):
    return render(request, 'blog/home.html',{"posts":Post.objects.all()})

class PostListView(ListView):#this will look for template with the name <app>/<model>_viewtype. 
    #if you dont want such type mention template_name variable
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=5

class PostDetailView(DetailView):#this will look for template with the name <app>/<model>_viewtype. 
    #if you dont want such type mention template_name variable
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    #LoginRequiredMixin is used as areplacemnet of decorator to make login a mandatory
    #this will look for template with the name <app>/<model>_viewtype. 
    #if you dont want such type mention template_name variable
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        #an existing method which we are overridigng to add the author as current logged in user
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    #LoginRequiredMixin is used as areplacemnet of decorator to make login a mandatory
    #UserPassesTestMixin is used to verify the same user is uediting the post
    #this will look for template with the name <app>/<model>_viewtype. 
    #if you dont want such type mention template_name variable
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        #an existing method which we are overridigng to add the author as current logged in user
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        else:
            return False
    
class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):#this will look for template with the name <app>/<model>_viewtype. 
    #if you dont want such type mention template_name variable
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True

        else:
            return False



class UserPostListView(ListView):#this will look for template with the name <app>/<model>_viewtype. 
    #if you dont want such type mention template_name variable
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    #ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

def about(request):
    return render(request, 'blog/about.html',{"title":"About Blogs"})