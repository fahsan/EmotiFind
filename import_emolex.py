# Import default dictionary for dictionary lists, initialize list and dicts. 
from collections import defaultdict
emotion_dict = defaultdict(list)
emolexdatalist= []

# Open and read the EmoLex into a list of lists. 
with open("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", "r") as emolexdata:
    next(emolexdata)
    for row in emolexdata:
        row = row.strip().split("\t")
        emolexdatalist.append(row)
    emolexdata.close()

# For each list in the list of lists 
for line in emolexdatalist:
    # If the word is included in the emotion
    if line[2] == "1":
        # And if the emotion is not a sentiment
        if (line[1] != 'negative') and (line[1] != 'positive'):
            # Add the word to the list of lists
            emotion_dict[line[1]].append(line[0])
        else:
            # Otherwise if it is 0, and if is a sentiment, skip. 
            continue
