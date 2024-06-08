# let’s start by importing all the necessary Python libraries and the dataset we need for this task.
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import re
import nltk
from nltk.corpus import stopwords
import string

# Download stopwords if not already downloaded
nltk.download('stopwords')

stemmer = nltk.SnowballStemmer("english")
stopword = set(stopwords.words('english'))

data = pd.read_csv("twitter.csv")

data["labels"] = data["class"].map({0: "Hate Speech",
                                    1: "Offensive Language",
                                    2: "No Hate and Offensive"})

data = data[["tweet", "labels"]]

def clean(text):
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [stemmer.stem(word) for word in text.split(' ') if word not in stopword]
    return " ".join(text)

data["tweet"] = data["tweet"].apply(clean)

# Now let’s split the dataset into training and test sets
# And train a machine learning model for the task of hate speech detection

x = np.array(data["tweet"])
y = np.array(data["labels"])

cv = CountVectorizer()
X = cv.fit_transform(x)  # Fit the Data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#building the model

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

#Now let’s test this machine learning model to see if it detects hate speech or not And we will call the function
# from the app.py (backend server file)


def model(sample):
    data = cv.transform([sample]).toarray()
    prediction = clf.predict(data)
    print(prediction)
    return prediction




