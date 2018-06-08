

#================================================================================

print("\n --- 10. 行数のカウント --- ")

num_lines = sum(1 for line in open('hightemp.txt'))
print(num_lines)

#================================================================================

print("\n --- 11. タブをスペースに置換 --- ")

f = open('hightemp.txt')
Allf = f.read()

text = Allf.expandtabs(1)
print( text )

f.close()
