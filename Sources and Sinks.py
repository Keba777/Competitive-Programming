n = int(input())
graph = [[] for _ in range(n)]

for r in range(n):
    row = list(map(int, input().split()))
    graph[r] = row

source = []
sink = []

for node in range(1, n + 1):
    has_incoming_edge = False
    has_outgoing_edge = False

    for r in range(n):
        if graph[r][node - 1] == 1:
            has_incoming_edge = True
        if graph[node - 1][r] == 1:
            has_outgoing_edge = True

    if not has_incoming_edge:
        source.append(node)

    if not has_outgoing_edge:
        sink.append(node)

print(len(source), *source)
print(len(sink), *sink)
