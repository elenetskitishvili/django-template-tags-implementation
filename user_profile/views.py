from django.shortcuts import render
from datetime import datetime
from .forms import ContactForm  

def user_profile(request):
    user = {
        'name': 'Elene Tskitishvili',
        'email': 'elene.tskitishvili504@gmail.com',
        'date_joined': datetime.strptime('2022-04-15', '%Y-%m-%d'),
        'posts': [
            {'title': 'My First Post', 'date_published': datetime.strptime('2024-08-01', '%Y-%m-%d')},
            {'title': 'Learning Django', 'date_published': datetime.strptime('2024-09-10', '%Y-%m-%d')},
        ]
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success_message = 'Thank you! Your form has been submitted successfully.'
            return render(request, 'user_profile/profile.html', {'user': user, 'form': form, 'success_message': success_message})
        else:
            error_message = 'Please correct the errors below.'
            return render(request, 'user_profile/profile.html', {'user': user, 'form': form, 'error_message': error_message})
    else:
        form = ContactForm()  

    return render(request, 'user_profile/profile.html', {'user': user, 'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            success_message = 'Thank you for getting in touch!'
            return render(request, 'user_profile/contact.html', {'form': form, 'success_message': success_message})
        else:
            error_message = 'Please correct the errors in the form.'
            return render(request, 'user_profile/contact.html', {'form': form, 'error_message': error_message})
    else:
        form = ContactForm()
    
    return render(request, 'user_profile/contact.html', {'form': form})
