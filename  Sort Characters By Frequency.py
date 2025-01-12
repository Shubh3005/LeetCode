from collections import Counter
def frequencySort(s):
    c = Counter(s)
    s = ""
    for k, v in c.most_common():
        s += k*v

    return s
print(frequencySort("tree"))
