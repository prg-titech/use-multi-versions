from version_dispatch import load_numpy

#scipy
class SciPy():
    def place_poles(self, A, B, desired_poles):
        np = load_numpy('1.26.4')
        res = np.linalg.solve(A, B)
        return res

# User Program
def my_place_poles(A, B, desired_poles):
    np = load_numpy('2.0.0')
    res = np.linalg.solve(A, B)
    return res

def main():
    np = load_numpy('2.0.0')
    # System Array & Desired Poles
    A = np.array(
      [ [[3, 1], [1, 2]]
      , [[2, 1], [1, 3]] ]) 
    B = np.array(
      [ [9, 8]
      , [7, 10] ])
    desired_poles = np.array([-1.0, -2.0])

    expect = SciPy().place_poles(A,B,desired_poles).tolist()
    actual = my_place_poles(A,B,desired_poles).tolist()

    print(expect)
    print(actual)

    test = np.array_equal(expect, actual)
    print(test)

main()
