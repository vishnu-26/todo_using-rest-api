from django.forms import ModelForm
from api.models import Todo
from django.contrib.auth import get_user_model
User = get_user_model()


#class TodoForm(ModelForm):
#    class Meta:
#        model = Todo
#        fields = ['title']


class loginForm(ModelForm):
    class Meta:
        model = User
        fields=['username','password']


    
