import pandas as pd
import os

def menu():
    options = ["1", "2", "3", "4", "5"]

    print("\n----- Inventory Manager -----")
    print("1. Add New Item")
    print("2. Update Stock")
    print("3. View Inventory")
    print("4. Check Low Stock Items")
    print("5. Quit")

    while True:
        option = input("\nChoose an Option: ").strip()
        if option not in options:
            print("Please Choose a Valid Option.")
        else:
            return option


def view_inventory(df):
    print("   Inventory   ".center(104, "=") + "\n")
    print(df.to_string(index=False, col_space=20))
    print("\n" + "=" * 104)


def initialize_inventory():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "inventory.csv")

    df = pd.read_csv(file_path)
    df.columns = ["ID", "Name", "Category", "Quantity", "Packaging Type"]
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").astype("Int64")
    return df


def add_item(df):
    print("\n======= Adding New Item =======")

    item_id = len(df) + 1

    # Item Name Input
    while True:
        item_name = input("\nEnter Item Name: ").strip().capitalize()
        if item_name in df["Name"].tolist():
            print("An item with this name already exists. Try another name.")
        else:
            break

    # Category Selection
    all_categories = sorted(set(df["Category"]))
    print("\nCategorys:")
    for idx, category in enumerate(all_categories, start=1):
        print(f"{idx}. {category}")

    while True:
        try:
            choice = int(input("\nSelect Category (number): ").strip())
            selected_category = all_categories[choice - 1]
            print(f"You Selected {selected_category}")
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

    # Quantity input
    while True:
        item_quantity_str = input("\nEnter Item Quantity: ").strip()
        if not item_quantity_str.isdigit():
            print("Please enter a number.")
            continue 
        item_quantity = int(item_quantity_str)
        break

    # Packaging type selection
    all_packaging_types = sorted(set(df["Packaging Type"]))
    print("\nPackaging Types:")
    for i, p_type in enumerate(all_packaging_types, 1):
        print(f"{i}. {p_type}")

    while True:
        try:
            choice = int(input("\nSelect Packaging Type (number): ").strip())
            selected_package_type = all_packaging_types[choice - 1]
            print(f"You selected: {selected_package_type}")
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

    new_item = {
        "ID": item_id,
        "Name": item_name,
        "Category": selected_category,
        "Quantity": item_quantity,
        "Packaging Type": selected_package_type,
    }

    df.loc[len(df)] = new_item
    print("\n✅ Item added successfully!")
    return df


def update_stock(df):
    view_inventory(df)  # Display all inventory

    while True:
        try:
            choice = int(input("\nEnter Item ID to Update: ").strip())
            row_df = df[df["ID"] == choice]
            if row_df.empty:
                print("Invalid choice. No item with that ID.")
                continue  

            row = row_df.iloc[0]

            print("\n" + "   Item Details   ".center(80, "=") + "\n")
            for field, value in row.items():
                if field == "ID":
                    continue
                print(f"{field}: {value}")

            while True:
                item_quantity_str = input("\nEnter Item Quantity: ").strip()
                try:
                    item_quantity = int(item_quantity_str)
                    if item_quantity < 0:
                        print("Please enter a positive number.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")


            df.loc[df["ID"] == choice, "Quantity"] = item_quantity      
            print(f"\nQuantity updated!")
            break 
        except ValueError:
            print("Invalid input. Please enter a number.")

    return df


def check_low_stock(df):
    low_stock_items = df[df["Quantity"] <= 5]
    if low_stock_items.empty:
        print("There are no low stock items.")
    else:
        print(low_stock_items.to_string(index=False, col_space=20))
    

def main():
    df = initialize_inventory()
    
    while True:
        option = menu()
        
        if option == "1":
            df = add_item(df)

        elif option == "2":
            print("Updating Stock")
            df = update_stock(df)
        
        elif option == "3":
            view_inventory(df)
            
        elif option == "4":
            check_low_stock(df)

        elif option == "5":
            print("Applicaiton Closed. Data all changes have been saved.")
            df.to_csv("inventory.cvs", index=False, header=["id", "name", "category", "quantity", "packaging_type"])
            break
        

if __name__ == "__main__":
    main()