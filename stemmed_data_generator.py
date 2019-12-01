import os
from nltk.stem import PorterStemmer


def process_folder(in_path, out_path, stemmer):
    for target_class_name in os.listdir(in_path):
        target_class_in_path = os.path.join(in_path, target_class_name)
        target_class_out_path = os.path.join(out_path, target_class_name)
        os.mkdir(target_class_out_path)

        for file_name in os.listdir(target_class_in_path):
            with open(os.path.join(target_class_in_path, file_name), "r") as instance_file:
                words = instance_file.read().split()

            stemmed_content = " ".join(list(map(lambda x: stemmer.stem(x), words)))

            with open(os.path.join(target_class_out_path, file_name), "w") as instance_file:
                instance_file.write(stemmed_content)


if __name__ == "__main__":
    input_path = os.path.join(os.path.curdir, "cleaned_data")
    output_path = os.path.join(os.path.curdir, "stemmed_data")

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    stemmer = PorterStemmer()
    for folder in os.listdir(input_path):
        cur_path = os.path.join(output_path, folder)
        os.mkdir(cur_path)

        process_folder(os.path.join(input_path, folder), cur_path, stemmer)
