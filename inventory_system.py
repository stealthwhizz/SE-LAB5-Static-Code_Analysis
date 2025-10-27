
"""
Inventory System Module
Provides functions to manage inventory items, including adding, removing, saving, and loading stock data.
"""

import json
import logging
from datetime import datetime


# Global variable
stock_data = {}  # Global variable for inventory stock data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.
    Args:
        item (str): Name of the item.
        qty (int): Quantity to add.
        logs (list, optional): List to append log messages to.
    """
    if not isinstance(item, str) or not item:
        logging.warning("Invalid item name: %r", item)
        return
    if not isinstance(qty, int):
        logging.warning("Invalid quantity for %s: %r", item, qty)
        return
    if logs is None:
        logs = []
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """
    Remove a quantity of an item from the inventory.
    Args:
        item (str): Name of the item.
        qty (int): Quantity to remove.
    """
    if not isinstance(item, str) or not item:
        logging.warning("Invalid item name: %r", item)
        return
    if not isinstance(qty, int):
        logging.warning("Invalid quantity for %s: %r", item, qty)
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        logging.warning("Tried to remove non-existent item: %s", item)

def get_qty(item):
    """
    Get the quantity of an item in the inventory.
    Args:
        item (str): Name of the item.
    Returns:
        int: Quantity of the item, or 0 if not found.
    """
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.
    Args:
        file (str): Path to the JSON file.
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)

def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.
    Args:
        file (str): Path to the JSON file.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)

def print_data():
    """
    Print a report of all items in the inventory.
    """
    print("Items Report")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")

def check_low_items(threshold=5):
    """
    Check for items with quantity below a threshold.
    Args:
        threshold (int): The threshold value.
    Returns:
        list: List of item names below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    """
    Main execution block for inventory system demo.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, now checked
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
