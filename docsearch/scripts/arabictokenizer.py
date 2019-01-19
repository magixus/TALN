import nltk
from re import sub
TBWTokenizer = nltk.tokenize.TreebankWordTokenizer()
from django.conf import settings
from os.path import join

mypath = join(settings.BASE_DIR, 'static/nltk_data')

stp1 = join(mypath,"corpora/stopwords/arabic")
stp2 = join(mypath,"corpora/stopwords/arabic2")
# read input file and return it string
def load(fileName):
    f = open(fileName, 'r', encoding="utf-8")
    str = f.read()
    f.close()
    return str

def arabicTokenize(fileName):
    # get the fileName's text
    file_text = load(fileName)

    # get all words form that text
    list_words= TBWTokenizer.tokenize(sub(r"[،.؟!]*","",file_text))

    # get all stop words
    stpwords1 = load(stp1).split('\n')
    stpwords2 = load(stp2).split('\n')

    # merge stop words to one list
    stpwords = set(stpwords1) | set(stpwords2)

    # return on a list all pure words.
    return [w for w in list_words if w not in stpwords]