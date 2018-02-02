from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier

seed = 42

# DATASET
iris = datasets.load_iris()
print("Iris data shape: " + str(iris.data.shape))
X = iris.data[:, :4]
y = iris.target

# print(X)
# print(y)

# Only needed if we don't do k-fold CV
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(y)
encoded_Y = encoder.transform(y) # y_train for manual split...
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

# print(dummy_y)

# TRAINING

def baseline_model():
    model = Sequential()
    model.add(Dense(units=8, input_dim=4, activation='relu'))
    model.add(Dense(units=3, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])
    return model


# model.fit(X_train, dummy_y, epochs=150, batch_size=10)

# EVALUATION
estimator = KerasClassifier(build_fn=baseline_model, epochs=150, batch_size=10, verbose=0)
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))