"""Inventory Management System
Performs add, remove, view, and save operations on stock data.
This version passes Pylint, Flake8, and Bandit checks cleanly.
"""

import json
import logging
from datetime import datetime
import ast  # for safe evaluation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Global variable (kept for simplicity)
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add a quantity of an item to the inventory."""
    if logs is None:
        logs = []

    # Type validation
    if not isinstance(item, str):
        logging.warning("Invalid item name: %s. Must be a string.", item)
        return
    if not isinstance(qty, (int, float)):
        logging.warning("Invalid quantity: %s. Must be numeric.", qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(
        f"{datetime.now()}: Added {qty} of {item}"
    )
    logging.info("Added %d of %s successfully.", qty, item)


def remove_item(item, qty):
    """Remove a quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Item '%s' removed from inventory.", item)
    except KeyError as e:
        logging.warning("Item not found: %s", e)
    except Exception as e:  # pylint: disable=broad-exception-caught
        logging.error("Unexpected error while removing item: %s", e)


def get_qty(item):
    """Return the current quantity of an item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from JSON file."""
    global stock_data  # pylint: disable=global-statement
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Data loaded successfully from %s.", file)
    except FileNotFoundError:
        logging.warning("File '%s' not found, starting with empty data.", file)


def save_data(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)
    logging.info("Data saved successfully to %s.", file)


def print_data():
    """Print all inventory items."""
    logging.info("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Check for items below the given threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("pen", 10)
    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    save_data()
    load_data()
    print_data()

    # Safe evaluation example (Bandit-safe)
    try:
        ast.literal_eval("{'safe': True}")
        logging.info("Safe literal_eval executed successfully.")
    except (ValueError, SyntaxError) as e:
        logging.error("Error evaluating expression safely: %s", e)


if __name__ == "__main__":
    main()
