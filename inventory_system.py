"""
Inventory Management System

Performs basic operations such as adding, removing, saving, loading,
and checking for low-stock items in an inventory.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Global variable for inventory data
STOCK_DATA = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item with the given quantity to the inventory.
    Quantity must be a positive number.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning("Invalid item or quantity: item=%s, qty=%s", item, qty)
        return

    if qty <= 0:
        logging.warning("Cannot add non-positive quantity (%s) for item '%s'", qty, item)
        return

    STOCK_DATA[item] = STOCK_DATA.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)



def remove_item(item, qty):
    """
    Remove a specific quantity of an item from the inventory.
    """
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        logging.warning(
            "Invalid item or quantity for removal: %s, %s",
            item,
            qty,)
        return

    if item not in STOCK_DATA:
        logging.warning("Attempted to remove non-existing item: %s", item)
        return

    STOCK_DATA[item] -= qty
    if STOCK_DATA[item] <= 0:
        del STOCK_DATA[item]
        logging.info("Removed item '%s' completely (stock depleted)", item)
    else:
        logging.info("Removed %d of %s", qty, item)


def get_qty(item):
    """
    Get the current quantity of an item in the inventory.
    """
    return STOCK_DATA.get(item, 0)


def load_data(file_path="inventory.json"):
    """
    Load inventory data from a JSON file.
    """
    global STOCK_DATA
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            STOCK_DATA = json.load(file)
        logging.info("Loaded data from %s", file_path)
    except FileNotFoundError:
        logging.warning(
            "File not found: %s. Starting with empty stock.",
            file_path,)
        STOCK_DATA = {}
    except json.JSONDecodeError as exc:
        logging.error("Invalid JSON format in %s: %s", file_path, exc)
        STOCK_DATA = {}


def save_data(file_path="inventory.json"):
    """
    Save current inventory data to a JSON file.
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(STOCK_DATA, file, indent=4)
        logging.info("Saved data to %s", file_path)
    except OSError as exc:
        logging.error("Error saving data: %s", exc)


def print_data():
    """
    Print all inventory items with their quantities.
    """
    print("Items Report:")
    if not STOCK_DATA:
        print("No items in stock.")
        return

    for item, qty in STOCK_DATA.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """
    Return a list of items below the given stock threshold.
    """
    return [item for item, qty in STOCK_DATA.items() if qty < threshold]


def main():
    """
    Demonstration of inventory system functions.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)

    apple_qty = get_qty("apple")
    low_items = check_low_items()

    print(f"Apple stock: {apple_qty}")
    print(f"Low items: {low_items}")

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
