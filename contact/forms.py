from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name:',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        label='Email:',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        label='Message:',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 4})
    )
