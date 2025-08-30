import os

def list_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if not files:
        print("No files found in current directory.")
        return []
    
    print("\nFiles in current directory:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    return files

def rename_file():
    files = list_files()
    if not files:
        return
    
    try:
        choice = int(input("\nEnter file number to rename: ")) - 1
        if 0 <= choice < len(files):
            old_name = files[choice]
            new_name = input(f"Enter new name for '{old_name}': ")
            
            if new_name and new_name != old_name:
                os.rename(old_name, new_name)
                print(f"✅ Renamed '{old_name}' to '{new_name}'")
            else:
                print("❌ Invalid name or no change needed")
        else:
            print("❌ Invalid file number")
    except (ValueError, FileExistsError) as e:
        print(f"❌ Error: {e}")

print("📁 File Renamer")
print("-" * 20)

while True:
    print("\n1. Rename a file")
    print("2. Exit")
    
    choice = input("\nChoose option: ")
    if choice == '1':
        rename_file()
    elif choice == '2':
        break
    else:
        print("❌ Invalid option")