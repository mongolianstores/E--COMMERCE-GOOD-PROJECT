from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .models import Post, University




# if you are not login you can not see this view 
class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/index.html'
    fields = ['title', 'body']
    
    

# A next-level permissions is something specific to the user. In our case, let's enforce the rule that only the author of a blog post can update it. We can use the built-in UserPassesTestMixin for this.
class BlogUpdateViews(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/index.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.title == self.request.user
    
# python manage.py check --deploy


def school(request):
    
    u = University.objects.get(id=1)
    context={'u': u}
    
    return render(request, 'blog/index.html', context )