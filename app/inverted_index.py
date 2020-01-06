from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

class FileMetadata:
    def __init__(self, filename):
        self.filename = filename



class InvertedIndex:
    def __init__(self, list_files):
        nltk.download('wordnet')
        nltk.download('stopwords')

        # self.stemmer=LancasterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = stopwords.words('english')
        for file_to_index in list_files:
            file_meta = FileMetadata(file_to_index)
            with open(file_to_index) as f:
                for line in f:
                    wordlist = line.lower().split()
                    for word in wordlist:
                        # word_stem = self.stemmer.stem(word)
                        if word not in self.stopwords:
                            word_lemma = self.lemmatizer.lemmatize(word)
                            print(f'{word_lemma}')
