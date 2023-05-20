from sys import stdin
def main():
    n = int(input().strip())
    k = int(input().strip())
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(k):
        operation = list(map(int, input().strip().split()))
        
        if operation[0] == 1:
            u, v = operation[1], operation[2]
            graph[u].append(v)
            graph[v].append(u)
        else:
            u = operation[1]
            print(" ".join(map(str, graph[u])))

if __name__ == "__main__":
    main()
