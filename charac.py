from pprint import pprint
a = input().strip('\r')
b = input().strip('\r')
c = input().strip('\r')
common1 = set.intersection(set(a),set(b),set(c))
pprint(list(common1))
common2= set(a) & set(b) - set(c)
pprint(list(common2))
common3= set(a) - set(b) - set(c)
pprint(list(common3))
common4= set.union(set(a),set(b),set(c))
pprint(common4)