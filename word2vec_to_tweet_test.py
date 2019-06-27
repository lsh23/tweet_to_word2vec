import pickle

with open('./word2vec/tweets_word2vec.pkl', 'rb') as f:
    tweet_vectors = pickle.load(f)

with open('./word2vec/pretrained_set_dict_vector_word.pkl', 'rb') as f:
    pretrained_set_dict_vector_word = pickle.load(f)

    # print(tweet_vectors)

    # pretrained_set_dict_vector_word[tweet_vectors[0]]

    pretrained_set_dict_vector_word[tweet_vectors[0]]
tweets = []
for tweet_vector in tweet_vectors:

    # for one_vector in tweet_vector:
    tweet =""
    if(tweet_vector in pretrained_set_dict_vector_word):
            tweet += pretrained_set_dict_vector_word[tweet_vector]

    tweets.append(tweet)

print(tweets)

# with open('./tweet_parser_result/_FACup/5_5_2012_16_00.txt','r',encoding='utf-8') as tweets:
#     for tweet in tweets:
#         tweet = tweets.readline()
#         tweet_words = tweet.strip().split(" ");
#         for word in tweet_words:
#             tweet_vector = []
#             word = word.strip(".")
#             if(word in pretrained_set_dict):
#                 tweet_vector += pretrained_set_dict[word]
#                 tweet_vectors.append(tweet_vector)
