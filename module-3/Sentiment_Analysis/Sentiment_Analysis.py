# Load dataset
import pandas as pd
import re
import string
import nltk

nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from bs4 import BeautifulSoup
import contractions

df = pd.read_csv("module-3/Sentiment_Analysis/IMDB-Dataset.csv")

# Remove duplicate rows
df = df.drop_duplicates()


stop = set(stopwords.words("english"))


# Expanding contractions
def expand_contractions(text):
    return contractions.fix(text)


# Function to clean data
def preprocess_text(text):
    wl = WordNetLemmatizer()
    soup = BeautifulSoup(text, "html.parser")  # Removing html tags

    text = soup.get_text()
    text = expand_contractions(text)  # Expanding contractions

    # Removing emojis and special symbols
    emoji_clean = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_clean.sub(r"", text)

    text = re.sub(r"\.(?=\S)", ". ", text)  # Add space after full stop
    text = re.sub(r"http\S+", "", text)  # Remove URLs

    # Remove punctuation, stopwords, and lowercase the text
    text = "".join([word.lower() for word in text if word not in string.punctuation])
    text = " ".join(
        [
            wl.lemmatize(word)
            for word in text.split()
            if word not in stop and word.isalpha()
        ]
    )

    return text


df["review"] = df["review"].apply(preprocess_text)
