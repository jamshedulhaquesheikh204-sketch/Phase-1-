"""
Task Data Module

This module defines the Task data structure and validation functions.
A Task is represented as a Python dictionary with the following fields:
- id: int (unique identifier, auto-generated)
- title: str (task title, required)
- description: str (task description, optional)
- completed: bool (completion status, default False)

Functions:
- validate_title(title): Check if a title is valid (non-empty string)
- create_task(task_id, title, description): Create a new task dictionary
"""


def validate_title(title):
    """
    Validate that a task title is acceptable.

    A valid title must be:
    - A string type
    - Non-empty after removing whitespace

    Args:
        title: The title to validate (should be a string)

    Returns:
        bool: True if title is valid, False otherwise

    Examples:
        >>> validate_title("Buy groceries")
        True
        >>> validate_title("")
        False
        >>> validate_title("   ")
        False
        >>> validate_title(123)
        False
    """
    # Check if title is a string
    if not isinstance(title, str):
        return False

    # Check if title is not empty after removing whitespace
    if len(title.strip()) == 0:
        return False

    return True


def create_task(task_id, title, description=""):
    """
    Create a new task dictionary with the given information.

    Args:
        task_id (int): Unique identifier for the task
        title (str): Task title (required)
        description (str): Task description (optional, defaults to empty string)

    Returns:
        dict: A task dictionary with keys: id, title, description, completed

    Example:
        >>> task = create_task(1, "Buy milk", "Get 2% milk from store")
        >>> print(task)
        {'id': 1, 'title': 'Buy milk', 'description': 'Get 2% milk from store', 'completed': False}
    """
    # Create and return a dictionary representing the task
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "completed": False  # New tasks are always incomplete
    }
