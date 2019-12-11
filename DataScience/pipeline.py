from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#making the pipe line
pipe=make_pipeline(
    StandardScaler(),
    LogisticRegression()
)


#loading the dataset
X,y=load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


#traing the pipeline
pipe.fit(X_train,y_train)
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression(random_state=0))])


#scoring the pipeline
result=accuracy_score(pipe.predict(X_test), y_test)
print(result)