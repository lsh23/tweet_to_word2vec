# 트위터 파일 한줄한줄씩 읽어서 토크나이징 (" ")하고 해당 토큰들이
# wordlist 에 있으면 해당 word에 해당하는 vector를 취하고
# 없으면 다음 토큰으로 넘어가서 그 한 트윗에 대한 vectors를 만들어서
# 한줄로 파일에 저장하면 됨 .

import numpy as np
import pickle


with open('./word2vec/pretrained_set_dict/pretrained_set_dict_word_vector.pkl', 'rb') as f:
    pretrained_set_dict = pickle.load(f)


tweet_vectors = []

with open('./tweet_parser_result/_FACup/5_5_2012_16_00.txt','r',encoding='utf-8') as tweets:
    for tweet in tweets:
        tweet = tweets.readline()
        tweet_words = tweet.strip().split(" ");
        for word in tweet_words:
            tweet_vector = np.zeros(300,'float32')
            word = word.strip(".")
            count = 0
            if(word in pretrained_set_dict):
                count = count + 1
                tweet_vector += np.array(pretrained_set_dict[word],'float32')
        if(count):
            mean_of_tweet_vector = tweet_vector / count
            tweet_vectors.append(mean_of_tweet_vector)


with open('./word2vec/tweets_word2vec.pkl', 'wb') as f:
    pickle.dump(tweet_vectors, f)


with open('./word2vec_result/_FACup/5_5_2012_16_00.txt', 'w' ,encoding='utf-8') as f:
    for tweet_vector in tweet_vectors:
        f.write(','.join(str(float) for float in tweet_vector.tolist()))
        f.write("\n")
