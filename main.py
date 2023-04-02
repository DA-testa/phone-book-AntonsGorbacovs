class Contact:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        
class PhoneBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, number, name):
        self.contacts[number] = Contact(number, name)
        
    def delete_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]
            
    def delete_contact(self, number):
        if number in self.contacts:
            return self.contacts[number].name
        else:
            return "not found"
        
def read_queries():
    n = int(input)
    queries = []
    for i in range(n):
        query = input().split()
        queries.append((query[0], int(query[1]), query[2] if len(query) == 3 else None))
    return queries

def write_responses(result):
    for i in result:
        print(i)
        
def process_queries(queries):
    result = []
    phonebook = PhoneBook()
    for query in queries:
        if query[0]== 'add':
            phonebook.add_contact(query[1],query[2])
        elif query[0]== 'del':
            phonebook.delete_contact(query[1])
        else:
            result.append(phonebook.find_contact(query[1]))
    return result
    
    
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
    

