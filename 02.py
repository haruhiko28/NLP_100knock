
#================================================================================

print("\n --- 10. 行数のカウント --- ")

num_lines = sum(1 for line in open('hightemp.txt'))
print(num_lines)

#================================================================================

print("\n --- 11. タブをスペースに置換 --- ")

f = open('hightemp.txt','r')
Allf = f.read()
print( Allf )

print('\n↓↓↓↓↓↓↓↓↓↓↓( ^ω^ )( ^ω^ )スペースに変換するンゴ( ^ω^ )( ^ω^ )↓↓↓↓↓↓↓↓↓↓↓\n')

text = Allf.expandtabs(1)
print( text )

f.close()

#================================================================================

print("\n --- 12. 1列目をcol1.txtに，2列目をcol2.txtに保存 --- ")

import pandas as pd

df = pd.read_table("hightemp.txt",header = None)
df.columns = ['prefecture','place', 'temp', 'day']

df['prefecture'].to_csv('col1.txt',index=False)
df['place'].to_csv('col2.txt',index=False)

with open("hightemp.txt", "r") as f:
    lines = f.readlines()
    lines = lines.replace('\n','')
    lines = lines.replace('\t','')
    print(lines)
    print(len(lines))

#================================================================================

print("\n --- 13. col1.txtとcol2.txtをマージ --- ")

col1 = pd.read_csv('col1.txt')
col2 = pd.read_csv('col2.txt')

col1_2 = pd.concat([col1, col2],axis=1)

col1_2.to_csv('ans_13.txt',sep='\t',index=False)

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
        print('==== group ' + str(g_num) + ' ====\n')
        g_num += 1

    target_line = linecache.getline('hightemp.txt', i)
    print(target_line)
    linecache.clearcache()

#================================================================================

print("\n --- 17. １列目の文字列の異なり --- ")

print(df['prefecture'].unique().tolist())

#================================================================================

print("\n --- 18. 各行を3コラム目の数値の降順にソート --- ")

print(df.sort_values(by = ['temp'], ascending=False))

#================================================================================

print("\n --- 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる --- ")

print(df['prefecture'].value_counts())
