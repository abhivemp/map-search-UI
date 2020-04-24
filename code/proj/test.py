tagName = []
tagCount = []
#adter otag stuff
oTag = [('Java', 25), ('Python', 20), ('C++', 80), ('Psql', 35), ('C', 50)]
colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

for i in oTag:
    tagCount.append(i[1])
    tagName.append(i[0])
    # print(i)

# print(tagCount)
# print(tagName)
set = zip(tagName,tagCount,colors)
for i in set:
    print(i)
