from unittest import mock

class A():
    def __init__(self,passedAlgorithm):
        self.algorithm = passedAlgorithm

    def execute(self):
        self.algorithm()

    def others(self):
        print('I stay the same')

class B():
    def compute(self):
        def heavyAlgorithm():
            print ('I am Heavy')
        a = A(heavyAlgorithm)
        a.execute()
        a.others()

def liteAlgorithm():
    print('I am Lite')

class C(A):
    def __init__(self,passedAlgorithm):
        A.__init__(passedAlgorithm)
        self.algorithm = liteAlgorithm


# b = B()
# b.compute()


@mock.patch('__main__.A')
def mock_simple_class(mock_class):
    mock_class = C
    b = B()
    b.compute()

def dummy():
    print('Dummy')

mock_simple_class()