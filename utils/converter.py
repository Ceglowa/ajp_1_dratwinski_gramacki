from lxml import etree

def convert_krnnt_output_file_to_xml(path_to_file: str, path_to_output_file: str) -> None:
    krnnt_text = open(path_to_file, "r", encoding="utf-8")

    root = etree.Element('chunkList')

    current_chunk_index = 1
    current_chunk = etree.Element('chunk',id=f"{current_chunk_index}", type='p')
    root.append(current_chunk)

    current_sentence_index = 1
    current_sentence = etree.Element('sentence', id=f"{current_sentence_index}")
    current_chunk.append(current_sentence)

    i=0
    for line in krnnt_text:
        line = line.replace("\n", "")
        split = line.split("\t")

        if len(split) ==1 and split[0] == '':
            current_sentence_index += 1
            current_sentence = etree.Element('sentence', id=f"{current_sentence_index}")
            current_chunk.append(current_sentence)
        else:
            if split[0] == '':
                lex = etree.Element('lex', disamb='1')

                base = etree.Element('base')
                base.text = split[1]
                lex.append(base)

                ctag = etree.Element('ctag')
                ctag.text = split[2]
                lex.append(ctag)
                current_tok.append(lex)
                current_sentence.append(current_tok)
            else:
                if split[1] == 'none':
                    current_sentence.append(etree.Element('ns'))

                current_tok = etree.Element('tok')
                orth = etree.Element('orth')
                orth.text = split[0]
                current_tok.append(orth)


    # pretty string
    s = etree.tostring(root, pretty_print=True, encoding='utf8')
    output_file = open(path_to_output_file, "wb")
    output_file.write(s)
    output_file.close()
    return

if __name__ == '__main__':
    convert_krnnt_output_file_to_xml("../data/results_from_taggers/pol_eval_test_raw_krnnt.xml", "../data/results_from_taggers/pol_eval_test_raw_krnnt_processed.xml")