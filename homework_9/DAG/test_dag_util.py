import unittest
from dag_util import detect_cycle, topological_sort


class TestDAGUtil(unittest.TestCase):
    def test_cycle_detection_no_cycle(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': [],
        }
        self.assertEqual(detect_cycle(graph), (False, None))

    def test_cycle_detection_with_cycle(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': ['A'],
        }
        has_cycle, cycle = detect_cycle(graph)
        self.assertTrue(has_cycle)
        self.assertIn('A', cycle)

    def test_topological_sort_simple(self):
        graph = {
            'A': ['B'],
            'B': ['C'],
            'C': [],
        }
        self.assertEqual(topological_sort(graph), ['A', 'B', 'C'])

    def test_topological_sort_multiple_edges(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['C'],
            'C': ['D'],
            'D': []
        }
        self.assertEqual(topological_sort(graph), ['A', 'B', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
