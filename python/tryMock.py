from python.mockCheck import myClass
import unittest
import unittest.mock as mock


class testMock(unittest.TestCase):

    @mock.patch.object(myClass, 'functionToMock')
    def callIt(self,replacementMethod):
        myObject = myClass()
        return myObject.functionToMock(1)

def replacementFunction():
    return 123

tempObject = testMock()
print (testMock.callIt(123))