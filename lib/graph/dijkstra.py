def dijkstra(graph, n, s):
    d = [INF] * n
    d[s], q = 0, [(0, s)]
    while q:
        dist, v = heappop(q)
        if d[v] < dist: continue
        for nv, cost in graph[v]:
            if d[nv] > d[v] + cost:
                d[nv] = d[v] + cost
                heappush(q, (d[nv], nv))
    return d
