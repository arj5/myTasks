from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task


class SignUpForm(UserCreationForm):
    first_name = forms.CharField( max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField( max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField( required=True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

# Adding tasks form
class AddTaskForm(forms.ModelForm):
    
    task_title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Title")
    description = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Description")
    priority = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Priority")
    status = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Status")
    est_time = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Estimated time to complete")
    due_date = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), label="Due Date")

    class Meta:
        model = Task
        fields= ('task_title', 'description', 'priority', 'status', 'est_time', 'due_date')
