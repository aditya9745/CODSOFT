from django.shortcuts import render
from random import *

def home(request):
	return render(request, "home.html")


def show(request):
	length=int(request.GET.get("length"))
	pw=""
	text="abcdefghijklmnopqrstuvwxyz"
	
	if request.GET.get("uc"):
		text=text+text.upper()
	if request.GET.get("dg"):
		text=text+"0123456789"
	for i in range(length):
		r = randrange(len(text))
		pw = pw + text[r]
	msg = "Password is " + str(pw)
	return render(request, "show.html", {"msg":msg})

