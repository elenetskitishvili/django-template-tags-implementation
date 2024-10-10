from django.shortcuts import render
from datetime import datetime

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
    return render(request, 'user_profile/profile.html', {'user': user})
