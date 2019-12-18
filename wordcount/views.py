from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')

def count(request):
	full_text = request.GET['fulltext']
	wordlist = full_text.split()
	length = len(wordlist)
	word_dict = {}
	for word in wordlist:
		if(word in word_dict):
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	dict_length = len(word_dict)
	# sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':full_text, 'length':length, 'word_dict':word_dict, 'dict_length':dict_length})

def about(request):
	return render(request, 'about.html')