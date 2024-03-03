from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job

def postajob(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('joblist')
    else:
        form = JobForm()
    return render(request, 'postajob.html')

def joblist(request):
    form = Job.objects.all()
    return render(request, 'joblist.html',{'form': form})