# -*- coding: utf-8 -*-
"""NLP_basic_preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZbpKxJUJdG6jVbuQrmM8LEm_fNXqzyqu
"""

#import NLP libries 
import re
import nltk
import string
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

np.random.seed(2018)
import string

#convert to lowercase, strip and remove punctuations
def preprocess(text):
    text = text.lower() 
    text=text.strip()  
    text=re.compile('<.*?>').sub('', text)
    text=re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+').sub('', text) 
    text=re.compile('((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}').sub('', text)
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'\[[0-9]*\]',' ',text)
    #text = re.sub(r'\b\w\b', '',text)
    text=re.sub(r'[^\w\s]', '', str(text).lower().strip())
    #text = re.sub(r'\d',' ',text) 
    text = re.sub(r'\s+',' ',text)
   
    
    return text


# STOPWORD REMOVAL
def stopword(string):
    a= [i for i in string.split() if i not in stopwords.words('english')]
    return ' '.join(a)

#remove accented characters
def remove_accented_chars(text):
    """remove accented characters from text, e.g. café"""
    text = unidecode.unidecode(text)
    return text


#remove single character
def single_characters(text):
    text = re.sub(r'\b\w\b', '',text)
    return text

# function to convert numbers to words
def num_to_words(text):
    """
    Return :- text which have all numbers or integers in the form of words
    Input :- string
    Output :- string
    """
    # splitting text into words with space
    after_spliting = text.split()

    for index in range(len(after_spliting)):
        if after_spliting[index].isdigit():
            after_spliting[index] = num2words(after_spliting[index])

    # joining list into string with space
    numbers_to_words = ' '.join(after_spliting)
    return numbers_to_words


## Remove single characters

def remove_single_char(text):
    """
    Return :- string after removing single characters
    
    """
    single_char_pattern = r'\s+[a-zA-Z]\s+'
    without_sc = re.sub(pattern=single_char_pattern, repl=" ", string=text)
    return without_sc

from collections import Counter
 
def remov_duplicates(input):
 
    # split input string separated by space
    input = input.split(" ")
 
    # joins two adjacent elements in iterable way
    for i in range(0, len(input)):
        input[i] = "".join(input[i])
 
    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    UniqW = Counter(input)
 
    # joins two adjacent elements in iterable way
    s = " ".join(UniqW.keys())
    return s