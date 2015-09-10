#!/usr/bin/env python
# -*- coding: utf-8 -*-

word_1 = u"パトカー"
word_2 = u"タクシー"

words_1 = list(word_1)
words_2 = list(word_2)

output = ""
for n in range(0,len(words_2)):
    output = output + words_1[n] + words_2[n]

print output
