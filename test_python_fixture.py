import pytest

# to run the test case with print statements use command: pytest -s
# to run a specific method in the pytest the use command: pytest -s test_python_fixture.py::test_firstTest
# command to run those test cases which are mark with smoke tag: pytest -m smoke
# to run only failed test cases: pytest --last-failed
@pytest.fixture(scope="function")
def precondition():
    print("fixture will run first before execute function")
    return "fail"

@pytest.fixture(scope="module")
def precondition1():
    print("module fixture run before yield")
    yield
    print("module fixture run after yield")

def test_firstTest(precondition, precondition1):
    print("my first pytest")
    assert precondition == "fail"

def test_secondTest(session_precondition):
    print("my second pytest")

def test_ThirdTest(session_precondition):
    print("my third pytest")

@pytest.mark.smoke # we can use custom tag
def test_forthTest(precondition):
    print("my forth pytest")

@pytest.mark.skip
def test_fifthTest(precondition):
    print("my fifth pytest")
