list_of_keys = [
    "access_level", 
    "age"
    ]
employee = {
    "name": "John", 
    "email": "john@ecorp.com", 
    "access_level": "5", "age": "28"
    }

deleted_items = {}
for key in list_of_keys:
    if key in employee:
        deleted_items[key] = employee.pop(key)
        
print(employee)
print(f'Deleted item: {deleted_items}')


#{’name’: ‘John’, 'email’: ‘john@ecorp.com’}