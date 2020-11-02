import urllib.parse
from urllib import request
import csv
import gensim
import spacy
from spacy import displacy
import pandas as pd
import gensim
import numpy as np
from collections import Counter
from sklearn import datasets
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from gensim import corpora, models
from janome.tokenizer import Tokenizer
import collections
from sklearn.metrics.pairwise import cosine_similarity
from janome.tokenizer import Tokenizer

#jupyternotebookのコピー
t = Tokenizer()
nlp = spacy.load('ja_ginza')
with open('daigaku3.csv', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    l = [row for row in reader]
docs = [x[1] for x in l]
documents = [x[1] for x in l]
all_documents = ''
for d in documents:
    all_documents += d
counter = collections.Counter(token.base_form for token in t.tokenize(all_documents)
                          if token.part_of_speech.split(',')[0] == '名詞')
bag_of_word = []
remove_list = [')（',')、','ょしらべしょ',')）',')。','大学','学部','大学院','学院','学校','設置','立大','４月','創立','現在','時点','ほか']
keys = [k for k, v in counter.items()]
for k in keys:
    if not str.isdecimal(k) == True:
        if not len(k) == 1:
            if not k in remove_list:
                bag_of_word.append(k)
texts = [
    [w for w in bag_of_word if w in doc]
        for doc in documents
]
dictionary = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
num_topics = 10
 
lda = gensim.models.ldamodel.LdaModel(
    corpus=corpus,
    num_topics=num_topics,
    id2word=dictionary
)
plt.figure(figsize=(30,30))
FONT_FILE = "C:\Windows\Fonts\MSGOTHIC.TTC"
for t in range(lda.num_topics):
    plt.subplot(5,4,t+1)
    x = dict(lda.show_topic(t,200))
    im = WordCloud(font_path=FONT_FILE,collocations=False, regexp=r"[\w']+").generate_from_frequencies(x)
    plt.imshow(im)
    plt.axis("off")
    plt.title("Topic #" + str(t))