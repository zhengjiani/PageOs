import collections
import json

tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = 'yellow'
print(json.dumps(some_dict))