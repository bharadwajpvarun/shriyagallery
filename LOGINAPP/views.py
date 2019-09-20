from django.shortcuts import render,redirect
from django.contrib import messages
from LOGINAPP.models import imagecount
from django.core.files.storage import FileSystemStorage

def upload(response):
	if response.method == 'POST':
		upload = response.FILES['image']
		st = FileSystemStorage()
		st.save(upload.name,upload)
		messages.success(response, f'YooHooo {upload} is Uploaded !')
		return redirect('upload')
	return render(response,'LOGINAPP/upload.html')

def populate(response):
		data = imagecount.objects.all()[:1].get()
		return render(response, 'LOGINAPP/gallery.html',{"data":data})

