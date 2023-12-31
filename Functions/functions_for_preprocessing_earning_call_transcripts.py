# -*- coding: utf-8 -*-
"""Functions for Preprocessing Earning Call Transcripts.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bxH1YI43--0M-bk7_gGZGyzzbS2WhGfb
"""

# Commented out IPython magic to ensure Python compatibility.
# Functions for Preprocessing Earning Call Transcripts 1.0
# Author: Yuchen Zhou
# The script contains alll the utility functions for  preprocessing the texts from earning call transcript

import pandas as pd
import numpy as np
import re
import string
import nltk
import spacy
import gensim
import matplotlib.pyplot as plt
import json
import contractions
import spacy_transformers
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
# %matplotlib inline


def load_data (file_name):
  
  """# **1. Initial Preprocessing before Tokenization**

  # 1.1 load_data

  load_data(file_name)

  This function will read the csv file that contains the earning call transcripts and store the data into a Pandas data frame.

  **Parameter**(file_name): the name of the csv file that contains data

  **Return**(raw_earning_call_transcript): the Pandas data frame that stores data
  """
  
  raw_earning_call_transcripts = pd.read_csv(file_name)
  return raw_earning_call_transcripts


def entity_removal(text,nlp):
  
  """# 1.2 entity_removal

  entity_removal(text,nlp)

  This function will take a text and remove entities that are not important for topic modeling (including person, date, moeny, percent, ordinal, cardinal, and time).

  **Parameter**(text): an imput string or text

  **Parameter**(nlp): Spacy's natural language processing model

  **Return**(newString): the new string after removal of unimportant entities
  """
  
  remove_entity_list = ["PERSON","DATE","MONEY","PERCENT","ORDINAL","CARDINAL","TIME"] # entities that will be removed
  doc = nlp(text)
  newString = text
  for e in reversed(doc.ents):
    if e.label_ in remove_entity_list:
      newString = newString[:e.start_char] + newString[e.start_char + len(e.text):] # create a mew string without those entities
  return newString


def split_and_entity_removal(my_dataframe):
  
  """# 1.3 split_and_entity_removal

  split_and_entity_removal(my_dataframe)

  This function will split an earning transcrip into each response (each person's talking) and call functions to remove unimportant entities.

  **Parameter** (my_dataframe): Pandas data frame that contains all earning transcript data

  **Return** (earning_transcripts_name_removed): a list of earning transcripts that were splitted, and unimportant entities were removed from the transcripts
  """
  
  nlp=spacy.load("en_core_web_trf") # load Spacy's model
  earning_transcripts =my_dataframe.content.values.tolist()
  earning_transcripts_remove_operator=[]
  for earning_transcript in earning_transcripts:
     single_transcript=(re.sub('Operator:.*\n', '', earning_transcript))
     single_transcript=re.sub('Operator:.*\Z', '', single_transcript)
     earning_transcripts_remove_operator.extend(single_transcript.split(":")) # split earning transcripts into each response (each person's talking)

  earning_transcripts_name_removed=[]
  for earning_transcript in earning_transcripts_remove_operator:
      earning_transcript=earning_transcript.replace("â"," ") # remove unkown characters
      new_transcript=entity_removal(earning_transcript,nlp) # calling function to remove unimportant entities
      new_transcript=new_transcript.replace("[Operator Instructions]"," ") # remove following words which were not important for topic modeling
      new_transcript=new_transcript.replace("Operator"," ")
      new_transcript=new_transcript.replace("operator"," ")
      new_transcript=new_transcript.replace("Thank"," ")
      new_transcript=new_transcript.replace("Thanks"," ")
      new_transcript=new_transcript.replace("thank"," ")
      new_transcript=new_transcript.replace("thanks"," ")

      if len(new_transcript)<=10: # ignore strings which are short in length after entity removal and splitting
        continue
      else: # add the transcripts after entity removal and splitting into a new list
        earning_transcripts_name_removed.append(new_transcript)
  return earning_transcripts_name_removed


def split_and_expand_contraction(earning_transcripts):
  
  """# 1.4 split_and_expand_contraction

  split_and_expand_contraction(earning_transcripts)

  This function will expand the contractions in the earning transcripts and further split each response(each person's talking) into single sentences

  **Parameter** (earning_transcripts): the output from 1.3

  **Parameter** (earning_transcripts_single_sentence): a list of strings. Each string is a single sentence

  **Return** (earning_transcripts_single_sentence): a list of strings. Each string is a single sentence from earning transcripts
  """
  
  earning_transcripts_single_sentence=[]
  for single_transcript in earning_transcripts:
    single_transcript = contractions.fix(str(single_transcript)) # contractions were expanded
    earning_transcripts_single_sentence.extend(single_transcript.split(".")) # strings were further splitted into single sentences
  return earning_transcripts_single_sentence


def lower_case_and_tokenize(earning_transcripts):
  
  """# **2. Tokenization and Further Preprocessing**

  # 2.1 lower_case_and_tokenize

  lower_case_and_tokenize(earning_transcripts)

  This function will tokenize each sentence from earning transcript and remove punctuations

  **Parameter** (earning_transcripts): the output from 1.4

  **Return** (tokenized_earning_transcripts): A list of sentences which are tokenized (a list of lists of words)
  """
  
  tokenizer = RegexpTokenizer(r'\w+') # set a tokenizer that filters out punctuations
  tokenized_earning_transcripts=[]
  for single_transcript in earning_transcripts:
    single_transcript = single_transcript.lower() # make each sentence into lower case
    single_transcript = tokenizer.tokenize(single_transcript) # tokenize and append into a new list
    tokenized_earning_transcripts.append(single_transcript)
  return tokenized_earning_transcripts


