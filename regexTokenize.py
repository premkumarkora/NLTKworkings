
import nltk
#nltk.download('punkt') to download punkt
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer


tokenizer = RegexpTokenizer(r'\w+')
tokens= tokenizer.tokenize("I am Prem, I am a Data Scientist!")
# removes all the special chars
print (tokens)

