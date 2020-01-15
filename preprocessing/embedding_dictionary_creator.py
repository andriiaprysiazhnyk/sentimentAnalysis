import os
import numpy as np
import pickle


def create_dictionary(embeddings_path):
    glove_file = os.path.join(embeddings_path, "glove.6B.100d.txt")
    emb_dict = {}

    with open(glove_file, "r") as glove:
        for line in glove:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            emb_dict[word] = vector

    with open(os.path.join(embeddings_path, "100d_dictionary"), "wb") as f:
        pickle.dump(emb_dict, f)
