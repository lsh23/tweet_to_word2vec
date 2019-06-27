# 트위터 파일 한줄한줄씩 읽어서 토크나이징 (" ")하고 해당 토큰들이
# wordlist 에 있으면 해당 word에 해당하는 vector를 취하고
# 없으면 다음 토큰으로 넘어가서 그 한 트윗에 대한 vectors를 만들어서
# 한줄로 파일에 저장하면 됨 .

import numpy as np
import pickle

# with open('./word2vec/word_list.pkl', 'rb') as f:
#     word_list = pickle.load(f)
#
# with open('./word2vec/word2vec_vectors.pkl', 'rb') as f:
#     vectors = pickle.load(f)
with open('./word2vec/pretrained_set_dict_word_vector.pkl', 'rb') as f:
    pretrained_set_dict = pickle.load(f)

# print(word_list)
# print(vectors)
tweet_vectors = []

with open('./tweet_parser_result/_FACup/5_5_2012_16_00.txt','r',encoding='utf-8') as tweets:
    for tweet in tweets:
        tweet = tweets.readline()
        tweet_words = tweet.strip().split(" ");
        for word in tweet_words:
            tweet_vector = tuple()
            word = word.strip(".")
            if(word in pretrained_set_dict):
                tweet_vector += pretrained_set_dict[word]
        # if(tweet_vector):
                tweet_vectors.append(tweet_vector)

with open('./word2vec/tweets_word2vec_test.pkl', 'wb') as f:
    pickle.dump(tweet_vectors, f)

print(tweet_vectors)

#     tweets_word2vec_np_vector = np.array(tweet_vectors)
# np.save('./word2vec_result/_FACup/5_5_2012_16_00.txt', tweets_word2vec_np_vector)
