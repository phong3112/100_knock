#!/usr/bin/env python
# -*- coding: utf-8 -*-

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split(" ")


pi = []
for word in words:
    pi.append(len(word))

print pi

