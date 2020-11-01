from typing import Tuple, List, Union, Callable

from sklearn.feature_extraction.text import CountVectorizer
import os
import pickle as pkl

PATH_TO_PICKLES = "../data/wikipedia_data"


def read_pickled_data(file: str) -> Tuple[
    List[List[Tuple[str, str]]], List[str], List[List[Tuple[str, str]]], List[str]]:
    with open(file, 'rb') as f:
        data = pkl.load(f)

    train_words_list = data['train_words']
    train_labels_list = data['train_labels']
    test_words_list = data['test_words']
    test_labels_list = data['test_labels']

    return train_words_list, train_labels_list, test_words_list, test_labels_list


def extract_words_based_on_rules(words_list: List[List[Tuple[str, str]]], rules_list: List[Callable]) -> List[
    List[str]]:
    processed_words_list = []
    for words_idx in range(len(words_list)):
        words_for_doc = []
        for word_idx in range(len(words_list[words_idx])):
            if any([rule(words_list[words_idx][word_idx][1]) for rule in rules_list]):
                words_for_doc.append(words_list[words_idx][word_idx][0].lower())
        processed_words_list.append(words_for_doc)

    return processed_words_list


if __name__ == '__main__':
    train_words, train_labels, test_words, test_labels = read_pickled_data(PATH_TO_PICKLES + os.path.sep + "krnnt.pkl")

    nouns_rules_list = [lambda tag: tag.startswith("subst")]

    train_words_only_nouns = extract_words_based_on_rules(train_words, nouns_rules_list)
    test_words_only_nouns = extract_words_based_on_rules(test_words, nouns_rules_list)
    train_vocalbuary = set([train_words_only_nouns[train_words_idx][train_word_idx] for train_words_idx in
                            range(len(train_words_only_nouns)) for train_word_idx in
                            range(len(train_words_only_nouns[train_words_idx]))])
