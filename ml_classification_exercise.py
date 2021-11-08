from sklearn.datasets import load_iris

iris = load_iris()

from sklearn.model_selection import train_test_split

data_train, data_test, targets_train, targets_test = train_test_split(
    iris.data, iris.target, random_state=11
)
print(data_train.shape)
print(targets_train.shape)
print(data_test.shape)
print(targets_test.shape)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X=data_train, y=targets_train)
predicted = knn.predict(X=data_test)
expected = targets_test

print(predicted[:20])
print(expected[:20])

predicted = [iris.target_names[x] for x in predicted]
expected = [iris.target_names[y] for y in expected]
print(predicted[:20])
print(expected[:20])

wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print(wrong)
print(format(knn.score(data_test, targets_test), ".2%"))
from sklearn.metrics import confusion_matrix

confusion = confusion_matrix(y_true=expected, y_pred=predicted)
print(confusion)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt2

confusion_df = pd.DataFrame(confusion, index=iris.target_names, columns=iris.target_names)
figure = plt2.figure(figsize=(7, 6))
axes = sns.heatmap(confusion_df, annot=True, cmap=plt2.cm.nipy_spectral_r)
plt2.xlabel("expected")
plt2.ylabel('predicted')

plt2.show()
print("done")


# The Iris dataset is referred to as a “toy dataset” because it has only 150 samples and four features.
# The dataset describes 50 samples for each of three Iris flower species—Iris setosa, Iris versicolor and Iris
# virginica. Each sample’s features are the sepal length, sepal width, petal
# length and petal width, all measured in centimeters. The sepals are the larger outer parts of each flower
# that protect the smaller inside petals before the flower buds bloom.

# EXERCISE
# load the iris dataset and use classification
# to see if the expected and predicted species
# match up

# display the shape of the data, target and target_names

# display the first 10 predicted and expected results using
# the species names not the number (using target_names)

# display the values that the model got wrong

# visualize the data using the confusion matrix
