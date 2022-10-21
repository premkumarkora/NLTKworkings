import nltk
#nltk.download('punkt') to download punkt
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
stop_words  =set(stopwords.words("english"))
print(stop_words)
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize("DevOps @ too theirs offers a definite career path that promises steady growth. As a DevOps engineer, you will possess extensive knowledge of SDLC and you will know how to juggle coding, integrating, and testing.")
print(tokens)
tok=[]
for token in tokens:
    if token not in stop_words:
        tok.append(token)
print(tok)