from ast import main
import tools

def test_py():
    print("Testing Chibchas...")
    user = "VICEFEP"
    password = "EDUCACION2021"
    tools.main(user, password, headless=False, end=2)
    print("All tests passed!")


test_py()
