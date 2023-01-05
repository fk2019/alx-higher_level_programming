"""This module defines a factorial function"""

import collections

def group_by_len(words):
    d = collections.defaultdict(set)
    for word in words:
        d[len(word)].add(word)
        print(d)
        print("--")
    return d

l = group_by_len(["python", "module","of", "the", "week"])
s = {3:set(['the']),
      2:set(['of']),
      6:set(['python', 'module']),
      4:set(['week']),
    }
if l == s:
    print("True")
else:
    print("False")
