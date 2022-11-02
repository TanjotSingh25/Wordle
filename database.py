class database:
    def __init__(self, file):
        self.database = self.make_database(file)

    def make_database(self, file):
        word_file = open(file)
        data = []
        for word in word_file:
            data.append(word.strip())
        return data

    def add_word(self, word):
        
