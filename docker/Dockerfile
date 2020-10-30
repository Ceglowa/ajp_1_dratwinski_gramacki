FROM ubuntu:16.04

RUN apt-get update && apt-get install -y libboost-dev libboost-program-options-dev libboost-filesystem-dev libboost-system-dev libboost-regex-dev libboost-iostreams-dev libicu-dev libxml++2.6-dev bison flex libloki-dev git cmake gcc libedit-dev swig make python-dev 

RUN git clone http://nlp.pwr.wroc.pl/corpus2.git &&  mkdir corpus2/bin 

WORKDIR corpus2/bin

RUN cmake .. && make && make install && ldconfig

RUN echo "dig" >> /usr/local/share/corpus2/nkjp.tagset && echo "romandig" >> /usr/local/share/corpus2/nkjp.tagset

WORKDIR /app

ADD . /app

ENV PYTHONIOENCODING=utf8

ENTRYPOINT ["python2", "tagger-eval.py", "-t", "nkjp", "-s"]

CMD ["submission.xml", "gold-task-c.xml"]
