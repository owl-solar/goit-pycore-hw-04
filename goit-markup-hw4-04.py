def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide a name and a phone number."
    name, phone = args
    if name in contacts:
        return f"Error: Contact '{name}' already exists."
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Please provide a name and a new phone number."
    name, new_phone = args
    if name not in contacts: 
        return "Error: Contact not found."
    else:
        contacts[name] = new_phone
        return "Contact updated."
     

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Please provide a name."
    name = args[0]
    if name not in contacts:
        return "Error: Contact not found."
    else:
        return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)
     
def parse_input(user_input):
    parts = user_input.split(maxsplit=1)
    cmd = parts[0].strip().lower()
    args = parts[1].split() if len(parts) > 1 else []
    return cmd, args
     
def main():
    contacts = {}                                         
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break                                           
        elif command == "hello":
            print("How can I help you?")                    
        elif command == "add":
            print(add_contact(args, contacts))            
        elif command == "change":
            print(change_contact(args, contacts))          
        elif command == "phone":
            print(show_phone(args, contacts))               
        elif command == "all":
            print(show_all(contacts))                       
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()                                                  
