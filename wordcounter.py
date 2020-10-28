
book_title = ['great', 'great', 'expectation', 'hello', 'hello']
word_counter = {} #creating a dictionary, key and value
for word in book_title:

#   if word not in word_counter:
#        word_counter = 1
#   else:
#      word_counter += 1
#print(word_counter)


    word_counter[word] = word_counter.get(word,0) + 1
print(word_counter)