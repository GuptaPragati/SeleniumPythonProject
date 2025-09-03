
import pytest

@pytest.fixture
def setUp():
    print("before test")
    yield
    print("after test")

pytest.mark.usefixtures("setUp")
class TestClassDemo:
    def test_method1(setUp):
        print("test 1")

    def test_method2(setUp):
        print("test 2")