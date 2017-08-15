from pprint import pprint
import sys
from copy import deepcopy


class Node:
    def __init__(self, name):
        self.name = str(name)
        self.neighbors = []

    def __repr__(self):
        return self.name

    def add_neighbor(self, neighbor, edge):
        self.neighbors.append((neighbor, edge))

    def remove_neighbor(self, neighbor, edge_wt):
        for nbr, edge in self.neighbors:
            if nbr == neighbor and edge.cost == edge_wt:
                self.neighbors.remove((nbr, edge))

    def __iter__(self):
        yield self.name


class Edge:
    def __init__(self, left_node, right_node, edge_label):
        self.left_node = left_node
        self.right_node = right_node
        self.edge_label = edge_label

    def __repr__(self):
        return "{}-[{}]->{}".format(self.left_node, self.edge_label, self.right_node)

    @property
    def cost(self):
        return self.edge_label

    def __iter__(self):
        yield self.left_node
        yield self.right_node
        yield self.edge_label


class Graph:
    def __init__(self, is_directed=False):
        self.nodes = []
        self.edges = []
        self.is_directed = is_directed

    def create_graph(self, size):
        for i in range(1, size + 1):
            self.nodes.append(Node(i))

        self.adj_mat = [[0] * size for _ in range(size)]

    def add_node(self, node):
        self.nodes.append(node)

    def get_index(self, node):
        return self.nodes.index(node)

    def get_node_by_index(self, index):
        return self.nodes[index - 1]

    @property
    def no_of_edges(self):
        return len(self.edges)

    @property
    def no_of_nodes(self):
        return len(self.nodes)

    def add_edge(self, left_idx, right_idx, edge_wt):
        edge = Edge(self.nodes[left_idx - 1], self.nodes[right_idx - 1], edge_wt)
        left, right = edge.left_node, edge.right_node
        if left not in self.nodes:
            self.add_node(left)
        if right not in self.nodes:
            self.add_node(right)
        left.add_neighbor(right, edge)
        self.adj_mat[self.get_index(left)][self.get_index(right)] = 1

        if not self.is_directed:
            right.add_neighbor(left, Edge(right, left, edge_wt))
            self.adj_mat[self.get_index(right)][self.get_index(left)] = 1

        self.edges.append(edge)
        return edge

    def exists_edge(self, edge):
        return edge in self.edges

    def remove_edge(self, edge):
        if self.exists_edge(edge):
            left, right, edge_wt = edge.left_node, edge.right_node, edge.cost
            left.remove_neighbor(right, edge_wt)
            self.adj_mat[self.get_index(left)][self.get_index(right)] = 0
            if not self.is_directed:
                right.remove_neighbor(left, edge_wt)
                self.adj_mat[self.get_index(right)][self.get_index(left)] = 0
            self.edges.remove(edge)

    def print_graph(self):
        print("Nodes:", self.nodes)
        print("Edges:", self.edges)
        print("Adj Matrix:")
        pprint(self.adj_mat)

    def __str__(self):
        self.print_graph()
        return ''

    def dfs(self, node):
        node = self.get_node_by_index(node)
        stack = [node]
        visited = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
            for nbr, _ in node.neighbors:
                if nbr not in visited:
                    stack.append(nbr)

        return visited

    def bfs(self, node):
        node = self.get_node_by_index(node)
        queue = [node]
        visited = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
            for nbr, _ in node.neighbors:
                if nbr not in visited:
                    stack.append(nbr)

    def dijkstra(self, node):
        dist_list = [sys.maxsize] * len(self.nodes)
        node = self.get_node_by_index(node)
        dist_list[self.get_index(node)] = 0

        queue = [node]
        visited = []
        while queue:
            curr_node = queue.pop(0)
            visited.append(curr_node)
            for next_node, edge in curr_node.neighbors:
                cost_to_curr_node = dist_list[self.get_index(curr_node)]
                cost_to_next_node = dist_list[self.get_index(next_node)]
                if cost_to_next_node > cost_to_curr_node + edge.cost:
                    dist_list[self.get_index(next_node)] = cost_to_curr_node + edge.cost

                if next_node not in visited:
                    queue.append(next_node)

        return dist_list

    def floyd_warshall(self):
        n_vertices = len(self.nodes)

        dist_mat = [[sys.maxsize] * n_vertices for _ in range(n_vertices)]
        for i in range(n_vertices):
            dist_mat[i][i] = 0

        for edge in self.edges:
            left, right = edge.left_node, edge.right_node
            left, right = self.get_index(left), self.get_index(right)
            dist_mat[left][right] = edge.cost

        path_mat = [[0 if dist_mat[i][j] == sys.maxsize else i for j in range(n_vertices)] for i in range(n_vertices)]

        # Given dist(u,v), check if path u -- intermediate_node -- v is shorter
        for intermediate_node in range(n_vertices):
            for u in range(n_vertices):
                for v in range(n_vertices):
                    # dist_mat[u][v] = min(dist_mat[u][v],
                    #                      dist_mat[u][intermediate_node] + dist_mat[intermediate_node][v])
                    cost_via_intermediate_node = dist_mat[u][intermediate_node] + dist_mat[intermediate_node][v]
                    curr_cost = dist_mat[u][v]
                    if cost_via_intermediate_node < curr_cost:
                        dist_mat[u][v] = cost_via_intermediate_node
                        path_mat[u][v] = path_mat[intermediate_node][v]

        dist_mat = [[-1 if dist == sys.maxsize else dist for dist in row] for row in dist_mat]

        # pprint(path_mat)
        return dist_mat

    def is_cyclic(self):
        if not self.is_directed:
            # return self.no_of_nodes <= self.no_of_edges
            no_of_nodes_with_edges = len(set((n for *t_nodes, _ in self.edges for n in t_nodes)))
            return no_of_nodes_with_edges <= self.no_of_edges
        else:
            parent_list = list(range(len(self.nodes)))
            for edge in self.edges:
                parent, child = edge.left_node, edge.right_node
                parent, child = self.get_index(parent), self.get_index(child)
                if parent_list[parent] == child:
                    return True
                parent_list[child] = parent_list[parent]
            return False

    def kruskal(self):
        mst = Graph(is_directed=self.is_directed)
        mst.create_graph(self.no_of_nodes)
        t_edges = sorted(self.edges, key=lambda e: e.cost, reverse=True)
        print(t_edges)
        while mst.no_of_edges < self.no_of_nodes - 1:
            new_edge = t_edges.pop()
            left_node, right_node, edge_wt = new_edge.left_node, new_edge.right_node, new_edge.cost
            left_idx, right_idx = self.get_index(left_node), self.get_index(right_node)
            new_edge = mst.add_edge(left_idx, right_idx, edge_wt)
            if mst.is_cyclic():
                mst.remove_edge(new_edge)
        return mst

    def prims(self):
        def helper(graph, mst_nodes):
            ''' Finds the minimum distance node from other set across the cut 
                Can be implemented with MinHeap for E*log(V) complexity 
            '''
            reachable_nodes_edges = []
            for node in mst_nodes:
                node = self.get_node_by_index(int(node))
                for nbr, edge in node.neighbors:
                    if nbr.name not in mst_nodes:
                        reachable_nodes_edges.append((nbr, edge))
            t = sorted(reachable_nodes_edges, key=lambda x: x[1].edge_label)
            next_cut_node, corr_edge = t[0]
            return next_cut_node, corr_edge

        mst_nodes = set(self.get_node_by_index(1))
        mst_edges = []

        while len(mst_nodes) <= self.no_of_nodes - 1:
            n, e = helper(self, mst_nodes)
            mst_nodes.add(n.name)
            mst_edges.append(e)

        print(mst_nodes)
        print(mst_edges)


def main(n_nodes, edge_list, is_directed):
    g = Graph(is_directed)
    g.create_graph(n_nodes)
    for edge in edge_list:
        _ = g.add_edge(*edge)
    print(g)
    # print(g.dijkstra(2))
    # pprint(g.floyd_warshall())
    # print(g.is_cyclic())
    g.prims()


edge_list = [(1, 2, 4), (1, 8, 8), (2, 3, 8), (2, 8, 11), (8, 9, 7), (8, 7, 1), (3, 9, 2), (9, 7, 6), (3, 6, 4), (3, 4, 7), (7, 6, 2), (4, 6, 14), (4, 5, 9), (6, 5, 10)]
main(9, edge_list, False)

edge_list = [(1, 2, 5), (2, 3, 3), (3, 4, 1), (4, 1, 2)]
# main(4, edge_list, False)
