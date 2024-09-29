import json
f = open("C:\\Users\\v-rapoosala\\test.txt ","w+")
phone_book = {}

command = ""

while(command!="exit"):
    command = input("enter operation new, get, save")
    
    if command == "new":
        person_name = input("enter person name")
        phone_num = input("enter phone num")
        address = input("enter address")

        phone_book[person_name]= {
            'phone_num' : phone_num,
            'address' : address
        }
        
        print(f"phone_book details {json.dumps(phone_book)}")
    
    elif command == "get":
        name = input("enter person name")

        if name in phone_book:
            print(f"found name from phone_book details {phone_book[name]}")
        else:
            print("details not found for given name")
    
    elif command == 'save':
        print("saving doc")
        f.write(json.dumps(phone_book))



