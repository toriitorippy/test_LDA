import gensim
import numpy as np
from collections import Counter
from sklearn import datasets
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

import xml.etree.ElementTree as ET 

# XMLファイルを解析
tree = ET.parse('uwai.xml') 

# # XMLを取得
root = tree.getroot()

node = tree.getroot()
body = node[1][0]

time_list = []
word_list = []

for i in range(len(body[0])):
    if not len(body[0][i]) == 0:
        time_list.append(body[0][i].attrib['source'])
        text  =''
        for child in body[0][i]:
            text += child.text
        word_list.append(text)

with open("character.txt", encoding='utf-8') as f:
    chara = f.read()
    chara = chara.split()

for i in range(len(word_list)):
    doc = nlp(word_list[i]) 
    for ent in doc.ents:
        if ent.label_ == 'Person':
            if not ent.text in chara:
                chara.append(ent.text)

with open("character.txt", mode='w', encoding='utf-8') as f:
    f.write('\n'.join(chara))

#１文字のもの削除
remove_list = []
for i in range(len(chara)):
    if len(chara[i]) == 1:
        remove_list.append(chara[i])
#         chara.remove(chara[i])
#         print(i, chara[i])

for i in range(len(remove_list)):
    chara.remove(remove_list[i])

texts = [
    [w for w in chara if w in doc]
        for doc in word_list
]

dictionary = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

num_tokens = len(count.most_common())
N = int(num_tokens*0.05)
max_frequency = count.most_common()[N][1]
 
corpus = [[w for w in doc if max_frequency > w[1] >= 3] for doc in corpus]

corpus = [[w for w in doc if max_frequency > w[1] >= 3] for doc in corpus]
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

    

