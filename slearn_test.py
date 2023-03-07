from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3)

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("Accuracy: ", accuracy)