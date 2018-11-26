from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from os import listdir
from os.path import join


mypath = join(settings.BASE_DIR, 'static/docs')  # insert the path to our directory

def index(request):
    return render(request, "docsearch/index.html")

def documents(request):
    # get files list
    file_list = listdir(mypath)
    file_list_title = [l.split('.')[0] for l in file_list]
    #file_list_links = [mypath.join(l) for l in file_list]
    # render this list to view
    return render(request,'docsearch/mydocuments.html', {'docs': file_list_title})


def statistics(request):
    return render(request,'docsearch/index.html')

def infos(request):
    return render(request, 'docsearch/about.html')

## load a file and return it content
def load(fileName):
    f = open(fileName, 'r', encoding="utf-8")
    str = f.read()
    f.close()
    return str

## show document content on the web
def show_doc(request, doc):
    file = doc+".txt"
    doc_path = join(mypath, file)
    str_doc = load(doc_path)
    return HttpResponse(str_doc)


def searchTags (request, tags):
    return render(request, "docsearch/index.html")