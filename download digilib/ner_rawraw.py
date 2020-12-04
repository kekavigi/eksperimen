from pprint import pprint

data = []

while True:
    a = input()
    if not a: break
    raw, train = a.split('\t')
    train = train.split(' - ')

    res = []
    for t in train:
        start = raw.index(t)
        end = start+len(t)
        res.append((start, end, 'Name'))

    data.append((raw, {'entities': res.copy()}))
    
