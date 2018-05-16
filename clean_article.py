import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
import string

# Remove named entities
def ne_removal(text):
    tokens = nltk.word_tokenize(text)
    chunked = nltk.ne_chunk(nltk.pos_tag(tokens))
    tokens = [leaf[0] for leaf in chunked if type(leaf) != nltk.Tree]
    return tokens

# Clean article
def clean_article(articleName):
    token_frequency_dic = {}
    with open(articleName,'r') as f:
        text = f.read()
        tokens = ne_removal(text)
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
            token_frequency_dic[str(k)] = v
        return token_frequency_dic

    f.close()
