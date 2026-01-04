"""
Main Application Module

This is the entry point for the Todo CLI App.
It provides a menu-driven interface for managing tasks.

Menu Options:
1. Add Task - Create a new todo item
2. View Tasks - Display all tasks in a formatted list
3. Update Task - Modify title/description of an existing task
4. Delete Task - Remove a task from the list
5. Mark Complete - Mark a task as completed
6. Mark Incomplete - Mark a task as not completed
7. Exit - Close the application

Author: Generated with Claude Code
Date: 2026-01-04
"""

import task_manager
import utils


def display_menu():
    """
    Display the main menu options to the user.

    This function prints the available commands and prompts
    for user input.
    """
    print("\n" + "=" * 50)
    print("          📝 TODO CLI APP - PHASE 1")
    print("=" * 50)
    print("\nWhat would you like to do?")
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Mark Incomplete")
    print("7. Exit")
    print("\n" + "=" * 50)


def handle_add_task():
    """
    Handle the 'Add Task' menu option.

    Prompts the user for task title and description,
    then creates and stores the new task.
    """
    print("\n--- ADD NEW TASK ---")

    # Get title (required)
    title = utils.get_user_input("Enter task title: ")

    # Validate title is not empty
    if not title:
        utils.show_error("Title cannot be empty!")
        return

    # Get description (optional)
    description = utils.get_user_input("Enter task description (or press Enter to skip): ")

    # Add the task
    new_task = task_manager.add_task(title, description)

    if new_task:
        utils.show_success(f"Task added successfully! (ID: {new_task['id']})")
        utils.display_task(new_task)
    else:
        utils.show_error("Failed to add task. Please try again.")


def handle_view_tasks():
    """
    Handle the 'View Tasks' menu option.

    Retrieves and displays all tasks in a formatted list.
    """
    all_tasks = task_manager.get_all_tasks()
    utils.display_tasks(all_tasks)


def handle_update_task():
    """
    Handle the 'Update Task' menu option.

    Prompts for task ID and new values, then updates the task.
    """
    print("\n--- UPDATE TASK ---")

    # Get task ID
    task_id = utils.get_valid_id("Enter task ID to update: ")

    # Check if task exists
    task = task_manager.get_task_by_id(task_id)
    if not task:
        utils.show_error(f"Task with ID {task_id} not found!")
        return

    # Show current task
    print("\nCurrent task:")
    utils.display_task(task)

    # Get new values (optional)
    print("Enter new values (or press Enter to keep current):")
    new_title = utils.get_user_input(f"New title (current: {task['title']}): ")
    new_description = utils.get_user_input(f"New description (current: {task['description']}): ")

    # Update task (only if user provided new values)
    title_to_update = new_title if new_title else None
    desc_to_update = new_description if new_description else None

    if title_to_update or desc_to_update:
        updated_task = task_manager.update_task(task_id, title_to_update, desc_to_update)
        if updated_task:
            utils.show_success("Task updated successfully!")
            utils.display_task(updated_task)
        else:
            utils.show_error("Failed to update task.")
    else:
        print("\nNo changes made.")


def handle_delete_task():
    """
    Handle the 'Delete Task' menu option.

    Prompts for task ID and removes the task from the list.
    """
    print("\n--- DELETE TASK ---")

    # Get task ID
    task_id = utils.get_valid_id("Enter task ID to delete: ")

    # Delete the task
    deleted_task = task_manager.delete_task(task_id)

    if deleted_task:
        utils.show_success(f"Task deleted successfully!")
        print(f"Deleted: {deleted_task['title']}")
    else:
        utils.show_error(f"Task with ID {task_id} not found!")


def handle_mark_complete():
    """
    Handle the 'Mark Complete' menu option.

    Prompts for task ID and marks it as completed.
    """
    print("\n--- MARK TASK AS COMPLETE ---")

    # Get task ID
    task_id = utils.get_valid_id("Enter task ID to mark complete: ")

    # Mark as complete
    task = task_manager.mark_complete(task_id)

    if task:
        utils.show_success(f"Task marked as complete!")
        utils.display_task(task)
    else:
        utils.show_error(f"Task with ID {task_id} not found!")


def handle_mark_incomplete():
    """
    Handle the 'Mark Incomplete' menu option.

    Prompts for task ID and marks it as not completed.
    """
    print("\n--- MARK TASK AS INCOMPLETE ---")

    # Get task ID
    task_id = utils.get_valid_id("Enter task ID to mark incomplete: ")

    # Mark as incomplete
    task = task_manager.mark_incomplete(task_id)

    if task:
        utils.show_success(f"Task marked as incomplete!")
        utils.display_task(task)
    else:
        utils.show_error(f"Task with ID {task_id} not found!")


def main():
    """
    Main application loop.

    Displays the menu and handles user choices until the user exits.
    """
    print("\n🎉 Welcome to Todo CLI App (Phase 1)!")
    print("Manage your tasks easily from the command line.\n")

    # Main loop - runs until user chooses to exit
    while True:
        try:
            # Show menu
            display_menu()

            # Get user choice
            choice = utils.get_user_input("Enter your choice (1-7): ")

            # Handle the choice
            if choice == "1":
                handle_add_task()
            elif choice == "2":
                handle_view_tasks()
            elif choice == "3":
                handle_update_task()
            elif choice == "4":
                handle_delete_task()
            elif choice == "5":
                handle_mark_complete()
            elif choice == "6":
                handle_mark_incomplete()
            elif choice == "7":
                print("\n👋 Thanks for using Todo CLI App! Goodbye!\n")
                break
            else:
                utils.show_error("Invalid choice! Please enter a number from 1 to 7.")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n👋 Interrupted by user. Goodbye!\n")
            break
        except Exception as e:
            # Catch any unexpected errors
            utils.show_error(f"An unexpected error occurred: {e}")
            print("The application will continue running. Please try again.")


# Entry point - this runs when you execute: python src/main.py
if __name__ == "__main__":
    main()
