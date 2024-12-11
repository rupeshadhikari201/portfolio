from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

def contact(request):
    success_message = None  # Initialize success message
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():
            Contact.objects.get_or_create(
                name=form_data.cleaned_data['name'],
                email=form_data.cleaned_data['email'],
                defaults={'message': form_data.cleaned_data['message']}
            )
            success_message = "Thanks for submitting the form!"
    else:
        form_data = ContactForm()

    return render(request, 'contact/contact.html', {
        'contact_form': form_data,
        'success_message': success_message
    })