def bigram_trigram(earning_transcripts):
  
  """# 2.2 bigram_trigram

  bigram_trigram(earning_transcripts)

  This function will generate bigram and trigram from tokenized sentences

  **Parameter** (earning_transcripts): tokenized sentences (output from 2.1)

  **Return** (earning_transcripts_trigram): a list of tokenized sentences with bigram and trigram
  """
  
  bigram = gensim.models.Phrases(earning_transcripts, min_count=5, threshold=50) # generate bigram
  trigram = gensim.models.Phrases(bigram[earning_transcripts], threshold=30) # generate trigram
  bigram_mod = gensim.models.phrases.Phraser(bigram)
  trigram_mod = gensim.models.phrases.Phraser(trigram)
  earning_transcripts_trigram=[trigram_mod[bigram_mod[doc]] for doc in earning_transcripts]
  return earning_transcripts_trigram


def filter_noun_only(earning_transcripts):
  
  """# 2.3 filter_noun_only

  filter_noun_only(earning_transcripts)

  This function will remove words that were not Nouns from each sentence

  **Parameter** (earning_transcripts): output from 2.2

  **Return** (earning_transcripts_noun): a list of lists of words that only contain Nouns
  """
  
  tokenizer = RegexpTokenizer(r'\w+')
  earning_transcripts_noun = []
  for earning_transcript in earning_transcripts:
    text=' '.join(earning_transcript).lower()
    tokens = tokenizer.tokenize(text)
    tags = nltk.pos_tag(tokens) # use nltk package's function to identify POS
    new_transcript=[word for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')] # only keep words that are Nouns
    earning_transcripts_noun.append(new_transcript)
  return earning_transcripts_noun


def stopword_removal(earning_transcripts):
  
  """# 2.4 stopword_removal

  stopword_removal(earning_transcripts)

  This function will remove the stop words from each tokenized sentence

  **Parameter** (earning_transcripts): output from 2.3

  **Return** (earning_transcripts_stopword_removal): tokenized sentences with stop words removed
  """
  
  stopwords = nltk.corpus.stopwords.words('english') # a list of stop words from nltk package
  newStopWords = ["right","everyone","hey","sorry","joining_us","thing","term","lot","number","time","way","little_bit","yes","something","anything","couple","one","color","prepared_remarks","my_remarks","unidentified_analyst","talk","congrats","sure","call","question","sort","okay","guess","thought","answer","commentary","please","make_sense","wondering_if","hello","comment","guy","hi","bunch","talk_about","yeah","think","taking_my_question","let_me","kind","sense","versus","hi_good","hey_good","quick_follow_up","appreciate","ask","call","you"] # extra stop words that are manually added
  stopwords.extend(newStopWords)
  earning_transcripts_stopword_removal=[]
  for earning_transcript in earning_transcripts:
    new_transcript=[word for word in earning_transcript if word.lower() not in stopwords]
    earning_transcripts_stopword_removal.append(new_transcript) # stop words are removed
  return earning_transcripts_stopword_removal


def lemmatization(earning_transcripts):
  
  """# 2.5 lemmatization

  lemmatization(earning_transcripts)

  This function will group together the inflected forms of a word so they can be analysed as a single item

  **Parameter** (earning_transcripts): output from 2.4

  **Return** (earning_transcripts_lemmatization): tokenized sentences after lemmatization
  """
  stopwords = nltk.corpus.stopwords.words('english')
  lemm = WordNetLemmatizer() # use lemmatizer from nltk package
  earning_transcripts_lemmatization=[]
  for earning_transcript in earning_transcripts:
    new_transcript=[lemm.lemmatize(word) for word in earning_transcript]
    new_transcript=[word for word in new_transcript if word.lower() not in stopwords]
    earning_transcripts_lemmatization.append(new_transcript) # generate a new list that contains tokenized sentences after lemmatization
  return earning_transcripts_lemmatization


def preprocessing( input_file_name,output_file_name):
  
  """# **3. Main Function**

  # 3.1 Preprocessing

  This is the main function for preprocessing. Call the function to start preprocessing for a single csv file

  **Parameter** (input_file_name): the name of the csv file that contains earning transcripts

  **Parameter** (output_file_name): the name of the csv file that will contain the earning transcripts after preprocessing
  """
  
  earning_transcripts = load_data(input_file_name)
  print("step 1: data loading is completed")
  earning_transcripts_name_removed = split_and_entity_removal(earning_transcripts)
  print("step 2: unrelated entities is removed")
  earning_transcripts_single_sentence = split_and_expand_contraction(earning_transcripts_name_removed)
  print("step 3: earning transcripts are splitted into single sentences")
  tokenized_earning_transcripts = lower_case_and_tokenize(earning_transcripts_single_sentence)
  print("step 4: earning transcripts are tokenized")
  earning_transcripts_bigram_trigram = bigram_trigram(tokenized_earning_transcripts)
  print("step 5: bigram and trigram formations were completed")
  earning_transcripts_noun = filter_noun_only(earning_transcripts_bigram_trigram)
  print("step 6: only nouns were kept in earning transcripts")
  earning_transcripts_stopword_removal = stopword_removal(earning_transcripts_noun)
  print("step 7: stop words were removed from earning transcripts")
  earning_transcripts_lemmatization = lemmatization(earning_transcripts_stopword_removal)
  print("step 8:lemmatization were completed")
  post_processing_earning_transcript=[]
  for earning_transcript in earning_transcripts_lemmatization:
    if len(earning_transcript)>1:
      post_processing_earning_transcript.append(' '.join(earning_transcript))
  df=pd.DataFrame(post_processing_earning_transcript)
  df.to_csv(output_file_name, index=False)
