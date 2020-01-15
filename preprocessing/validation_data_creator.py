import os
import numpy as np


def move_half_files(in_path, out_path):
    files = os.listdir(in_path)
    indices_to_move = np.random.choice(len(files), size=len(files) // 2, replace=False)

    for i in indices_to_move:
        file_name = files[i]

        os.replace(os.path.join(in_path, file_name), os.path.join(out_path, file_name))


def create_validation_set(data_path):
    test_path = os.path.join(data_path, "test")
    validation_path = os.path.join(data_path, "validation")
    positive_instances_path = os.path.join(validation_path, "pos")
    negative_instances_path = os.path.join(validation_path, "neg")

    os.mkdir(validation_path)
    os.mkdir(positive_instances_path)
    os.mkdir(negative_instances_path)

    move_half_files(os.path.join(test_path, "pos"), positive_instances_path)
    move_half_files(os.path.join(test_path, "neg"), negative_instances_path)
