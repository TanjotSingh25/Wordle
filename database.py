class database:
    def __init__(self, word_length, file):
        self.database = self.make_database(file)
        self.word_length = word_length

    def make_database(self, file):
        word_file = open(file)
        data = make_hash_table()
        for word in word_file:
            hash(data, word)
        return data

    def make_hash_table(self):
        hash_table = []
        for i in range(0, 26*26*26):
            hash_table.append([])
        return hash_table

    # Creating function that hashes each string based of first 3 characters of that word
    def hash_number(word):
        # convert char to ascii value
        c = ord(word[0]) + ord(word[1]) + ord(word[2])
        return c
    
    def hash(data, word):
        h = hash_number(word)
        data[h].append(word)
    
    def add_word(self, word):
        h = hash_number(word)
        self.database[h].append(word)


