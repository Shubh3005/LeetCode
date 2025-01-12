def groupAnagrams(strs):
    if not strs:
        return [[""]]
    if len(strs)==1:
        return [strs]
    res = {}
    for i in strs:
        k = "".join(sorted(i))
        if k in res:
            res[k].append(i)
        else:
            res[k] = [i]
    return list(res.values())