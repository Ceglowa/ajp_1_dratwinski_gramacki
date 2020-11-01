import re
import json

def segmentate(file_name):


    text = open(file_name, "r",encoding="utf-8").read()

    sentences = []
    begin_of_sentence = 0


    for index in range(len(text)):
        if begin_of_sentence is None and text[index].isupper():
            begin_of_sentence = index
        elif re.search("[.!?]", text[index]) and index+1<len(text) and text[index+1].isspace():
            sentence = text[begin_of_sentence:index+1]
            last_space = sentence.rfind(" ")
            last_word_in_sentence = sentence[last_space:]
            is_shortcut = re.search("it[pd]|inż|inz|ur|zm", last_word_in_sentence)

            if is_shortcut is None:
                sentences.append({"text":text[begin_of_sentence:index+1]})

                begin_of_sentence=None

    begin_of_word = 0
    for sen_index in range(len(sentences)):
        sentence = sentences[sen_index]['text']
        words_for_sentence = []
        for index in range(len(sentence)):
            if begin_of_word is None:
                if re.search("[0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ]", sentence[index]):
                    begin_of_word = index

            elif not re.search("[0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ]", sentence[index]):

                if not re.search("[0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ][^ ][0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ]", sentence[index-1:index+2]):
                    word = sentence[begin_of_word:index]
                    words_for_sentence.append(word)
                    begin_of_word=None
        sentences[sen_index]['words'] = words_for_sentence

    with open('segmented_text.json', 'w') as fout:
        json.dump(sentences, fout, ensure_ascii=False)

if __name__ == '__main__':
    file_name = "data/for_report.txt"
    segmentate(file_name)

