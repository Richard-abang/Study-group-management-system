study_groups = []

def create_group():
    group_name = input("Enter group name: ")
    members = input("Enter members (comma separated): ")
    study_groups.append({
        "group": group_name,
        "members": members
    })
    print("Study group created")

def view_groups():
    if not study_groups:
        print("No study groups found")
    else:
        for g in study_groups:
            print("Group:", g["group"])
            print("Members:", g["members"])
            print("------------------")

def main():
    while True:
        print("1. Create Study Group")
        print("2. View Study Groups")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_group()
        elif choice == "2":
            view_groups()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
