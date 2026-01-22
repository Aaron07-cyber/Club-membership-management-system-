members = []

def add_member():
    name = input("Enter member name: ")
    member_id = input("Enter member ID: ")
    members.append({
        "name": name,
        "member_id": member_id
    })
    print("Member added successfully")

def view_members():
    if not members:
        print("No members found")
    else:
        for m in members:
            print("Name:", m["name"], "| ID:", m["member_id"])

def main():
    while True:
        print("1. Add Member")
        print("2. View Members")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
