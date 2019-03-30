wordnum = int(input())
words = []
graph = {}
for i in range(wordnum):
    words.append(input())
for i in range(wordnum):
    for a in range(0,len(words[i])-2):
        try:
            key = words[i][a]+words[i][a+1]+words[i][a+2]
            
            if key not in graph.keys():
                graph[key] = {}
                if a!=0:
                    graph[lastkey][key] = 1
                lastkey = key
                continue
            elif key in graph[lastkey].keys():
                graph[lastkey][key]+=1
                lastkey=key
            else:
                graph[lastkey][key]=1
                lastkey = key
        except:
            continue
print(len(graph.keys()))
b = 0
for a in graph.keys():
    b+=len(graph[a].keys())
print(b)
for a, b in graph.items():
    for c,d in b.items():
        print(a,c,d)
