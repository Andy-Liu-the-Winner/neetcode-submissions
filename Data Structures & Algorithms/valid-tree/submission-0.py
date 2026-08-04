class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges.sort()
        graph = [set() for i in range(n)]
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue 
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n

