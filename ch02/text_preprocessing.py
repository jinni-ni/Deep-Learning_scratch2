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


text = "You say goodbye and I say hello"
corpus, word_to_id, id_to_word = preprocess(text)
print("corpus : " + str(corpus))
print("word_to_id : " + str(word_to_id))
print("id_to_word : " + str(id_to_word))

print("#######################################")
c = np.array([
    #you 옆에 say
    [0,1,0,0,0,0,0],
    [1,0,1,0,1,1,0],
    [0,1,0,1,0,0,0],
    [0,0,1,0,1,0,0],
    [0,1,0,1,0,0,0],
    [0,1,0,0,0,0,1],
    [0,0,0,0,0,1,0]
], dtype=np.int32)

print(c[0])
print(c[4])
print(c[word_to_id['goodbye']])


def create_co_matrix(corpus, vocab_size, window_size=1):
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size+1):
            left_idx = idx - i
            right_idx = idx + i

            if left_idx >= 0:
                left_word_id = corpus[left_idx]
                co_matrix[word_id, left_word_id] += 1

            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                co_matrix[word_id,right_word_id] += 1

    return co_matrix

def cos_similarity(x,y,eps=1e-8):
    # x,y 정규화
    nx = x / np.sqrt(np.sum(x**2) + eps)
    ny = y / np.sqrt(np.sum(y**2)+ eps)

    return np.dot(nx,ny)
