"""
Task Manager Module

This module manages the in-memory storage and CRUD operations for tasks.
It maintains a global list of tasks and provides functions to:
- Add new tasks
- Retrieve all tasks or a specific task by ID
- Update existing tasks
- Delete tasks
- Mark tasks as complete or incomplete

Global Variables:
- tasks: List of all task dictionaries
- next_task_id: Counter for generating unique task IDs
"""

from task import create_task, validate_title

# GLOBAL STATE
# These variables store the application's data in memory
# Data will be lost when the program exits
tasks = []  # List to store all task dictionaries
next_task_id = 1  # Counter for generating unique IDs (starts at 1)


def add_task(title, description=""):
    """
    Add a new task to the task list.

    Args:
        title (str): Task title (required, must be non-empty)
        description (str): Task description (optional, defaults to empty string)

    Returns:
        dict or None: The created task if successful, None if title is invalid

    Example:
        >>> result = add_task("Buy groceries", "Milk and bread")
        >>> print(result['id'])
        1
    """
    global tasks, next_task_id

    # Validate the title first
    if not validate_title(title):
        return None

    # Create a new task with the current ID
    new_task = create_task(next_task_id, title, description)

    # Add the task to our list
    tasks.append(new_task)

    # Increment the ID counter for the next task
    next_task_id += 1

    return new_task


def get_all_tasks():
    """
    Retrieve all tasks in the system.

    Returns:
        list: A list of all task dictionaries

    Example:
        >>> all_tasks = get_all_tasks()
        >>> print(len(all_tasks))
        5
    """
    return tasks


def get_task_by_id(task_id):
    """
    Find and return a task with the given ID.

    Args:
        task_id (int): The ID of the task to find

    Returns:
        dict or None: The task dictionary if found, None otherwise

    Example:
        >>> task = get_task_by_id(3)
        >>> if task:
        ...     print(task['title'])
    """
    # Loop through all tasks to find the matching ID
    for task in tasks:
        if task["id"] == task_id:
            return task

    # If we didn't find it, return None
    return None


def update_task(task_id, title=None, description=None):
    """
    Update an existing task's title and/or description.

    Args:
        task_id (int): The ID of the task to update
        title (str, optional): New title (if provided)
        description (str, optional): New description (if provided)

    Returns:
        dict or None: The updated task if successful, None if task not found or validation fails

    Example:
        >>> updated = update_task(1, title="Buy groceries and fruit")
        >>> if updated:
        ...     print("Task updated successfully")
    """
    # Find the task
    task = get_task_by_id(task_id)
    if not task:
        return None

    # Update title if provided and valid
    if title is not None:
        if not validate_title(title):
            return None
        task["title"] = title

    # Update description if provided
    if description is not None:
        task["description"] = description

    return task


def delete_task(task_id):
    """
    Delete a task from the list by ID.

    Args:
        task_id (int): The ID of the task to delete

    Returns:
        dict or None: The deleted task if successful, None if task not found

    Example:
        >>> deleted = delete_task(2)
        >>> if deleted:
        ...     print(f"Deleted: {deleted['title']}")
    """
    global tasks

    # Find the task
    task = get_task_by_id(task_id)
    if not task:
        return None

    # Remove it from the list
    tasks.remove(task)

    return task


def mark_complete(task_id):
    """
    Mark a task as completed.

    Args:
        task_id (int): The ID of the task to mark complete

    Returns:
        dict or None: The updated task if successful, None if task not found

    Example:
        >>> task = mark_complete(1)
        >>> if task:
        ...     print(f"Completed: {task['completed']}")  # True
    """
    task = get_task_by_id(task_id)
    if not task:
        return None

    task["completed"] = True
    return task


def mark_incomplete(task_id):
    """
    Mark a task as incomplete.

    Args:
        task_id (int): The ID of the task to mark incomplete

    Returns:
        dict or None: The updated task if successful, None if task not found

    Example:
        >>> task = mark_incomplete(1)
        >>> if task:
        ...     print(f"Completed: {task['completed']}")  # False
    """
    task = get_task_by_id(task_id)
    if not task:
        return None

    task["completed"] = False
    return task
