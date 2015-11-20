#coding: utf-8

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word = sentence.split(" ")

print word

for i in word:
    if (i[-1]== ',' or i[-1]== '.'):
        print len(i)-1,
    else:
        print len(i),
