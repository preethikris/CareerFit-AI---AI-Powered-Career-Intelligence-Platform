import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# -----------------------------------
# Initialize NLP Tools
# -----------------------------------

stop_words = set(stopwords.words('english'))

lemmatizer = WordNetLemmatizer()


# -----------------------------------
# Text Cleaning Function
# -----------------------------------

def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()


    # Remove numbers
    text = re.sub(r'\d+', '', text)


    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)


    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()


    # Tokenization
    tokens = word_tokenize(text)


    # Remove stopwords + lemmatization
    cleaned_tokens = []

    for word in tokens:

        if word not in stop_words:

            lemma_word = lemmatizer.lemmatize(word)

            cleaned_tokens.append(lemma_word)


    # Join words again
    cleaned_text = " ".join(cleaned_tokens)

    return cleaned_text