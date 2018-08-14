from django.shortcuts import render

# Create your views here.
from .forms import ProfileForm

def profile_create_view(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'profiles/profile_create.html', context)