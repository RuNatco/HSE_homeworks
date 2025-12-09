import unittest
from connected_components import find_connected_components


class TestConnectedComponents(unittest.TestCase):
    def test_disconnected_graph(self):
        graph = {
            1: [],
            2: [],
            3: []
        }
        self.assertListEqual(find_connected_components(graph), [[1], [2], [3]])

    def test_connected_graph(self):
        graph = {
            1: [2, 3],
            2: [1, 3],
            3: [1, 2]
        }
        self.assertListEqual(find_connected_components(graph), [[1, 2, 3]])


    def test_large_graph(self):
        graph = {
            i: [i + 1] if i < 10 else [] for i in range(1, 12)
        }
        self.assertListEqual(find_connected_components(graph), [[i for i in range(1, 11)], [11]])

    def test_isolated_and_connected(self):
        graph = {
            1: [2],
            2: [1],
            3: [],
            4: [5, 6],
            5: [4],
            6: [4]
        }
        self.assertListEqual(find_connected_components(graph), [[1, 2], [3], [4, 5, 6]])

    def test_one_node(self):
        graph = {1: []}
        self.assertListEqual(find_connected_components(graph), [[1]])

    def test_empty_graph(self):
        graph = {}
        self.assertListEqual(find_connected_components(graph), [])


if __name__ == '__main__':
    unittest.main()
