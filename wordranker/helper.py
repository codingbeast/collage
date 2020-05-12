from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
from bs4 import BeautifulSoup
import string
import requests
from .models import words
def MyHtml(url):
    response = requests.get(url)
    raw = response.text
    striped_string=MyString(raw)
    return striped_string

def punctuation_removed(data):
    punctuations = list(string.punctuation)
    punctuations.append('’')
    mydata=''.join((x for x in data if x not in punctuations))
    return mydata

def MyString(html):
    soup = BeautifulSoup(html,"lxml")
    for i in soup(['script', 'style']):
        i.decompose()
    return ' '.join(soup.stripped_strings)
def stopwords_removed(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(data)
    words=[i.lower() for i in words]
    mywords=[word for word in words if word not in stop_words]
    mywords=[i for i in mywords if not i.isdigit()]
    return mywords
def freq_counter(data,limit):
    fdist1 = FreqDist(data)
    filtered_word_freq = dict((word, freq) for word, freq in fdist1.items() if not word.isdigit())
    frenq=sorted(filtered_word_freq.items(), key=lambda x: x[1], reverse=True)
    frenqdata=frenq[:limit]
    return frenqdata
def dataisavailable(url):
    flag=words.objects.filter(url=url).exists()
    return flag
def dbinsert(mydict):
    myinst=words()
    myinst.url = mydict['url']
    myinst.word = mydict['word']
    myinst.count = mydict['count']
    try:
        myinst.save()
        return True
    except:
        return False
def CompleteLogic(url):
        myhtml=MyHtml(url=url)
        pdata=punctuation_removed(data=myhtml)
        sdata=stopwords_removed(data=pdata)
        fdata=freq_counter(data=sdata,limit=10)
        return fdata
def getdata(url):
    data=words.objects.filter(url=url)
    return data
