from pytest_playwright_e2e.tests.demo.parent import parentClass

#  method resolution order
# list comprehension
# generators
obj = parentClass()
print(obj._parentClass__prev_attr )
class childClass(parentClass):
    def inherit_examp(self):
        pass
