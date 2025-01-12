def diStringMatch(s):
    while 'D' in s:
        s = s.replace('D', '0')
    while 'I' in s:
        s = s.replace('I', '1')
    return [i for i in range(len(s)+1)]
print(diStringMatch("IDID"))
