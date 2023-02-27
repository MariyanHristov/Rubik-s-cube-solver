import unittest
from a_solver import scramble, solve, is_cube_solved
from a_movements import Movement


class TestTheProgram(unittest.TestCase):
    def test_stress_scramble_and_solve_100_times(self):
        for _ in range(100):
            scramble()
            solve()
            self.assertTrue(is_cube_solved())

    def test_correct_notation(self):
        movements = dict(zip(['up', 'up prime', 'down', 'down prime', 'left', 'left prime', 'right', 'right prime', 'front', 'front prime', 'back', 'back prime'],
                             ['U', 'U\'', 'D', 'D\'', 'L', 'L\'', 'R', 'R\'', 'F', 'F\'', 'B', 'B\'']))
        for movement in movements:
            self.assertEqual((Movement.move(movement, [], [], [], []),
                             movements[movement]), (movement, movements[movement]))


if __name__ == "__main__":
    unittest.main()
