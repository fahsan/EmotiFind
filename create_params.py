import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer 
import string
from collections import defaultdict
emotion_dict = {"sad":["x","y","z"], "fear":["a","b","z","glitter"], "anger":["m","y","suck"]}
token_frequency = {"sucks":1,"x": 2,"y":3,"shine":2,"disco":2}

#part 1 of checking the words in emption_dict
def token_checker_1(emotion_dict, token_frequency):
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



#part 2 of checking the words in the emption_dict
def token_checker_2(token_frequency_present,token_frequency_absent,emotion_dict):
    lemmatizer = WordNetLemmatizer()
    token_frequency_absent_l = {}
    for word in token_frequency_absent: #taking the word sorrow
        word_lemma = lemmatizer.lemmatize(word)
        for word_p in token_frequency_present:
            if word_lemma is word_p:
                token_frequency_present[word_p] = token_frequency_present[word_p] + token_frequency_absent[word]
            else:
                token_frequency_absent_l[word_lemma] = token_frequency_absent[word]

    [token_frequency_present_2,token_frequency_absent_2] = token_checker_1(emotion_dict,token_frequency_absent_l)

    for emotion in token_frequency_present_2:
        if emotion == {}:
            continue
        for word in token_frequency_present_2[emotion]:
            token_frequency_present[emotion][word] = token_frequency_present_2[emotion][word]
    return [token_frequency_present,token_frequency_absent_2]


#part 3 for checking the words in the synonyms:
def token_checker_3(token_frequency_present,token_frequency_absent_2,emotion_dict):    
    for word in token_frequency_absent_2:
        #create a list with all synonyms
        syns = wordnet.synsets(word)
        syns_words = []
        for n in range(len(syns)):
            syns_words.append(syns[n].lemmas()[0].name())
        #print(syns_words)
        # go in each word in syns_words to make comparison
        present = False        
        token_frequency_absent_3 = {}
        for word_s in syns_words:
            if present == True:
                break
                #check if it is token_frequency_present, 
                #if yes update the frequency and exit all the for loops except the first one
            if word_s in token_frequency_present:
                token_frequency_present[word_s] = token_frequency_present[word_s] + token_frequency_absent_2[word]
                present = True
                #print(present)
            else:
                #if is is absent in token_frequency_present, 
                #check emotion dictionary and if it is present exit all except first for
                for emotion in emotion_dict: # going into sad in the emotion dict
                    if word_s in emotion_dict[emotion]: # going into the list of words in sad words
                        token_frequency_present[emotion][word]= token_frequency_absent_2[word]
                        present = True
                        #print("present for", word_s)
        #if it is absent in emotion dictionary, add it to token_frequency_present_3
        if present == False:
            token_frequency_absent_3[word]= token_frequency_absent_2[word]
    return [token_frequency_present, token_frequency_absent_3]

def create_param(token_frequency_present,token_frequency):    
    parameter1 = {}
    for emotion in token_frequency_present:
        parameter1[emotion] = 0
    for emotion in token_frequency_present:
        parameter1[emotion] = sum(token_frequency_present[emotion].values())

    parameter2 = {}
    total_words = sum(token_frequency.values())
    for emotion in parameter1:
        parameter2[emotion] = parameter1[emotion]/total_words    
    return [parameter1, parameter2]
    
def token_checker(emotion_dict,token_frequency):
    [token_frequency_present,token_frequency_absent_1] = token_checker_1(emotion_dict,token_frequency)
    #print("part 1 token_frequency_present is", token_frequency_present)
    #print("part 1 token_frequency_absent is", token_frequency_absent_1)
    [token_frequency_present, token_frequency_absent_2] = token_checker_2(token_frequency_present,token_frequency_absent_1,emotion_dict)
    #print("part 2 token_frequency_present is", token_frequency_present)
    #print("part 2 token_frequency_absent is", token_frequency_absent_2)
    [token_frequency_present, token_frequency_absent_3] = token_checker_3(token_frequency_present,token_frequency_absent_2,emotion_dict)
    #print("part 3 token_frequency_present is", token_frequency_present)
    #print("part 3 token_frequency_absent is", token_frequency_absent_3)
    return create_param(token_frequency_present,token_frequency)
    #print(parameter1)
    #print(parameter2)

