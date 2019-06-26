import numpy as np
import struct
import pickle

#tweet_txt 토크나이징 하고
#한 토큰에 대하여
#bin 파일 읽어서 한글자한글자씩 디코드해서 읽은다음
# apple 0.43534
#꼴이니까 공백나올때까지 한글자한글짜씩 읽은다음 토큰과 같으면 해당 실수 vector에 추가
# with open("tweet_parser_result\\_FACup\\5_5_2012_16_00.txt",'r',encoding='utf-8') as tweets:
#     tweet = tweets.readline()
#     print(tweet)
def make_word2vec_set():
    float_size = 4
    words = []
    vectors = []
    with open("GoogleNews-vectors-negative300.bin\\GoogleNews-vectors-negative300.bin",'rb') as file:
        first_line = file.readline().decode('utf-8').strip('\n').split(' ')
        num_words = int(first_line[0])
        vector_size = int(first_line[1])
        # count=0
        for i in range(num_words):
            word = ''
            # count = count + 1
            while True:
                input_c = struct.unpack('c', file.read(1))
                # print(input_c)
                try:
                    input_c = input_c[0].decode('utf-8')
                except UnicodeDecodeError:
                    input_c = input_c[0].decode('latin1')
                    #유니코드처리가 안되는 것들에 대한 처리
                if input_c != ' ':
                    word += input_c
                else:
                    break
            # print(count)
            word = word.lower()
            words.append(word)

            vector = list(struct.unpack('300f', file.read(float_size * vector_size)))
            vectors.append(vector)
            # dummy = file.read(1)
            # print("dummy : ",dummy)

        numpy_vector = np.array(vectors)
        return words, numpy_vector

words, numpy_vector = make_word2vec_set()

with open('./word2vec/word_list.pkl', 'wb') as f:
    pickle.dump(words, f)
np.save('./word2vec/word2vec_vector_not_norm.npy', numpy_vector)

# with open('./word2vec/word_list.pkl', 'rb') as f:
#     words = pickle.load(f)
# words

# numpy_vector = np.load('./word2vec/word2vec_vector_not_norm.npy')
# numpy_vector