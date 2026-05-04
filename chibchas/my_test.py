from ast import main
import tools

def test_py():
    print("Testing Chibchas...")
    user = "VICEFEP"
    password = "EDUCACION2021"
    tools.main(user, password, headless=False, end=None, target_data='All')
    print("All tests passed!")


def read_pickle():
    import pickle

    objects = []
    with open('InstituLAC/dfg.pickle', 'rb') as file:
        while True:
            try:
                objects.append(pickle.load(file))
            except EOFError:
                break  # End of file reached

    print(objects[0].keys())

test_py()
# read_pickle()
