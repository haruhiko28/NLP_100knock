import re
import random

#================================================================================

print("\n --- 00. 文字列の逆順 --- ")
moji = 'stressed'
print(moji)

def rev_func(moji):
    moji = moji[::-1]
    return moji

moji = rev_func(moji)
print('=> '+str(moji))

#================================================================================

print("\n ---01. 「パタトクカシーー」--- ")
moji = 'パタトクカシーー'
print(moji)

def patotaku(moji):
    pato = []
    for i in [1,3,5,7]:
        pato.append(moji[i])
    return ''.join(pato)

moji = patotaku(moji)
print('=> '+str(moji))

#================================================================================

print("\n ---02. 「パトカー」＋「タクシー」＝「パタトクカシーー」--- ")

moji1 = 'パトカー'
moji2 = 'タクシー'

def def_02(moji1, moji2):
    _ = []

    for (a, b) in zip(moji1, moji2):
        _.append(a)
        _.append(b)
    _ = ''.join(_)
    print('=> '+str(_))

def_02(moji1, moji2)

#================================================================================

print("\n ---03. 円周率--- ")
moji = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

def str_len(moji):
    moji = moji.replace(",","")
    moji = moji.replace(".","")
    moji = moji.split(" ")

    for ix, word in enumerate(moji):
        print('=> '+str(ix), word, len(word))

str_len(moji)

#================================================================================

print("\n ---04. 元素記号--- ")

moji = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

def def_04(moji):
    moji = re.sub('[!@#$_“”¨«»®´·º½¾¿¡§£₤‘’.,]', '', moji)
    moji = moji.split(" ")
    list_1 = [1,5,6,7,8,9,15,16,19]
    dic = {}
    for ix, word in enumerate(moji):
        if ix + 1 in list_1:
            dic[word[0]] = ix + 1
        else:
            dic[word[0:2]] = ix + 1

    print('=> '+str(dic))

def_04(moji)

#================================================================================

print("\n ---05. n-gram--- ")

class N_gram():
    def __init__(self, sentence, n, splitter = "-*-"):
        self.sentence = re.sub('[!@#$_“”¨«»®´·º½¾¿¡§£₤‘’.,]', '', sentence)
        self.n = n
        self.splitter = splitter

    def word(self):
        # make list
        sentence_list = self.sentence.split(" ")

        lst = []
        for i in range(len(sentence_list[:-self.n+1])):
            lst.append(self.splitter.join(sentence_list[i:i+self.n]))

        return lst


    def alpha(self):
        # concat all alphabats
        self.sentence = self.sentence.replace(" ","")

        lst = []
        for i in range(len(self.sentence[:-self.n+1])):
            lst.append(self.splitter.join(self.sentence[i:i+self.n]))

        return lst


a = N_gram("I am an NLPer", 3)

print("I am an NLPer")
print(a.word())
print(a.alpha())

#================================================================================

print("\n ---06. 集合--- ")

b = N_gram("paraparaparadise",2,"-")
c = N_gram("paragraph",2,"-")

b1 = b.alpha()
c1 = c.alpha()

print('積集合' + str(set(b1).intersection(set(c1))))
print('差集合' + str((set(b1).difference(set(c1)))))
print('和集合' + str((set(b1).union(set(c1)))))

if 's-e' in b1:
    print("X has se")

if 's-e' in c1:
    print('Y has se')

#================================================================================

print("\n ---07. テンプレートによる文生成--- ")

def def_07(x, y, z):
    return str(x) + '時の' + str(y) + 'は' + str(z)

moji = def_07(12, '気温', 22.4)
print(moji)

#================================================================================

print("\n ---08. 暗号文--- ")

def def_08(bun):
    _ = []
    for ix, word in enumerate(bun):
        if word.islower():
            _.insert(ix, chr(219-ord(word)))
        else:
            _.insert(ix, word)
    print( '=>' + str(''.join(_)))

print('paraparaparadise')
def_08('paraparaparadise')

#================================================================================

print("\n ---09. Typoglycemia--- ")

def def_09(sentence):
    print(sentence)
    sentence = sentence.split(" ")
    _ = []

    for word in sentence:
        if len(word) > 4:
            word = list(word)

            first = word[0]
            last = word[-1]
            middle = word[1:- 1]

            random.shuffle(middle)
            middle = ''.join(middle)

            word = first + middle + last

        _.append(word)

    _ = ' '.join(_)

    print('=>' + str(_))

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
def_09(sentence)
