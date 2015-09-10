#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = "I am an NLPer"

def n_gram(sequence,n):
    elements = sequence#.split(" ")
    for element_index in xrange(0,len(elements)-n+1):
        yield elements[element_index:element_index+n]
    
#def n_gram_character(sequence,n):


#単語バイグラム
for item in n_gram(sentence.split(),2):
    print item

#文字バイグラム
for item in n_gram(sentence,2):
    print item
