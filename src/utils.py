"""
Utility Module

This module provides helper functions for:
- Displaying tasks in a formatted way
- Getting validated user input
- Showing success and error messages

Functions:
- display_tasks(tasks): Show a list of tasks in a formatted table
- display_task(task): Show details of a single task
- get_user_input(prompt): Get and return user input as a string
- get_valid_id(prompt): Get and validate an integer ID from user
- show_success(message): Display a success message
- show_error(message): Display an error message
"""


def display_tasks(tasks):
    """
    Display a formatted list of all tasks.

    Args:
        tasks (list): List of task dictionaries to display

    Example output:
        ID  | Title         | Status | Description
        ----|---------------|--------|------------------
        1   | Buy groceries | ❌     | Milk and bread
        2   | Read book     | ✔      | Finish chapter 3
    """
    # Handle empty list
    if not tasks or len(tasks) == 0:
        print("\n📋 No tasks yet. Add one to get started!\n")
        return

    # Print header
    print("\n" + "=" * 80)
    print("📋 YOUR TASKS")
    print("=" * 80)
    print(f"{'ID':<5} | {'Title':<30} | {'Status':<8} | {'Description':<25}")
    print("-" * 80)

    # Print each task
    for task in tasks:
        # Determine status symbol
        status = "✔" if task["completed"] else "❌"

        # Truncate long strings for display
        title = task["title"][:30]
        description = task["description"][:25] if task["description"] else ""

        print(f"{task['id']:<5} | {title:<30} | {status:<8} | {description:<25}")

    print("=" * 80 + "\n")


def display_task(task):
    """
    Display detailed information about a single task.

    Args:
        task (dict): The task dictionary to display

    Example output:
        Task ID: 1
        Title: Buy groceries
        Description: Milk and bread
        Status: Incomplete (❌)
    """
    status_text = "Complete (✔)" if task["completed"] else "Incomplete (❌)"

    print("\n" + "-" * 40)
    print(f"Task ID: {task['id']}")
    print(f"Title: {task['title']}")
    print(f"Description: {task['description']}")
    print(f"Status: {status_text}")
    print("-" * 40 + "\n")


def get_user_input(prompt):
    """
    Get input from the user and return it as a trimmed string.

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        str: The user's input with leading/trailing whitespace removed

    Example:
        >>> title = get_user_input("Enter task title: ")
    """
    user_input = input(prompt)
    return user_input.strip()


def get_valid_id(prompt):
    """
    Get a valid integer ID from the user.

    Keeps asking until the user provides a valid positive integer.

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        int: A valid positive integer ID

    Example:
        >>> task_id = get_valid_id("Enter task ID: ")
    """
    while True:
        try:
            # Try to convert input to integer
            user_input = get_user_input(prompt)
            task_id = int(user_input)

            # Check if it's positive
            if task_id <= 0:
                show_error("ID must be a positive number. Please try again.")
                continue

            return task_id

        except ValueError:
            # User entered something that's not a number
            show_error("Please enter a valid number.")


def show_success(message):
    """
    Display a success message in a formatted way.

    Args:
        message (str): The success message to display

    Example:
        >>> show_success("Task added successfully!")
        ✅ Task added successfully!
    """
    print(f"\n✅ {message}\n")


def show_error(message):
    """
    Display an error message in a formatted way.

    Args:
        message (str): The error message to display

    Example:
        >>> show_error("Task not found")
        ❌ Task not found
    """
    print(f"\n❌ {message}\n")
