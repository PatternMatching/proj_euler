#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

"""Enumerates lattice paths that terminate in lower right corner."""

from itertools import product

LATTICE_SIZE = 20


class DirectedLatticeGraph(object):

    def __init__(self, lattice_size=LATTICE_SIZE):
        self.lattice_size = lattice_size
        self._vertices = set()
        # Will use a map from unique vertex to list of other vertices
        self._edges = {}

    def add_vertex(self, v):
        """Adds 'v' to the graph"""
        assert self._is_vertex_valid(v)
        self._vertices.add(v)
        self._edges[v] = []

    def add_edge(self, source, dest):
        assert self._is_vertex_valid(source)
        assert self._is_vertex_valid(dest)
        assert source in self._vertices and dest in self._vertices
        self._edges[source].append(dest)

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    def print_all_paths(self, source, dest):
        """Depth-first traversal of paths from 'source' to 'dest'"""
        visited = {v: False for v in self._vertices}

        all_paths = []
        self._dfs(source, dest, visited, [], all_paths)

        return all_paths

    def _dfs(self, v, dest, visited, path, all_paths):
        path.append(v)
        visited[v] = True
        adj_vertices = self._edges[v]

        if v == dest:
            all_paths.append(path)
        for av in adj_vertices:
            if not visited[av]:
                self._dfs(av, dest, visited, path, all_paths)

        path.pop()
        visited[v] = False

    def _is_vertex_valid(self, v):
        assert isinstance(v, tuple)
        # Only dealing in two dimensions for now
        assert len(v) == 2
        assert isinstance(v[0], int)
        assert isinstance(v[1], int)
        assert (v[0] >= 0) and (v[1] >= 0)
        assert (v[0] <= self.lattice_size) and (v[1] <= self.lattice_size)
        return True


def construct_lattice_graph(size=LATTICE_SIZE):
    dg = DirectedLatticeGraph()

    for x, y in product(range(LATTICE_SIZE + 1), repeat=2):
        dg.add_vertex((x, y))

    for x, y in product(dg.vertices, repeat=2):
        row_threshold = y[0] - x[0]
        col_threshold = y[1] - x[1]
        discard = ((row_threshold < 0 or col_threshold < 0) or
                   (row_threshold > 1 or col_threshold > 1) or
                   (row_threshold == 1 and col_threshold == 1))
        if discard:
            continue
        elif row_threshold == 1:
            dg.add_edge(x, y)
            continue
        elif col_threshold == 1:
            dg.add_edge(x, y)

    return dg


if __name__ == '__main__':
    dg = construct_lattice_graph()
    paths = dg.print_all_paths((0, 0), (20, 20))
    print(len(paths))
