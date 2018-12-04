import nltk
from re import sub
TBWTokenizer = nltk.tokenize.TreebankWordTokenizer()

nltk.data.path = "../../static/nltk_data"

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
    stpwords1 = nltk.corpus.stopwords.words("arabic")
    stpwords2 = nltk.corpus.stopwords.words("arabic2")

    # merge stop words to one list
    stpwords = set(stpwords1) | set(stpwords2)

    # return on a list all pure words.
    return [w for w in list_words if w not in stpwords]


