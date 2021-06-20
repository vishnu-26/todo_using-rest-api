from django.forms import ModelForm
from api.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title']


    
