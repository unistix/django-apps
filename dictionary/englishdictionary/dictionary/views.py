from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.

def index(request):
	return render(request, 'index.html')

def word(request):
	search = request.GET.get('search') #the name assigned to input#
	dictionary = PyDictionary()
	meaning = dictionary.meaning(search)

	try:
		noun = meaning["Noun"][0]
		

	except KeyError:
		noun = "None"
		


	try:
		
		verb = meaning["Verb"][0]
		

	except KeyError:
		
		verb = "None"
		


	try:
	
		adjective = meaning["Adjective"][0]

	except KeyError:
	
		adjective = "None"

	


	context = {
		'meaning': meaning,
		 'noun': noun,
		 'verb': verb,
		 'adjective': adjective
		


	}

	
	return render(request, 'word.html', context)