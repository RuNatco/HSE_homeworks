import unittest
from dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0, 'B': 1, 'C': 3, 'D': 4})

    def test_disconnected_graph(self):
        graph = {
            'A': {'B': 1},
            'B': {'A': 1},
            'C': {'D': 1},
            'D': {'C': 1}
        }
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0, 'B': 1, 'C': float('inf'), 'D': float('inf')})

    def test_single_node(self):
        graph = {'A': {}}
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0})

    def test_isolated_nodes(self):
        graph = {'A': {}, 'B': {}, 'C': {}}
        self.assertEqual(dijkstra(graph, 'A'), {'A': 0, 'B': float('inf'), 'C': float('inf')})


if __name__ == '__main__':
    unittest.main()
