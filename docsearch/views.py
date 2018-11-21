from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from os import listdir
from os.path import join


mypath = join(settings.STATIC_URL, 'docs')  # insert the path to our directory

def index(request):
    return render(request, "docsearch/index.html")

def documents(request):
    # get files list
    #mypath = join(settings.BASE_DIR, 'docs')  # insert the path to our directory
    print(static(mypath))
    file_list = listdir(static(mypath))
    file_list_links = [mypath.join('/'+l) for l in file_list]
    print(file_list)

    # render this list to view
    return render(request,'docsearch/mydocuments.html', {'docs': file_list})


def statistics(request):
    return render(request,'docsearch/index.html')

def infos(request):
    return render(request, 'docsearch/index.html')

## load a file and return it content
def load(fileName):
    f = open(fileName)
    str = f.read()
    f.close()
    return str

## show document content on the web
def show_doc(request, doc):
    doc_path = join(settings.STATIC_URL, join('docs',doc))
    print(doc_path)
    print(doc_path)
    str_doc = load(doc_path)
    return HttpResponse(str_doc)


