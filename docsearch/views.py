from django.shortcuts import render
from django.conf.urls.static import static
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from os import listdir
from os.path import join, splitext
import nltk, re, socket

#from docsearch.scripts.staistics import theFirst20Reccurent as theFirst20Reccurent
# added for forms
from operator import itemgetter
from . import forms
from . import forms_add
from .scripts.staistics import theFirst20Reccurent, searchPopUp, validationPopUp, historyAge
from .scripts.worddefinition import kamouss
from .scripts.arabictokenizer import arabicTokenize
from pyquran import strip_tashkeel,strip_tatweel


# insert the path to our directory
mypath = join(settings.BASE_DIR, 'static\\nltk_data')
#nltk.data.path = mypath


def index(request):
    return render(request, "docsearch/index.html")


def documents(request):
    # get files list
    print(nltk.data.path)
    print(nltk.corpus.arabichistory.words())
    file_list = listdir(mypath)
    file_list_title = [l.split('.')[0] for l in file_list]
    #file_list_links = [mypath.join(l) for l in file_list]
    # render this list to view
    return render(request, 'docsearch/mydocuments.html', {'docs': file_list_title})


def statistics(request):
    pathfiles = [mypath + "\\corpora\\acreljahlia\\" +
                 file for file in listdir(mypath + "\\corpora\\acreljahlia")]
    pathfiles = pathfiles + [mypath + "\\corpora\\acrfjrislam\\" +
                             file for file in listdir(mypath + "\\corpora\\acrfjrislam")]
    pathfiles = pathfiles + [mypath + "\\corpora\\acrelhadith\\" +
                             file for file in listdir(mypath + "\\corpora\\acrelhadith")]
    pathfiles = pathfiles + [mypath + "\\corpora\\quoran\\" +
                             file for file in listdir(mypath + "\\corpora\\quoran")]

    Fil = load(join(mypath,listdir(mypath)[1])).split(' ')
    words = nltk.corpus.arabichistory.words()

    str_tab = """<table class="table  table-striped table-borderless"><thead>
                <tr>
                    <th scope="col" class="text-right">الكلمة الأكثر تكرار</th>
                    <th scope="col" class="text-right">عدد الكلمات</th>
                    <th scope="col" class="text-right">النص</th>
                    <th scope="col" class="text-right">العصر /الصنف</th>
                </tr>
            </thead>
            <tbody>"""
    str_s = ''
    nbr = 0
    nbrtext = 0
    for file in pathfiles:
        tmp = splitext(file)[0].split('\\')[-1]
        tmp1 = len(arabicTokenize(file))
        tmp2 = historyAge(splitext(file)[0].split('\\')[-2])
        fd = nltk.FreqDist(arabicTokenize(file))
        tmp3 = fd.most_common(1)
        str_tab = str_tab + f"""
                <tr>
                    <th scope="row" class="text-right">{tmp3[0][0]}</th>
                    <td class="text-right">{tmp1}</td>
                    <td class="text-right">{tmp}</td>
                    <td class="text-right">{tmp2}</td>
                </tr>"""
        nbr += len(arabicTokenize(file))
        nbrtext += 1

    str_tab = str_tab + '</tbody></table>'

    str_s = """
    <div class="row">
        <div class="col-4">
            <h3 class="text-center"></h3>
        </div>
        <div class="col-4">
            <h3>العدد الكلي للكلمات : """
    str_s = str_s + str(nbr) + """</h3>
        </div>
        <div class="col-4">
            <h3>العدد الكلي النصوص : """
    str_s = str_s + str(nbrtext) + """</h3>
        </div>
    </div>"""
    str_s = str_s + """<span class="d-block p-2 bg-success text-white text-right">
                            احصائات عامة حول النصوص         
                        </span>"""

    str_s = str_s + str_tab

    return render(request, 'docsearch/statistics.html', {'str': str_s})


def infos(request):
    return render(request, 'docsearch/about.html')


def editcorpus(request):
    return render(request, 'docsearch/editcorpus.html')

