import os


def load_text_data(path):
    positive_reviews = list(map(lambda z: os.path.join(path, "pos", z), os.listdir(os.path.join(path, "pos"))))
    negative_reviews = list(map(lambda z: os.path.join(path, "neg", z), os.listdir(os.path.join(path, "neg"))))

    x = list(map(lambda z: open(z, "r").read(), positive_reviews)) + \
        list(map(lambda z: open(z, "r").read(), negative_reviews))
    y = [0] * len(positive_reviews) + [1] * len(negative_reviews)

    return x, y
