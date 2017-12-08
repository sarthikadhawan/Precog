from __future__ import unicode_literals

from django.shortcuts import render


from django.http import HttpResponseRedirect

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main import *

from django.core.files.storage import FileSystemStorage




from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def home(request):
	if request.method == 'POST':

  		myfile = request.FILES['myfile']
		fs = FileSystemStorage(location=os.getcwd()+'/django_precog/static/')

		'''try:
			os.remove(os.getcwd()+'/django_precog/static/test.jpg')
		except:
			print '''''

		u = fs.url("test.jpg")
		uu=u.split("/")[2]
		filename = fs.save(uu, myfile)
		
		uploaded_file_url = u

		'''return render(request, 'home.html', {
		    'uploaded_file_url': uploaded_file_url
		})'''
		results=main(filename)

		return render(request, 'output.html', {
		    "output":results,
		    "MEDIA_URL":settings.MEDIA_URL,
		    "filename":filename.split(".")[0]+"_"+"Output.jpg"
		})


		

	return render(request, "home.html")




