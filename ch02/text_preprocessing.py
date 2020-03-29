import numpy as np
from common.util import preprocess

text = "You say goodbye and I say hello"

# 소문자로 변환
text = text.lower()
# 마침표 앞에 공백 삽입
text = text.replace('.',' .')
print(text)

words = text.split(' ')
print(words)

word_to_id = {}
id_to_word = {}

for word in words:
    if word not in word_to_id:
        new_id = len(word_to_id)
        word_to_id[word] = new_id
        id_to_word[new_id] = word

print(id_to_word)
print(word_to_id)

print(id_to_word[1])
print(word_to_id['hello'])

corpus = [word_to_id[w] for w in words]
corpus = np.array(corpus)
print(corpus)



# 함수로 구현


text = "You say goodbye and I ay hello"
corpus, word_to_id, id_to_word = preprocess(text)
print("corpus : " + str(corpus))
print("word_to_id : " + str(word_to_id))
print("id_to_word : " + str(id_to_word))
