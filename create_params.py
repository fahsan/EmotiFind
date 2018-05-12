import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
emotion_dict = {"sad":["x","y","z"], "fear":["a","b","z"], "anger":["m","y","suck"]}
token_frequency = {"sucks":1,"x": 2,"y":3,"rock":2}

#part 1 of checking the words in emption_dict
def token_checker(emotion_dict, token_frequency):
    token_frequency_present = {}
    token_frequency_absent = {}
    #creating a blank dictionary for each emotion based on emotion_dict
    for emotion in emotion_dict:
        token_frequency_present[emotion] = {}
        
    for word in token_frequency: #taking the word 
        present = False  #internal check to see if the word is present in any of the emotion dicts
        for emotion in emotion_dict: # going into sad in the emotion dict
            if word in emotion_dict[emotion]: # going into the list of words in sad words
                token_frequency_present[emotion][word]= token_frequency[word]
                present = True #will change if 
        if present == False:
            token_frequency_absent[word]= token_frequency[word]
    return [token_frequency_present,token_frequency_absent]

[token_frequency_present,token_frequency_absent] = token_checker(emotion_dict,token_frequency)
print("part 1 token_frequency_present is", token_frequency_present)
print("part 1 token_frequency_absent is", token_frequency_absent)

#part 2 of checking the words in the emption_dict
token_frequency_absent_2 = {}
for word in token_frequency_absent: #taking the word sorrow
    word_lemma = lemmatizer.lemmatize(word)
    for word_p in token_frequency_present:
        if word_lemma is word_p:
            token_frequency_present[word_p] = token_frequency_present[word_p] + token_frequency_absent[word]
        else:
            token_frequency_absent_2[word_lemma] = token_frequency_absent[word]

token_checker(emotion_dict,token_frequency_absent_2)
print("part 1 token_frequency_present is", token_frequency_present)
print("part 1 token_frequency_absent is", token_frequency_absent)           

#part 3 for checking the words in the synonyms:

for word in token_frequency_absent_2:
    syns = wordnet.synsets(word)
    syns_words = []
    l = len(syns)
    for n in l:
        syns_words.append(syns(n).lemmas()[0].name())
    print(syns_words)
    for word in syns_words:
        present = False  #internal check to see if the word is present in any of the emotion dicts
        for emotion in emotion_dict: # going into sad in the emotion dict
            if word in emotion_dict[emotion]: # going into the list of words in sad words
            token_frequency_present[emotion][word]= token_frequency[word]
            present = True #will change if 
        if present == False:
        token_frequency_absent[word]= token_frequency[word]
        
        
print(syns)
print(syns[2].lemmas()[0])
print(syns[2].lemmas()[0].name())
#take the word, find it's synonym, look the synonym in the emotion_dict,


#for word in token_frequency


    
    
