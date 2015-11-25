#coding: utf-8

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"

words = sentence.split(" ")
a = [1,5,6,7,8,9,15,16,19]
c = []
for num,word in enumerate(words,start=1):
    if num in a:
        word = word[0]
    else:
        word = word[0:2]
    c.append(word)
print list(enumerate(c,start=1))