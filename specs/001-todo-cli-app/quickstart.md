# Quick Start Guide: Todo CLI App

**Version**: 1.0
**Last Updated**: 2026-01-04
**Status**: Complete ✅

## Prerequisites

- Python 3.13 or higher installed
- Terminal/Console access
- No additional dependencies required

## Installation

```bash
# Clone or download the repository
cd Todo_app_00

# No installation needed - pure Python standard library
```

## Running the Application

```bash
# From repository root
python src/main.py
```

## Menu Options

The application displays an interactive menu with the following options:

1. **Add Task** - Create a new todo task
2. **View Tasks** - Display all tasks with details
3. **Update Task** - Modify existing task title/description
4. **Delete Task** - Remove a task permanently
5. **Mark Complete** - Mark a task as completed
6. **Mark Incomplete** - Mark a task as not completed
7. **Exit** - Close the application

## Example Usage Session

Here's a complete workflow showing how to use the app:

```
$ python src/main.py

🎉 Welcome to Todo CLI App (Phase 1)!
Manage your tasks easily from the command line.

==================================================
          📝 TODO CLI APP - PHASE 1
==================================================

What would you like to do?

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Mark Incomplete
7. Exit

==================================================
Enter your choice (1-7): 1

--- ADD NEW TASK ---
Enter task title: Buy groceries
Enter task description (or press Enter to skip): Milk, bread, and eggs

✅ Task added successfully! (ID: 1)

----------------------------------------
Task ID: 1
Title: Buy groceries
Description: Milk, bread, and eggs
Status: Incomplete (❌)
----------------------------------------

Enter your choice (1-7): 1

--- ADD NEW TASK ---
Enter task title: Read Python book
Enter task description (or press Enter to skip): Chapter 5

✅ Task added successfully! (ID: 2)

Enter your choice (1-7): 2

================================================================================
📋 YOUR TASKS
================================================================================
ID    | Title                          | Status   | Description
--------------------------------------------------------------------------------
1     | Buy groceries                  | ❌       | Milk, bread, and eggs
2     | Read Python book               | ❌       | Chapter 5
================================================================================

Enter your choice (1-7): 5

--- MARK TASK AS COMPLETE ---
Enter task ID to mark complete: 1

✅ Task marked as complete!

----------------------------------------
Task ID: 1
Title: Buy groceries
Description: Milk, bread, and eggs
Status: Complete (✔)
----------------------------------------

Enter your choice (1-7): 2

================================================================================
📋 YOUR TASKS
================================================================================
ID    | Title                          | Status   | Description
--------------------------------------------------------------------------------
1     | Buy groceries                  | ✔        | Milk, bread, and eggs
2     | Read Python book               | ❌       | Chapter 5
================================================================================

Enter your choice (1-7): 7

👋 Thanks for using Todo CLI App! Goodbye!
```

## Troubleshooting

**Common Issues**:

- **Error: "No module named 'src'"**
  - Solution: Run from repository root directory

- **Error: "Invalid choice"**
  - Solution: Enter a number between 1-7

- **Unicode/Emoji Display Issues (Windows)**
  - Symptom: Checkmarks (✔/❌) don't display correctly
  - Solution: This is a Windows console limitation - functionality works fine

- **Application exits immediately**
  - Check you're running: `python src/main.py` from the repository root
  - Verify Python 3.13+ is installed: `python --version`

## Next Steps

After running the app:
- Create your first task
- Practice all CRUD operations
- Test edge cases (invalid IDs, empty inputs)

## File Structure

```
Todo_app_00/
├── src/
│   ├── __init__.py       # Package marker
│   ├── main.py           # Application entry point & CLI menu
│   ├── task.py           # Task data structure & validation
│   ├── task_manager.py   # CRUD operations & in-memory storage
│   └── utils.py          # Display & input helper functions
├── tests/
│   └── manual-test-checklist.md  # Testing scenarios
└── .gitignore            # Git ignore patterns

```

## Key Features

✅ Add tasks with title and optional description
✅ View all tasks in a formatted table
✅ Update task details (title/description)
✅ Delete tasks by ID
✅ Mark tasks as complete or incomplete
✅ Beginner-friendly code with extensive comments
✅ Input validation and error handling
✅ Clean CLI interface

## Limitations (Phase 1)

⚠️ **No Persistence**: All data is lost when the application exits
⚠️ **Single User**: No multi-user support
⚠️ **In-Memory Only**: No database or file storage

These limitations will be addressed in future phases.

---

**Implementation Complete**: 2026-01-04
**Total Lines of Code**: ~450 lines across 4 files
