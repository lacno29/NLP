import os

class Preprocessor:
    _sentences = []
    
    def __init__(self, input_filename, output_filename):
        self._deleteFile(output_filename)

        with open(input_filename) as input_file:
            split_words_per_sentence = self._splitWordsFromEverySentenceIn(input_file)
            print(split_words_per_sentence)
        input_file.close()

        self._sentences = [[self._removeQuotationMarks(word) for word in sentence] for sentence in split_words_per_sentence]
        self._sentences = [self._removeEmptyString(sentence) for sentence in self._sentences]
        print(self._sentences)

    def _deleteFile(self, filename):
        if os.path.isfile(filename) == 1:
            os.remove(filename)

    def _splitWordsFromEverySentenceIn(self, file):
        return [line.split(', ') for line in file.readlines()]

    def _removeEmptyString(self, list_):
        return list(filter(None, list_))

    def _removeQuotationMarks(self, string):
        return string[1:-1]

    def getSentences(self):
        return self._sentences
