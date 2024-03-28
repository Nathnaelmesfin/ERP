from django.shortcuts import render, redirect
from .forms import CustomUserEditForm

def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_updated')  # Redirect to a new URL
    else:
        form = CustomUserEditForm(instance=request.user)
    return render(request, 'profiles/edit_profile.html', {'form': form})
