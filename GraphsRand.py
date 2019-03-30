import random
import graphviz
import csv

def stdgrrand():
    a = random.randint(4,10)
    G = [[0]*a for i in range(a)]
    for i in range(a):
        for j in range(a):
            if j != i:
                G[i][j]=random.randint(0,1)
    for i in range(a):
        for j in range(a):
            if G[i][j]==1:
                G[j][i]=0
    T = {}
    for i in range(len(G)):
        Time = []
        for j in range(len(G[i])):
            if G[i][j] == 1:
                Time.append(j)
        T[i]=Time
    return T

def fgrrand(a):
    while True:
        mat = matfgrrand(a)
        if stockcheck(mat):
            break
    adj = {}
    for i in range(len(mat)):
        adj[i+1]=[]
        for j in range(len(mat)):
            if mat[i][j]==1:
                adj[i+1].append(j+1)
    
    addflow(adj)
    return adj

def stockcheck(mat):
    X = {}
    for a in range(1,len(mat)):
        X[a] = 0
    for i in range(1,len(mat)):
        for j in range(1,len(mat)):
            if mat[i][j]==1:
                X[j]=1
    if 0 in X.values():
        return False
    else:
        return True
        
def matfgrrand(a):
    G = [[0]*a for i in range(a)]
    for i in range(a-1):
        while True:
            G[i] = flowrandrow(G[i])
            for j in range(len(G[i])):
                if G[j][i]==1 and G[i][j]==1:
                    G[i][j]=0
            if 1 in G[i]:
                break
    return G

def flowrandrow(T):
    for i in range(len(T)):
        if i!=0:
            T[i] = random.randint(0,1)
    return T

def addflow(adj):
    for a in adj.keys():
        Time = {}
        for b in adj[a]:
            Time[b] = (0, random.randint(0,1))
        adj[a] = Time

def addveight(adj):
    for a in adj.keys():
        Time = []
        for b in adj[a]: 
            count = random.randint(1,10)
            Time.append([b,count])
        adj[a] = Time
 
 def stdcsvwrite(T, FILENAME):
    with open(FILENAME, "w", newline="") as file:
        wr = csv.writer(file)    
        for key,values in T.items():
            Time = []
            Time.append (key)
            Time += values
            wr.writerow(Time) 
  
  def flowcsvwrite(T,FILENAME):
     with open(FILENAME, "w", newline="") as file:
        wr = csv.writer(file)    
        for key,values in adj.items():
            Time = []
            Time.append(key)
            for a, b in values.items():
                Time.append(a)
                Time +=[b]
            wr.writerow(Time)
 
 def stdcsvread(FILENAME):
    adj = {}
    with open(FILENAME) as file:
        reader = csv.reader(file)
        for row in reader:
            st = int(row[0])
            adj[st] = []
            for a in row[1:]:
                adj[st].append(int(a))
    return adj

def vcsvreader(FILENAME):
    adj = {}
    with open(FILENAME) as file:
        reader = csv.reader(file)
        for row in reader:
            st = int(row[0])
            adj[st]=[]
            for a in row[1:]:
                Time = []
                for b in a:
                    try:
                        Time.append(int(b))
                    except:
                        continue
                adj[st].append(Time)
    return adj
 
 if __name__ == '__main__':
    while True:
        index = input()
        adj =stdgrrand()
        if index == "1" : 
            file = "graph.csv"
            stdcsvwrite(adj,file)
            adj = stdcsvread(file)
            graph = graphviz.Digraph()
            for a in adj.keys():
                for b in adj[a]:
                    graph.edge(str(a),str(b))
            break
        if index == "2" :
            file = "vgraph.csv"
            addveight(adj)
            stdcsvwrite(adj,file)
            adj = vcsvreader(file)
            graph = graphviz.Graph() 
            for a in adj.keys():
                for b in adj[a]:
                    graph.edge(str(a),str(b[0]),label = str(b[1]))
            break
        if index == "3" :
            print("Введите количество вершин:")
            st = int(input())
            file = "fgraph.csv"
            adj = fgrrand(st)
            flowcsvwrite(adj,file)
            if st < 10:
                graph = graphviz.Digraph()
                for a in adj.keys():
                    for b in adj[a].keys():
                        graph.edge(str(a),str(b),label = str(adj[a][b][0])+"/"+str(adj[a][b][1]))
            else:
                graph = "слишком большое число рёбер"
            break
    print("Вывод словаря(графа):")
    for a in adj.keys():
        print(a,": ",adj[a])
    graph
