# SequenceMatcher

from difflib import SequenceMatcher

txt1 = 'I am Sandeep'
txt2 = 'I am Sundeep'

SequenceMatcher (a = txt1, b = text2).ratio()


s = SequenceMatcher(lambda x: x == ' ', 'I am Sandeep', 'I am Sundeep')

print(round(s.ratio(), 3))

len(txt1)
len(txt2)

s.find_longest_match(0,12,0,12)

for block in s.get_matching_blocks():
    print ('a[%d] and b[%d] match for %d elements' % block)











