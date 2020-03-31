import collections

inf = float('inf')
def breadth_first_search(self,graph , root):
    visited, queue = set(), collections.deque([root])
    distances = {vertex: inf for vertex in self.vertices}
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                distances[neighbour]+=1
                visited.add(neighbour)
                queue.append(neighbour)
    print(visited)
    print(distances)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: []}
    breadth_first_search(graph, 0)