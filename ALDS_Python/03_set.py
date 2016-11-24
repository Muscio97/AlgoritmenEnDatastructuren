s = {3, 24, 105}
print(s)

# s = {[3], [24], [105]}

d = {3:'drie', 24:'vier_en_twintig',105:'honderd_en_vijf'}
print(d)

# d = {[3]:'drie', [24]:'vier_en_twintig',[105]:'honderd_en_vijf'}

a = [3,24,105,105,3,24]
s = set(a)
print('s:', s)

s2 = 'abacadabra'
s = set(s2)
print('s:', s)
print('sorted(s):', sorted(s))