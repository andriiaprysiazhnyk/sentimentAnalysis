import yaml

from definitions import CONFIG_PATH
from preprocessing.embedding_dictionary_creator import create_dictionary
from preprocessing.validation_data_creator import create_validation_set
from preprocessing.data_cleaner import clean_data
from preprocessing.stemmed_data_creator import create_stemmed_data


if __name__ == "__main__":
    with open(CONFIG_PATH, "r") as config_file:
        config = yaml.full_load(config_file)
        data_path = config["data_path"]
        embeddings_path = config["embeddings_path"]
        cleaned_data_path = config["cleaned_data_path"]
        stemmed_data_path = config["stemmed_data_path"]

    create_dictionary(embeddings_path)
    create_validation_set(data_path)
    clean_data(embeddings_path, data_path, cleaned_data_path)
    create_stemmed_data(cleaned_data_path, stemmed_data_path)
