"""
First Example
"""

import pickle

test_dict = {
    "name": "parsa",
    "age": 28,
    "height": 180
}

pickle_format = pickle.dumps(test_dict)

normal_format = pickle.loads(pickle_format)

print(pickle_format)
print(normal_format)