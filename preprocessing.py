import re
import nltk
import pandas as pd
import inflect
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('stopwords')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Converting Numerical Values into text using inflect module
p = inflect.engine()
def convert_number(text):
    temp_str = text.split()
    new_string = []
    for word in temp_str:
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
            temp_str = ' '.join(new_string)
    return temp_str

def clean_text(text):
    text = text.lower()
    text = convert_number(text)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def preprocess_data(path):
    df = pd.read_excel(path)
    df.dropna(subset=["ticket_text", "issue_type", "urgency_level"], inplace=True)
    df["cleaned_text"] = df["ticket_text"].apply(clean_text)
    df = df.reset_index(drop=True)
    return df