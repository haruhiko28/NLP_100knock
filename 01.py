import numpy as np

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
    return pato

moji = patotaku(moji)
print('=> '+str(moji))

#================================================================================

print("\n ---02. 「パトカー」＋「タクシー」＝「パタトクカシーー」--- ")

moji1 = 'パトカー'
moji2 = 'タクシー'

def def_02(moji1, moji2):
    _ = []
    #moji1 = moji1.split("")
    #moji2 = moji2.split("")

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
    moji = moji.replace(",","")
    moji = moji.replace(".","")
    moji = moji.split(" ")

    #print(moji)

    list_1 = [1,5,6,7,8,9,15,16,19]
    dic = {}
    for ix, word in enumerate(moji):
        if ix + 1 in list_1:
            #print(ix, word[0])
            dic[word[0]] = ix + 1
        else:
            #print(ix, word[0:2])
            dic[word[0:2]] = ix + 1

    print('=> '+str(dic))

def_04(moji)
#================================================================================
'''
print("\n ---05. n-gram--- ")

def def_05(moji, ):
'''




#================================================================================

print("\n ---07. テンプレートによる文生成--- ")

def def_07(x, y, z):
    return str(x) + '時の' + str(y) +'は' + str(z)

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
    print(''.join(_))

def_08('paraparaparadise')

#================================================================================

print("\n ---09. Typoglycemia--- ")

def def_09():
