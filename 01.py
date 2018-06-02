
"""問題00:[文字列の逆順]文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．"""
print("Do you input? y or n")
deci = input()
if deci == 'y':
    print('「stressed」と入力してください')
    moji = input()
elif deci == "n":
    moji = 'stressed'

def rev_func(moji):
    moji = moji[::-1]
    return moji

moji = rev_func(moji)
print(moji)

"""================================================================================"""

"""問題01. 「パタトクカシーー」「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．"""
print("Do you input? y or n")
deci = input()

if deci == 'y':
    print('「パタトクカシーー」と入力してください')
    moji = input()
elif deci == "n":
    moji = 'パタトクカシーー'

def patotaku(moji):
    pato = []
    for i in [1,3,5,7]:
        pato.append(moji[i])
    return pato

moji = patotaku(moji)
print(moji)
