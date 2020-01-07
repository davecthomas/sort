from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

class FileMetadata:
    def __init__(self, filename):
        self.filename = filename
        self.lemma_list = []



class InvertedIndex:
    def __init__(self, list_files, test=True):
        nltk.download('wordnet')
        nltk.download('stopwords')
        # Format of index: {word_lemma: {"count": count, "file_meta_list": [file_meta, ...]}
        self.inverted_index = {}

        # self.stemmer=LancasterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = stopwords.words('english')
        self.file_meta_list = []
        for file_to_index in list_files:
            file_meta = FileMetadata(file_to_index)
            self.file_meta_list.append(file_meta)
            lemma_list = []
            with open(file_to_index) as f:
                for line in f:
                    wordlist = line.lower().split()
                    # get the lemma from the word, store it in the set
                    for word in wordlist:
                        # word_stem = self.stemmer.stem(word)
                        if word not in self.stopwords:
                            word = word.rstrip('?:!.,;()')
                            word_lemma = self.lemmatizer.lemmatize(word)
                            lemma_list.append(word_lemma)
                            if word_lemma in self.inverted_index:
                                self.inverted_index[word_lemma]["count"] += 1
                                self.inverted_index[word_lemma]["file_meta_list"].append(file_meta)
                                # if test:
                                #     print(f'Found {word_lemma} in {file_to_index}'
                                #           f' {self.inverted_index[word_lemma]["count"]} times')
                            else:
                                self.inverted_index[word_lemma] = {}
                                self.inverted_index[word_lemma]["count"] = 1
                                self.inverted_index[word_lemma]["file_meta_list"] = [file_meta]
                            # if test:
                            #     print(f'{word_lemma}')
            file_meta.lemma_list = lemma_list
            if test:
                for key, value in self.inverted_index.items():
                    if value["count"] > 1:
                        print(f'{key}: {value["count"]}')