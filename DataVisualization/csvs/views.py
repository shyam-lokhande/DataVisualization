import csv
from .forms import CsvForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def uploadFile(req):
    form=CsvForm(req.POST or None,req.FILES or None)
    if form.is_valid():
        form.save()
        form=CsvForm()

        obj=CsvUpload.objects.get(activated=False)
        with open(obj.file_name.path,'r') as f:
            reader=csv.reader(f)
            for row in reader:
                print(row)
                row="".join(row)
                row=row.replace(";"," ")
                row=row.split()
                user=User.objects.get(id=row[3])

        obj.activated=True
        obj.save()

    context={
        'form':form
    }

    return render(req,'csvs/upload.html',context)