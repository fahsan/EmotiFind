# Create lists and import using csv. 
import csv
train_sad = []
train_anger = []
train_joy = []
train_trust = []
train_fear = []
train_surprise = []
train_disgust = []
train_anticipation = []

#Open and import the training set emotions.txt
with open("TrainingSetEmotions.txt", "r") as trainingsetemotions:
    next(trainingsetemotions)
    reader = csv.reader(trainingsetemotions,delimiter='\t')
    for sad,anger,joy,trust,fear,surprise,disgust,anticipation in reader:
        train_sad.append(sad)
        train_anger.append(anger)
        train_joy.append(joy)
        train_trust.append(trust)
        train_fear.append(fear)
        train_surprise.append(surprise)
        train_disgust.append(disgust)
        train_anticipation.append(anticipation)
