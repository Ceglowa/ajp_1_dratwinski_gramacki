import re

def segmentate(text):
    sentences = []

    begin_of_sentence = 0
    end_of_sentence = None

    for index in range(len(text)):
        if begin_of_sentence is None and text[index].isupper():
            begin_of_sentence = index
        elif re.search("[.!?]", text[index]) and index+1<len(text) and text[index+1].isspace():
            sentence = text[begin_of_sentence:index+1]
            last_space = sentence.rfind(" ")
            last_word_in_sentence = sentence[last_space:]
            is_shortcut = re.search("it[pd]|inż|inz|ur", last_word_in_sentence)

            if is_shortcut is None:
                end_of_sentence = index
                sentences.append(text[begin_of_sentence:end_of_sentence+1])

                begin_of_sentence=None


    print(sentences)

    begin_of_word = 0
    end_of_word = None
    words = []

    for sentence in sentences:
        for index in range(len(sentence)):
            if begin_of_word is None:
                if re.search("[0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ]", sentence[index]):
                    begin_of_word = index

            elif not re.search("[0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ]", sentence[index]):

                if not re.search("[0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ][^ ][0-9a-zA-ZąćęńłóśżźĄĆĘŃŁÓŚŻŹ]", sentence[index-1:index+2]):
                    word = sentence[begin_of_word:index]

                    end_of_word = index
                    words.append(word)

                    begin_of_word=None

    print(words)

if __name__ == '__main__':
    file_name = "data/train/Katolicyzm_2850522.txt"
    f = open(file_name, "r",encoding="utf-8")
    segmentate(f.read())

