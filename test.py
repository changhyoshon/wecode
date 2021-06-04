
def even():
    list = []
    for i in range(1,51):
        if not i % 2:
            list.append(i)
    return list
print(even())