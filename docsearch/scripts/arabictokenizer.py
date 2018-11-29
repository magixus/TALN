from nltk.tokenize import TreebankWordTokenizer
from re import sub


# la fonction qui lit un fichier en entrée
def load(fileName):
    f = open(fileName, 'r', encoding="utf-8")
    str = f.read()
    f.close()
    return str


# récuprer le text du fichier et le stocker dans la variable file_text
file_text = load("1.txt")

list_words= TreebankWordTokenizer().tokenize(sub(r"[،.؟!]*","",file_text))

print(list_words)