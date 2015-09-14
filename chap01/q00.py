# coding:utf-8

"""
言語処理100本ノック第１章00
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""


def get_reversed(word):
    return word[::-1]


if __name__ == "__main__":
    word = "stressed"
    print get_reversed(word)

