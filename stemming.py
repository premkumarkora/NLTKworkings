from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stop_words  =set(stopwords.words("english"))
#Step 1  -- Tokenize
#tokens = word_tokenize("I am Prem, I am a Data Scientist!")
# Step 2 == Remove Special Chars
tokenizer = RegexpTokenizer(r'\w+')
tokens= tokenizer.tokenize("I am Prem, I am a happiest and promising Data Scientist!")

tok=[]
for token in tokens:
    if token not in stop_words:
        tok.append(token)
print("Removing Stop words", tok)

#Step do Stem Operation
porter = PorterStemmer()
stem_words = []
for token in tok:
    stem_words.append(porter.stem(token))

print(stem_words)