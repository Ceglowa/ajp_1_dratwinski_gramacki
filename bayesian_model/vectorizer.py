from typing import Tuple, List, Union, Callable

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import numpy as np
import os
import pickle as pkl

from sklearn.preprocessing import LabelEncoder

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


def get_vectorized_data(tagger_name: str, rules: List):
    train_words, train_labels, test_words, test_labels = read_pickled_data(PATH_TO_PICKLES + os.path.sep + f"{tagger_name}.pkl")
    train_lic_idx = train_labels.index("license.xml")
    test_lic_idx = test_labels.index("license.xml")

    train_words.pop(train_lic_idx)
    train_labels.pop(train_lic_idx)

    test_words.pop(test_lic_idx)
    test_labels.pop(test_lic_idx)

    train_words_filtered_POS = extract_words_based_on_rules(train_words, rules)
    test_words_filtered_POS = extract_words_based_on_rules(test_words, rules)

    vectorizer = CountVectorizer()
    encoder = LabelEncoder()

    train_words_filtered_POS = [' '.join(x) for x in train_words_filtered_POS]
    test_words_filtered_POS = [' '.join(x) for x in test_words_filtered_POS]

    X_train = vectorizer.fit_transform(train_words_filtered_POS).toarray()
    X_test = vectorizer.transform(test_words_filtered_POS).toarray()

    y_train = encoder.fit_transform(train_labels)
    y_test = encoder.transform(test_labels)

    return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test), encoder.classes_


if __name__ == '__main__':
    nouns_rules = [lambda tag: tag.startswith("subst"),
                   lambda tag: tag.startswith("depr"),
                   lambda tag: tag.startswith("ger")]

    verb_rules = [lambda tag: tag.startswith("fin"),
                  lambda tag: tag.startswith("praet"),
                  lambda tag: tag.startswith("impt"),
                  lambda tag: tag.startswith("imps"),
                  lambda tag: tag.startswith("inf")]

    adj_rules = [lambda tag: tag.startswith("adj"),
                 lambda tag: tag.startswith("adja"),
                 lambda tag: tag.startswith("adjp"),
                 lambda tag: tag.startswith("adjc"),
                 lambda tag: tag.startswith("pact"),
                 lambda tag: tag.startswith("ppas")]



    for tagger in ['krnnt', 'morpho', 'wcrft2']:
        X_train, y_train, X_test, y_test, labels = get_vectorized_data(tagger, nouns_rules)

        print("got data")

        clf = MultinomialNB()
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)

        with open(f"nouns_{tagger}.txt", 'w') as f:
            print(classification_report(y_true=y_test, y_pred=y_pred, labels=labels), file=f)
