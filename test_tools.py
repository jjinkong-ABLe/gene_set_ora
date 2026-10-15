import math
import tempfile
import unittest
from pathlib import Path

from gene_set_ora import bh_adjust, enrich, hypergeom_tail


class OraTests(unittest.TestCase):
    def test_exact_combinatorial_probability(self):
        expected = sum(math.comb(4,k)*math.comb(16,5-k) for k in range(2,5))/math.comb(20,5)
        self.assertAlmostEqual(hypergeom_tail(20,4,5,2),expected,places=12)
        self.assertEqual(hypergeom_tail(20,4,5,0),1)
        self.assertEqual(hypergeom_tail(20,4,5,5),0)

    def test_bh_known_values_and_order(self):
        observed = bh_adjust([0.01,0.04,0.03,0.2])
        for actual,expected in zip(observed,[0.04,0.05333333333333334,0.05333333333333334,0.2]):
            self.assertAlmostEqual(actual,expected)
        self.assertEqual(bh_adjust([]),[])

    def test_background_controls_membership(self):
        rows = enrich({'A'}, {'A','B','C'}, {'example':{'A','X'}, 'outside':{'X'}})
        self.assertEqual(rows[0]['set_size'],1)
        self.assertEqual(rows[1]['p_value'],1)
        with self.assertRaises(ValueError):
            enrich({'X'},{'A'},{'example':{'A'}})


if __name__ == '__main__':
    unittest.main()
