import nltk

# Download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Tokenize a sentence into words
sentence = "The quick brown fox jumps over the lazy dog."
words = nltk.word_tokenize(sentence)
print(words)

# Tag the parts of speech for each word
tags = nltk.pos_tag(words)
print(tags)

# Identify named entities in a sentence
text = "Barack Obama was born in Hawaii."
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tags)
print(entities)