

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

import linecache

a = input('取り出したい行数は？：')
for i in range(num_lines - (int(a) - 1), num_lines + 1):
    target_line = linecache.getline('hightemp.txt', i)
    print(target_line)
    linecache.clearcache()
