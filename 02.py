

#================================================================================

print("\n --- 10. 行数のカウント --- ")

num_lines = sum(1 for line in open('hightemp.txt'))
print(num_lines)

#================================================================================

print("\n --- 11. タブをスペースに置換 --- ")

f = open('hightemp.txt','r')
Allf = f.read()

text = Allf.expandtabs(1)
print( text )

f.close()

#================================================================================

print("\n --- 12. 1列目をcol1.txtに，2列目をcol2.txtに保存 --- ")

ld = open("hightemp.txt")
lines = ld.readlines()
ld.close()

f1 = open('col1.txt','a')
f2 = open('col2.txt','a')

for ix , line in enumerate(lines):
    if ix % 2 == 0:
        f1.write(line)
    else:
        f2.write(line)

f1.close()
f2.close()

#================================================================================

print("\n --- 13. col1.txtとcol2.txtをマージ --- ")

f1 = open('col1.txt')
f2 = open('col2.txt')

lines1 = f1.readlines()
lines2 = f2.readlines()

f1.close()
f2.close()

ans_13 = open('ans_13.txt','a')

for line1,line2 in zip(lines1, lines2):
    ans_13.write(line1 + line2)

ans_13.close()

#================================================================================

print("\n --- 14. 先頭からN行を出力 --- ")

import linecache

a = input('取り出したい行数は？：')
for i in range(int(a) + 1):
    target_line = linecache.getline('hightemp.txt', i)
    print(target_line)
    linecache.clearcache()


#================================================================================

print("\n --- 15. 末尾のN行を出力 --- ")


a = input('取り出したい行数は？：')
for i in range(num_lines - (int(a) - 1), num_lines + 1):
    target_line = linecache.getline('hightemp.txt', i)
    print(target_line)
    linecache.clearcache()

#================================================================================

print("\n --- 16. ファイルをN分割する --- ")

a = input('N分割？：')

num_1_group = int(num_lines / int(a))

g_num = 1
for i in range(num_lines + 1):
    if i % num_1_group - 1 == 0:
        print('group' + str(g_num))
        g_num += 1

    target_line = linecache.getline('hightemp.txt', i)
    print(target_line)
    linecache.clearcache()

#================================================================================

print("\n --- 17. １列目の文字列の異なり --- ")

target_line = linecache.getline('hightemp.txt', 1)
ans_17 = target_line.split(" ")
ans_17 = ans_17[0].replace("\n"," ")
ans_17 = ans_17.replace("\t"," ")
ans_17 = ans_17.replace(" ","")
print(ans_17)

alnum = []
alpha = []
digit = []
decimal = []
numeric = []

syugo_list = (alnum, alpha, digit , decimal, numeric)

for ix in range(len(ans_17)):
    if ans_17[ix].isalnum():
        alnum.append(ans_17[ix])
    if ans_17[ix].isalpha():
        alpha.append(ans_17[ix])
    if ans_17[ix].isdigit():
        digit.append(ans_17[ix])
    if ans_17[ix].isdecimal():
        decimal.append(ans_17[ix])
    if ans_17[ix].isnumeric():
        numeric.append(ans_17[ix])

for _ in syugo_list:
    print(_)
