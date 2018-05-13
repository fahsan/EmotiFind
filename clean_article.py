import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def clean_article(articleName):
    token_frequency_dic = {}
    with open(articleName,'r') as f:
        text = f.read()

        # split into words
        tokens = word_tokenize(text)

        # convert to lower case
        tokens = [w.lower() for w in tokens]

        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]

        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]

        # filter out stop words and sort
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        words.sort()
        req = nltk.FreqDist(words)
        for k,v in req.items():
            token_frequency_dic[str(k)] = str(v)
        return token_frequency_dic

    f.close()
