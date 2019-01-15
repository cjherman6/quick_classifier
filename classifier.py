from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import GradientBoostingClassifier

clf = DecisionTreeClassifier()
svc = LinearSVC()
sgd = SGDClassifier()
gdb = GradientBoostingClassifier()
models = [clf,svc,sgd,gdb]

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

def fit_predict(model):
    model = model.fit(X, Y)
    return model.predict([[190, 70, 43]])

predictions = []
for model in models:
    mod_pred = fit_predict(model)
    model_name = type(model).__name__
    predictions.append((model_name,mod_pred[0]))

if __name__ == "__main__":
    print(predictions)
