import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import csv

ratings = pd.read_csv("gameratings.csv")
test = pd.read_csv("test_esrb.csv")
target_names = pd.read_csv("target_names.csv")
x = ratings[
    [
        "alcohol_reference",
        "animated_blood",
        "blood",
        "blood_and_gore",
        "cartoon_violence",
        "crude_humor",
        "drug_reference",
        "fantasy_violence",
        "intense_violence",
        "language",
        "lyrics",
        "mature_humor",
        "mild_blood",
        "mild_cartoon_violence",
        "mild_fantasy_violence",
        "mild_language",
        "mild_lyrics",
        "mild_suggestive_themes",
        "mild_violence",
        "no_descriptors",
        "nudity",
        "partial_nudity",
        "sexual_content",
        "sexual_themes",
        "simulated_gambling",
        "strong_janguage",
        "strong_sexual_content",
        "suggestive_themes",
        "use_of_alcohol",
        "use_of_drugs_and_alcohol",
        "violence",
    ]
].values
y = ratings[["Target"]].values.reshape(-1, 1)


test_train = test[
    [
        "alcohol_reference",
        "animated_blood",
        "blood",
        "blood_and_gore",
        "cartoon_violence",
        "crude_humor",
        "drug_reference",
        "fantasy_violence",
        "intense_violence",
        "language",
        "lyrics",
        "mature_humor",
        "mild_blood",
        "mild_cartoon_violence",
        "mild_fantasy_violence",
        "mild_language",
        "mild_lyrics",
        "mild_suggestive_themes",
        "mild_violence",
        "no_descriptors",
        "nudity",
        "partial_nudity",
        "sexual_content",
        "sexual_themes",
        "simulated_gambling",
        "strong_janguage",
        "strong_sexual_content",
        "suggestive_themes",
        "use_of_alcohol",
        "use_of_drugs_and_alcohol",
        "violence",
    ]
].values


test_target = test[["Target"]].values.ravel()

games = test[["title"]].values.ravel()



print(x.shape)
print(y.shape)


from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X=x, y=y.ravel())
predicted = knn.predict(X=test_train)
expected = test_target
new2=[]
new3=[]
mydict = {}
with open("target_names.csv", mode="r") as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]: rows[2] for rows in reader}
print(dict_from_csv)
print(dict_from_csv.get('1'))
for i in predicted:
    new2.append(dict_from_csv.get(str(i)))

for i in expected:
    new3.append(dict_from_csv.get(str(i)))
all = []

for i in zip(games,new2,new3):
    all.append(i)




print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('correct guesses %' )
print(format(knn.score(test_train, test_target), ".2%"))
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
wrong = [(g,p,e) for (g,p,e) in zip(games,new2,new3) if p != e]
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
wrongdf = pd.DataFrame(wrong, columns=['title','predicted','expected'])
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('incorrect guesses')

print(wrongdf)

header = ['title','predicted','expected']

with open('gamesoutput.csv','w',newline='') as f:
    writer= csv.writer(f)
    writer.writerow(header)
    writer.writerows(all)