# load a file and return it content


def load(fileName):
    f = open(fileName, 'r', encoding="utf-8")
    str = f.read()
    f.close()
    return str

# show document content on the web


def show_doc(request, doc):
    file = doc+".txt"
    doc_path = join(mypath, file)
    str_doc = load(doc_path)
    return HttpResponse(str_doc)


def searchTags(request):

    # view for forms
    pathfiles = [mypath + "\\corpora\\acreljahlia\\" +
                 file for file in listdir(mypath + "\\corpora\\acreljahlia")]
    pathfiles = pathfiles + [mypath + "\\corpora\\acrfjrislam\\" +
                             file for file in listdir(mypath + "\\corpora\\acrfjrislam")]
    pathfiles = pathfiles + [mypath + "\\corpora\\acrelhadith\\" +
                             file for file in listdir(mypath + "\\corpora\\acrelhadith")]
    pathfiles = pathfiles + [mypath + "\\corpora\\quoran\\" +
                             file for file in listdir(mypath + "\\corpora\\quoran")]
    resultat = ''
    # for file in pathfiles:
    if request.method == 'POST':
        form = forms.FromName(request.POST)
        if form.is_valid():
            searched_tag = form.cleaned_data['tags'] 					# récupérer le mot recherché
            searched_tag =  normalisation_et_nettoyage(searched_tag) 	# normaliser
            if is_connected():										 	# tester si présence de la connexion
	            resultat_c = list(kamouss(searched_tag).keys())[0]
	            resultat_c = list(kamouss(searched_tag).keys())[0].replace(")", "").replace("(", "")
	            resultat = searchPopUp(list(kamouss(searched_tag).keys())[0].replace(")", "").replace("(", ""), list(kamouss(searched_tag).values())[0])
            for file in pathfiles:
                resultat = resultat + '<div class="row m-2 bg-warning justify-content-end">' + \
                    'النص : ' + splitext(file)[0].split('\\')[-1] + '</div>'
                Fil = load(file).split(' ')
                text = nltk.Text(Fil)
                simples = text.concordance_list(searched_tag)
                for i in range(len(simples)):
                    resultat_c = ''.join(simples[i][4]) + '<span style="background-color: #FFFF00">&nbsp;' + join(
                        simples[i][1]) + '&nbsp;</span>' + ''.join(simples[i][5])
                    resultat = resultat + '<div class="row border-bottom justify-content-end">' + \
                        '<p class="text-right">' + resultat_c + '</p>' + '</div>'

    return render(request, "docsearch/searchsection.html", {'searched_tag': resultat})


def addToCorpus(request):
    str_c = ''
    if request.method == 'POST':
        form = forms_add.FromName(request.POST)
        if form.is_valid():
            print('valide')
            tag = form.cleaned_data['tag']
            age = form.cleaned_data['age']
            text = form.cleaned_data['text']
            if age == '1':
                with open(mypath + "\\corpora\\acreljahlia\\" + tag + ".txt", "w", encoding="utf-8") as myfile:
                    myfile.write(text)
                str_c = validationPopUp()
            elif age == '2':
                with open(mypath + "\\corpora\\acrfjrislam\\" + tag + ".txt", "w", encoding="utf-8") as myfile:
                    myfile.write(text)
                str_c = validationPopUp()
            elif age == '3':
                with open(mypath + "\\corpora\\acrelhadith\\" + tag + ".txt", "w", encoding="utf-8") as myfile:
                    myfile.write(text)
                str_c = validationPopUp()
            else:
                with open(mypath + "\\corpora\\quoran\\" + tag + ".txt", "w", encoding="utf-8") as myfile:
                    myfile.write(text)
                str_c = validationPopUp()
        else:
            print('non valide')

    return render(request, "docsearch/editcorpus.html", {'str': str_c})

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

from pyquran import *
def normalisation_et_nettoyage (word):
    text = strip_tashkeel(word)
    text = strip_tatweel(word)
    #text = normalize_hamza(word)
    return text


