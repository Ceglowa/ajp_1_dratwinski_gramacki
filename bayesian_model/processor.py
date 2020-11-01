import os
from lxml import etree
import pickle as pkl

from taggers import get_tagging_from_krnnt, get_tagging_from_morphoDita, get_tagging_from_wcrft2
from utils.converter import convert_krnnt_output_file_to_xml

PATH_TO_RAW_FILES = "../data/wikipedia_data"
MORPHODITA_FOLDER = "morphoDita"
KRNNT_FOLDER = "krnnt"
WCRFT2_FOLDER = "wcrft2"


def process_training_data_to_xmls(path_to_data: str):
    training_data_files = os.listdir(path_to_data + os.path.sep + 'train')
    path_to_processed_train_files = PATH_TO_RAW_FILES + os.path.sep + "processed_train"

    for training_data_file in training_data_files:
        if training_data_file.endswith(".txt") and not os.path.isfile(
                path_to_processed_train_files + os.path.sep + WCRFT2_FOLDER + os.path.sep +
                training_data_file.split(".")[:-1][0] + ".xml"):
            text = open(PATH_TO_RAW_FILES + os.path.sep + "train" + os.path.sep + training_data_file, "r",
                        encoding="utf-8").read()
            get_tagging_from_krnnt(text, path_to_processed_train_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                   training_data_file.split(".")[:-1][0] + ".xml")

            convert_krnnt_output_file_to_xml(path_to_processed_train_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                             training_data_file.split(".")[:-1][0] + ".xml",
                                             path_to_processed_train_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                             training_data_file.split(".")[:-1][0] + ".xml"
                                             )

            get_tagging_from_morphoDita(text,
                                        path_to_processed_train_files + os.path.sep + MORPHODITA_FOLDER + os.path.sep +
                                        training_data_file.split(".")[:-1][0] + ".xml")
            get_tagging_from_wcrft2(text, path_to_processed_train_files + os.path.sep + WCRFT2_FOLDER + os.path.sep +
                                    training_data_file.split(".")[:-1][0] + ".xml")


def process_testing_data_to_xmls(path_to_data: str):
    test_data_files = os.listdir(path_to_data + os.path.sep + 'test')
    path_to_processed_test_files = PATH_TO_RAW_FILES + os.path.sep + "processed_test"

    for test_data_file in test_data_files:
        if test_data_file.endswith(".txt") and not os.path.isfile(
                path_to_processed_test_files + os.path.sep + WCRFT2_FOLDER + os.path.sep +
                test_data_file.split(".")[:-1][0] + ".xml"):
            text = open(PATH_TO_RAW_FILES + os.path.sep + "test" + os.path.sep + test_data_file, "r",
                        encoding="utf-8").read()
            get_tagging_from_krnnt(text, path_to_processed_test_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                   test_data_file.split(".")[:-1][0] + ".xml")

            convert_krnnt_output_file_to_xml(path_to_processed_test_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                             test_data_file.split(".")[:-1][0] + ".xml",
                                             path_to_processed_test_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                             test_data_file.split(".")[:-1][0] + ".xml"
                                             )

            get_tagging_from_morphoDita(text,
                                        path_to_processed_test_files + os.path.sep + MORPHODITA_FOLDER + os.path.sep +
                                        test_data_file.split(".")[:-1][0] + ".xml")
            get_tagging_from_wcrft2(text, path_to_processed_test_files + os.path.sep + WCRFT2_FOLDER + os.path.sep +
                                    test_data_file.split(".")[:-1][0] + ".xml")


def read_training_data(path_to_data: str, tagger_folder: str):
    training_data_files = os.listdir(path_to_data + os.path.sep + 'processed_train' + os.path.sep + tagger_folder)

    train_words = []
    train_labels = []

    for training_file in training_data_files:
        print(f"{tagger_folder}, {training_file}")
        xml_text = open(
            path_to_data + os.path.sep + 'processed_train' + os.path.sep + tagger_folder + os.path.sep + training_file,
            "rb").read()
        root = etree.fromstring(xml_text)

        words_with_tags = []
        number_of_chunks = len(root)
        for chunk_index in range(number_of_chunks):
            chunk = root[chunk_index]
            number_of_sentences = len(chunk)
            for sentence_index in range(number_of_sentences):
                sentence = chunk[sentence_index]
                number_of_tokens = len(sentence)
                for token_index in range(number_of_tokens):
                    if sentence[token_index].tag != 'ns':
                        words_with_tags.append((sentence[token_index][1][0].text, sentence[token_index][1][1].text))
        train_words.append(words_with_tags)
        train_labels.append(training_file.split("_")[0])

    return train_words, train_labels


def read_testing_data(path_to_data: str, tagger_folder: str):
    test_data_files = os.listdir(path_to_data + os.path.sep + 'processed_test' + os.path.sep + tagger_folder)

    test_words = []
    test_labels = []

    for test_file in test_data_files:
        print(f"{tagger_folder}, {test_file}")
        xml_text = open(
            path_to_data + os.path.sep + 'processed_test' + os.path.sep + tagger_folder + os.path.sep + test_file,
            "rb").read()
        root = etree.fromstring(xml_text)

        words_with_tags = []
        number_of_chunks = len(root)
        for chunk_index in range(number_of_chunks):
            chunk = root[chunk_index]
            number_of_sentences = len(chunk)
            for sentence_index in range(number_of_sentences):
                sentence = chunk[sentence_index]
                number_of_tokens = len(sentence)
                for token_index in range(number_of_tokens):
                    if sentence[token_index].tag != 'ns':
                        words_with_tags.append((sentence[token_index][1][0].text, sentence[token_index][1][1].text))
        test_words.append(words_with_tags)
        test_labels.append(test_file.split("_")[0])

    return test_words, test_labels


if __name__ == '__main__':
    train_words_morpho, train_labels_morpho = read_training_data(PATH_TO_RAW_FILES, "morphoDita")
    train_words_wcrft2, train_labels_wcrft2 = read_training_data(PATH_TO_RAW_FILES, "wcrft2")
    train_words_krnnt, train_labels_krnnt = read_training_data(PATH_TO_RAW_FILES, "krnnt")

    test_words_morpho, test_labels_morpho = read_testing_data(PATH_TO_RAW_FILES, "morphoDita")
    test_words_wcrft2, test_labels_wcrft2 = read_testing_data(PATH_TO_RAW_FILES, "wcrft2")
    test_words_krnnt, test_labels_krnnt = read_testing_data(PATH_TO_RAW_FILES, "krnnt")

    with open('../data/wikipedia_data/morpho.pkl', 'wb') as f:
        pkl.dump({"train_words": train_words_morpho, "train_labels": train_labels_morpho,
                  "test_words": test_words_morpho, "test_labels": test_labels_morpho}, f)

    with open('../data/wikipedia_data/krnnt.pkl', 'wb') as f:
        pkl.dump({"train_words": train_words_krnnt, "train_labels": train_labels_krnnt,
                  "test_words": test_words_krnnt, "test_labels": test_labels_krnnt}, f)

    with open('../data/wikipedia_data/wcrft2.pkl', 'wb') as f:
        pkl.dump({"train_words": train_words_wcrft2, "train_labels": train_labels_wcrft2,
                  "test_words": test_words_wcrft2, "test_labels": test_labels_wcrft2}, f)
