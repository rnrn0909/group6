import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier


def get_dataset():
    feature = []
    title = []
    for i in range(len(nf)): # nf[i][0] = id(auto): must be excluded from features
        co1 = nf[i][-7:7]      # nf[i][1] = time  # nf[i][2] = freq1  # nf[i][3] = freq2  # nf[i][4] = hash  # nf[i][5] = start  # nf[i][6] = stop  # nf[i][7] = title
        feature.append(co1)    # nf[i][-7:4] = t1, f1, f2    # nf[i][-7:7] = t1, f1, f2, hash, start, stop

    for j in range(len(nf)):
        c = nf[j][7]  # title
        enc = c.encode('utf-8')
        co4 = int.from_bytes(enc, 'big')
        title.append(co4)

    idx = []
    for t in title:
        if t not in idx:
             idx.append(t)
    label = []
    for k in range(len(title)):            # k : number of titles in dataset
        for p in range(len(idx)):         # p : number of idx
              if idx[p] == title[k]:
                   label.append(p)

    feature = np.array(feature)

    X = np.array(feature).reshape((len(feature), 6))
    y = np.array(label)      # y is expected to be a sort of label, not an integer, string, or float

    return X, y

def get_model():
     model = KNeighborsClassifier(n_neighbors=1)  # increase of neighbors: underfitting, 모델의 결정 경계가 단순해진다 / decrease of neighbors: overfitting
     return model


def main():
     print(' Start '.center(60, '*'))
     global nf
     f = read_csv('hash.csv', delimiter=',')
     nf = np.array(f)
     X, y = get_dataset()
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=10000)      # used value in example
     cv = KFold(n_splits=10, random_state=1, shuffle=True)
     clf = get_model()
     clf.fit(X_train, y_train)
     prediction = clf.predict(X_test)
     cvscore = cross_val_score(clf, X_test, y_test, scoring='accuracy', cv=cv, n_jobs=-1)
     print(prediction.shape)
     point = clf.score(X_test, y_test)
     print('KNN clf.score = {0:.3f}'.format(point))
     print('CV score = %.3f (%.3f)' % (np.mean(cvscore), np.std(cvscore)))

# test without k fold cv
# n_neighbors = 5: clf.score = 0.799
# n_neighbors = 2: clf.score = 0.819
# n_neighbors = 1: clf.score = 0.842
# n_neighbors = 1 + k fold cv : KNN clf.score = 0.842, CV score = 0.796 (0.001)

if __name__ == "__main__":
    main()


# reference: https://www.analyticsvidhya.com/blog/2018/08/k-nearest-neighbor-introduction-regression-python/
# https://machinelearningmastery.com/how-to-configure-k-fold-cross-validation/