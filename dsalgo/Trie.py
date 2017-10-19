class Contacts():
    def __init__(self):
        self.array = {'size':0}

    def addContact(self,contact):
        currentNode = self.array
        for eachChar in contact:
            if(currentNode.__contains__(eachChar)):
                currentNode['size'] = currentNode['size'] + 1
                currentNode = currentNode.get(eachChar)
            else:
                currentNode['size'] = 1
                currentNode.update({eachChar:{}})
                currentNode = currentNode.get(eachChar)

    def findContact(self,contact):
        currentNode = self.array
        counter = 0
        length = len(contact)
        if(len(contact) == 1):
            return currentNode['size']
        for eachChar in contact:
            counter = counter + 1
            if(not currentNode.__contains__(eachChar)):
                return 0
            else:
                if(counter == length):
                    return currentNode['size']
                currentNode = currentNode.get(eachChar)
        return 0

    def __str__(self):
        return str(self.array)


myContacts = Contacts()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if(op == 'add'):
        myContacts.addContact(contact)
    elif(op == 'find'):
        print (myContacts.findContact(contact))