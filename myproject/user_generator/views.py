from django.shortcuts import render
from .forms import MassUsercreationForm
from .models import User

def mass_user_creation(request):
    if request.method == 'POST':
        form = MassUserCreationForm(request.POST)
        if form.is_valid():
            num_users = form.cleaned_data['num_users']
            for i in range(num_users):

                User.objects.create(username=f'User{i}', email=f'user{i}@example.com')
            return render(request, 'success.html')
    else:
        form = MassUserCreationForm()
    return render(request, 'mass_user_creation.html', {'form': form})

# Create your views here.
