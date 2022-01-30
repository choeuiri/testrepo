counts = dict()
names = ['csev','csev','cwen','zaiqn', 'joe', 'csev','joe','cwem']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)
