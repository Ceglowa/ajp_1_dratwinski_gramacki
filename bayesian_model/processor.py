import os
from lxml import etree
import pickle as pkl

from taggers import get_tagging_from_krnnt, get_tagging_from_morphoDita, get_tagging_from_wcrft2
from utils.converter import convert_krnnt_output_file_to_xml

PATH_TO_RAW_FILES = "../data/wikipedia_data"
MORPHODITA_FOLDER = "morphoDita"
KRNNT_FOLDER = "krnnt"
WCRFT2_FOLDER = "wcrft2"


def process_data_to_xmls(path_to_data: str, dataset_part: str):
    data_files = os.listdir(path_to_data + os.path.sep + dataset_part)
    path_to_processed_files = PATH_TO_RAW_FILES + os.path.sep + f"processed_{dataset_part}"

    for data_file in data_files:
        if data_file.endswith(".txt") and not os.path.isfile(
                path_to_processed_files + os.path.sep + WCRFT2_FOLDER + os.path.sep +
                data_file.split(".")[:-1][0] + ".xml"):
            text = open(PATH_TO_RAW_FILES + os.path.sep + dataset_part + os.path.sep + data_file, "r",
                        encoding="utf-8").read()
            get_tagging_from_krnnt(text, path_to_processed_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                   data_file.split(".")[:-1][0] + ".xml")

            convert_krnnt_output_file_to_xml(path_to_processed_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                             data_file.split(".")[:-1][0] + ".xml",
                                             path_to_processed_files + os.path.sep + KRNNT_FOLDER + os.path.sep +
                                             data_file.split(".")[:-1][0] + ".xml"
                                             )

            get_tagging_from_morphoDita(text,
                                        path_to_processed_files + os.path.sep + MORPHODITA_FOLDER + os.path.sep +
                                        data_file.split(".")[:-1][0] + ".xml")
            get_tagging_from_wcrft2(text, path_to_processed_files + os.path.sep + WCRFT2_FOLDER + os.path.sep +
                                    data_file.split(".")[:-1][0] + ".xml")



def read_data(path_to_data: str, tagger_folder: str, dataset_part: str):
    data_files = os.listdir(path_to_data + os.path.sep + f'processed_{dataset_part}' + os.path.sep + tagger_folder)

    words = []
    labels = []

    for file in data_files:
        print(f"{tagger_folder}, {file}")
        xml_text = open(
            path_to_data + os.path.sep + f'processed_{dataset_part}' + os.path.sep + tagger_folder + os.path.sep + file,
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
        words.append(words_with_tags)
        labels.append(file.split("_")[0])

    return words, labels

if __name__ == '__main__':
    train_words_morpho, train_labels_morpho = read_data(PATH_TO_RAW_FILES, "morphoDita", "train")
    train_words_wcrft2, train_labels_wcrft2 = read_data(PATH_TO_RAW_FILES, "wcrft2", "train")
    train_words_krnnt, train_labels_krnnt = read_data(PATH_TO_RAW_FILES, "krnnt", "train")

    test_words_morpho, test_labels_morpho = read_data(PATH_TO_RAW_FILES, "morphoDita", "test")
    test_words_wcrft2, test_labels_wcrft2 = read_data(PATH_TO_RAW_FILES, "wcrft2", "test")
    test_words_krnnt, test_labels_krnnt = read_data(PATH_TO_RAW_FILES, "krnnt", "test")

    with open('../data/wikipedia_data/morpho.pkl', 'wb') as f:
        pkl.dump({"train_words": train_words_morpho, "train_labels": train_labels_morpho,
                  "test_words": test_words_morpho, "test_labels": test_labels_morpho}, f)

    with open('../data/wikipedia_data/krnnt.pkl', 'wb') as f:
        pkl.dump({"train_words": train_words_krnnt, "train_labels": train_labels_krnnt,
                  "test_words": test_words_krnnt, "test_labels": test_labels_krnnt}, f)

    with open('../data/wikipedia_data/wcrft2.pkl', 'wb') as f:
        pkl.dump({"train_words": train_words_wcrft2, "train_labels": train_labels_wcrft2,
                  "test_words": test_words_wcrft2, "test_labels": test_labels_wcrft2}, f)
