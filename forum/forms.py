from .models import Comments
from django import forms


class CommentsForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comments
        fields = ['body']