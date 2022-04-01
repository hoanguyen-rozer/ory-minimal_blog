from django import forms

from src.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter your comment...'}))

    class Meta:
        model = Comment
        fields = ('user_email', 'username', 'content')

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['user_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email address'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your name'})
