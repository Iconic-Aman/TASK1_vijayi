from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
vectorizer = TfidfVectorizer()
from preprocessing import preprocess_data

import pandas as pd
file_path = "ai_dev_assignment_tickets_complex_1000.xls"
df = pd.read_excel(file_path)

df = preprocess_data(file_path)

def extract_features(df, tfidf):
    X_text = tfidf.fit_transform(df["ticket_text"])
    ticket_len = df["ticket_text"].apply(lambda x: len(x.split())).values.reshape(-1, 1)
    features = np.hstack((X_text.toarray(), ticket_len))
    return features, tfidf


x, y = extract_features(df, vectorizer)

print(x, y)