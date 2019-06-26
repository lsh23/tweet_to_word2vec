def binary_vector_to_npy():
    float_size = 4
    words = []
    vectors = []
    with open('../word2vec/trunk/vector_tdata10', 'rb') as file:
        first_line = file.readline().decode('utf-8').strip('\n').split(' ')
        num_words = int(first_line[0])
        vector_size = int(first_line[1])

        for i in range(num_words):
            word = ''
            while True:
                input_c = struct.unpack('c', file.read(1))[0].decode('utf-8')
                if input_c != ' ':
                    word += input_c
                else:
                    break
            words.append(word)

            vector = list(struct.unpack('<300f', file.read(float_size * vector_size)))
            vectors.append(vector)
            dummy = file.read(1)

        numpy_vector = np.array(vectors)
        np.save('./word2vec/analogy/word2vec_vector_not_norm.npy', numpy_vector)
    with open('./word2vec/word_list.list', 'w') as wfile:
        for word in words:
            wfile.write(word + '\n')

    return words, numpy_vector