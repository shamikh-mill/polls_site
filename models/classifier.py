# Import libraries 
from sklearn import svm, datasets 
import pickle 
import numpy as np 
from sklearn.model_selection import cross_val_score

# Load data 
iris = datasets.load_iris()

features = iris.data
labels = iris.target 

# Train SVM classifier on the data 
clf = svm.SVC(kernel='poly', degree=3, C=1.0).fit(features, labels)

# Evaluate 
scores = cross_val_score(clf, features, labels, cv=5)
print (scores)

# Save the trained classifier 
file = open('classifier.pckl', 'wb')
pickle.dump(clf, file)
file.close()
print ('Classifier saved successfully.')