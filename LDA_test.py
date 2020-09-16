import gensim
import numpy as np
from collections import Counter
from sklearn import datasets
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#参考（https://www.sejuku.net/blog/67863）
print("Loading dataset...")
twenty_news = datasets.fetch_20newsgroups(shuffle=True, random_state=1,
                             remove=('headers', 'footers', 'quotes'))


#from(https://gist.github.com/sebleier/554280#file-nltk-s-list-of-english-stopwords)
with open("stop_word.txt") as f:
    stopwords = f.read()
    stopwords = stopwords.split()

docs = data.data
texts = [
    [w for w in doc.lower().split() if w not in stopwords]
        for doc in docs
]

count = Counter(w for doc in texts for w in doc)
count.most_common()[:10]
