import numpy as np
import pickle


if __name__ == "__main__":
    glove_file = "glove_embeddings/glove.6B.100d.txt"
    emb_dict = {}

    with open(glove_file, "r") as glove:
        for line in glove:
            values = line.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            emb_dict[word] = vector

    with open("glove_embeddings/100d_dictionary", "wb") as f:
        pickle.dump(emb_dict, f)
