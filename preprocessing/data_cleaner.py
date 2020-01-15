import os
import re
import pickle


def clean(text):
    # lowercase all characters
    text = text.lower()

    # remove html markup
    text = re.sub("(<.*?>)", "", text)

    # remove non-ascii and digits
    text = re.sub("(\\W|\\d)", " ", text)

    # remove whitespace
    return text.strip()


def process_folder(in_path, out_path, vocab):
    for target_class_name in ["pos", "neg"]:
        target_class_in_path = os.path.join(in_path, target_class_name)
        target_class_out_path = os.path.join(out_path, target_class_name)
        os.mkdir(target_class_out_path)

        for file_name in os.listdir(target_class_in_path):
            with open(os.path.join(target_class_in_path, file_name), "r") as instance_file:
                content = instance_file.read()

            words = clean(content).split()
            cleaned_content = " ".join(list(filter(lambda x: x in vocab, words)))

            with open(os.path.join(target_class_out_path, file_name), "w") as instance_file:
                instance_file.write(cleaned_content)


def clean_data(embeddings_path, data_path, cleaned_data_path):
    with open(os.path.join(embeddings_path, "100d_dictionary"), "rb") as f:
        vocab = pickle.load(f)

    if not os.path.exists(cleaned_data_path):
        os.mkdir(cleaned_data_path)

    for folder in os.listdir(data_path):
        if os.path.isdir(os.path.join(data_path, folder)):
            cur_path = os.path.join(cleaned_data_path, folder)
            os.mkdir(cur_path)

            process_folder(os.path.join(data_path, folder), cur_path, vocab)
