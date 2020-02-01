from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import json

# WordInFile represents a single word in a single file (which can happen many times)
# The line numbers are in a set to remove any duplicate words at a given location
class WordInFile:
    def __init__(self, filename, word_lemma, line_number):
        self.filename = filename
        self.word_lemma = word_lemma
        self.locations = set()  # Line locations if found
        self.locations.add(line_number)
        # self.lemma_list = []

    def get_num_times_found(self):
        return len(self.locations)

    def get_top_location(self):
        return min(self.locations)

    def found_again(self, line_number):
        # print(f'{self.word_lemma}: {line_number}')
        self.locations.add(line_number)

    def __str__(self):
        return {"filename": self.filename}

    def __repr__(self):
        return {"filename": self.filename}
    #
    # def to_json(self):
    #     return json.dumps(self, default=lambda o: o.__dict__,
    #                       sort_keys=True, indent=4)



class InvertedIndex:
    # Constructor creates the index
    def __init__(self, list_files, test=False):
        nltk.download('wordnet')
        nltk.download('stopwords')
        # Format of index: {word_lemma: {filename: file_meta, ...}} -- file_metas are sorted by score, after indexing.
        self.inverted_index = {}

        # self.stemmer=LancasterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = stopwords.words('english')
        for file_to_index in list_files:
            lemma_list = []
            with open(file_to_index) as f:
                idx = 0
                for line in f:
                    idx +=1
                    wordlist = line.lower().split()
                    # get the lemma from the word, store it in the set
                    for word in wordlist:
                        # word_stem = self.stemmer.stem(word)
                        if word not in self.stopwords:
                            word = word.rstrip('?:!.,;()')
                            word_lemma = self.lemmatizer.lemmatize(word)
                            # lemma_list.append(word_lemma)
                            if word_lemma in self.inverted_index:
                                lemma_dict = self.inverted_index[word_lemma]
                                if file_to_index in lemma_dict:
                                    word_in_file = lemma_dict[file_to_index]
                                    word_in_file.found_again(idx+1)

                                # if test:
                                #     print(f'Found {word_lemma} in {file_to_index}'
                                #           f' {self.inverted_index[word_lemma]["count"]} times')
                            else:
                                file_meta = WordInFile(file_to_index, word_lemma, idx+1)
                                # self.inverted_index[word_lemma] = {}
                                # self.inverted_index[word_lemma]["count"] = 1
                                self.inverted_index[word_lemma] = {file_to_index: file_meta}
        # Now that we have a dictionary of all the filenames, we need to rebuild the index to be more search friendly
        # by making it a sorted list, with top scoring locations for each word
        self.scored_inverted_index = {}
        list_of_word_in_files = []
        for word, file_dict in self.inverted_index.items():
            for filename, word_in_file in file_dict.items():
                print(f'{filename}')


    def search_index(self, find_me):
        word_lemma = self.lemmatizer.lemmatize(find_me)
        if word_lemma in self.inverted_index:
            return self.inverted_index[word_lemma]
        else:
            return None