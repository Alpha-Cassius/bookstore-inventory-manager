import json

new_book = {
    "title": "Atomic Habits", 
    "author": "James Clear", 
    "price": 14.99, 
    "in_stock": True
}

def manage_inventory():
    # --- Task 1: Read the inventory ---
    try:
        with open('inventory.json', 'r') as file:
            inventory = json.load(file)
        
        print(f"Task 1: Total books currently in file: {len(inventory)}")
        
    except FileNotFoundError:
        print("Error: inventory.json not found. Please ensure the file exists.")
        return

    # --- Task 2: Update and save ---
    inventory.append(new_book)

    with open('inventory.json', 'w') as file:
        json.dump(inventory, file, indent=4)
    
    print("Task 2: 'Atomic Habits' added and inventory.json updated successfully.")

    # --- Task 3: Display the inventory ---
    print("\nTask 3: Final Inventory List:")
    
    with open('inventory.json', 'r') as file:
        updated_inventory = json.load(file)

    for book in updated_inventory:
        print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']:.2f}")

if __name__ == "__main__":
    manage_inventory()
