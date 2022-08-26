from django.views.generic.edit import CreateView
from users.forms import SignupForm

class signup(CreateView):
    template_name = 'users/signup/signup.html'
    form_class = SignupForm