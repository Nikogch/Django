from django.contrib.auth.models import User
from django.views.generic import ListView


# Create your views here.

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'object_list'