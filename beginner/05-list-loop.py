arr = ["a", "bb", "ccc"]

for idx, val in enumerate(arr):
    print(idx, val)

for idx, val in enumerate(reversed(arr)):
    print(idx, val)



#  looping through dictionaries

mydic = {
           "name": "Abhishek",
           "address": "1234 street"
        }

for k, v in mydic.items():
    print(k, v)