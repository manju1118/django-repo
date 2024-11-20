from django import forms
from users.models import Post





class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['id','title','pub_date']