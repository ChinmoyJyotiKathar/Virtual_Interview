
from django.http import HttpResponse
from .models import Album
from django.template import loader

def index(request):
	all_albums = Album.objects.all()
	#myhtml = ''
	#for album in all_albums:
	#	url = '/polls/'+ str(album.id) +'/'
	#	myhtml += '<a href="' + url + '">'+ album.album_title +'</a> </br>'
	#return HttpResponse(myhtml)

	template = loader.get_template('polls/index.html') #we don't need to explicitly mention template/..
	context = {
		'all_albums': all_albums,

	}
	return HttpResponse(template.render(context, request))

def detail(request, album_id):
	return HttpResponse("<h2> Details for Album id =  " + str(album_id) + "</h2>")
