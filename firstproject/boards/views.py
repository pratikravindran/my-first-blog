from django.shortcuts import render
from .models import Post

# Create your views here.
from django.http import HttpResponse

def home(request):
	posts=Post.objects.all()
#	post_title=list()
	
#	for post in posts:
#		post_title.append(post.title)
		
#	response_html = '<br>'.join(post_title)
	
#	return HttpResponse(response_html)
	return render(request,'home.html',{'posts':posts})