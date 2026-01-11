# Inventory Manager – Personal Stock Tracker

## Overview
**Inventory Manager** is a Python console application for managing inventory in a small store, pantry, or personal collection. Users can add items, update quantities, view inventory, and monitor low-stock alerts. Data is stored in a CSV file for persistence.

---

## Core Features
* **Add New Items**: Assign unique IDs, enter name, category, quantity, and packaging type.
* **Update Quantities**: Increase or decrease stock; quantities cannot go negative.
* **View Inventory**: Display all items or filter by category.
* **Low-Stock Alerts**: Identify items below a predefined threshold.

---

## Data Management
* **CSV Storage**: Load inventory from `inventory.csv` at startup and save changes on exit.
* **Columns**: `["id", "item_name", "category", "quantity", "packaging_type"]`.
* **Input Validation**: Ensures valid IDs, quantities, and categories.

---

## Architecture
* **Functions**:
    * `initialize_inventory()`
    * `add_item()`
    * `update_quantity()`
    * `view_inventory()`
    * `check_low_stock()`
* **Control Flow**: Menu-driven `main()` function routes actions to functions.
* **State Management**: Data stored in a DataFrame or dictionary; updated in real time.

---

## Limitations
* Console-based, single-user only.
* Not designed for enterprise-scale inventory.
* Optional features like visualization require extra libraries (`matplotlib`).

---

## Summary
A functional, modular Python inventory system using CSV storage and unique IDs for reliable tracking. Focuses on state management, input validation, and core inventory operations.
