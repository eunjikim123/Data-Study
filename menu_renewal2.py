import itertools
import collections

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
result = []

for course in course:

    combination = []

    for order in orders:

        combination += itertools.combinations(order,course)
    
    most_ordered = collections.Counter(combination).most_common()
    #print(most_ordered)
    #print(most_ordered[0][1])

    result += [k for k,v in most_ordered if v != 1 and v == most_ordered[0][1]]
    
result = [''.join(v) for v in sorted(result)]
print(result)