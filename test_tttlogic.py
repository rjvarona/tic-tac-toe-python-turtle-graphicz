#  Perform some simple sanity checks on tttlogic.py

import unittest
import tttlogic

class SimpleTest(unittest.TestCase):
    def test001(self):
        # Sequence of moves (including some attempts at bad moves)
        seq = ["East", "Center", "SouthEast", "East", "NorthEast", 
               "SouthWest", "Fred", "North", "South"]
        tttlogic.initialize_board()
        for mv in seq:
            tttlogic.move(mv)
        self.assertEqual(tttlogic.check_status(), ('X', 'Win_SW_SE'))

    def test002(self):
        tttlogic.initialize_board()
        self.assertEqual(tttlogic.current_player(), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertEqual(tttlogic.look("Center"), None)
        self.assertTrue(tttlogic.move("Center"))
        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.look("Center"), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertFalse(tttlogic.move("Center"))
        self.assertEqual(tttlogic.look("Center"), 'X')
        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

    def test003(self):
        # Sequence of moves (including some attempts at bad moves)
        seq = ["East", "Center", "SouthEast", "East", "NorthEast", 
               "SouthWest", "Fred", "North", "South"]
        tttlogic.initialize_board()
        self.assertEqual(tttlogic.current_player(), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertEqual(tttlogic.look("East"), None)
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertEqual(tttlogic.current_player(), 'X')
        self.assertTrue(tttlogic.move("East"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertTrue(tttlogic.move("Center"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertTrue(tttlogic.move("SouthEast"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertEqual(tttlogic.look("East"), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertFalse(tttlogic.move("East"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertTrue(tttlogic.move("NorthEast"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertTrue(tttlogic.move("SouthWest"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertFalse(tttlogic.move("Fred"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'O')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertTrue(tttlogic.move("North"))
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))

        self.assertEqual(tttlogic.current_player(), 'X')
        self.assertEqual(tttlogic.check_status(), (None, 'Playing'))
        self.assertTrue(tttlogic.move("South"))
        self.assertEqual(tttlogic.check_status(), ('X', 'Win_SW_SE'))


if __name__ == '__main__':
    unittest.main()

