from django.shortcuts import render, redirect
from .forms import StrayReportForm
from .models import StrayReport
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def report(request):
    if request.method == 'POST':
        form = StrayReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('nearby')  # Redirect to map page
    else:
        form = StrayReportForm()
    return render(request, 'report.html', {'form': form})

def nearby(request):
    reports = StrayReport.objects.exclude(latitude__isnull=True, longitude__isnull=True)
    data = list(reports.values('latitude', 'longitude', 'location', 'description', 'photo'))  # Added photo & desc
    return render(request, 'nearby.html', {'reports': json.dumps(data, cls=DjangoJSONEncoder)})

def donate(request):
    return render(request, 'donate.html')
