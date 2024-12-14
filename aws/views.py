from django.shortcuts import render, redirect
from .forms import TestFileForm

def upload_file(request):
    if request.method == 'POST':
        form = TestFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload_success.html')
    else:
        form = TestFileForm()
    return render(request, 'main_app/aws/index.html', {'form': form})
