# Implementation Plan: Todo CLI App (Phase 1)

**Branch**: `001-todo-cli-app` | **Date**: 2026-01-04 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-todo-cli-app/spec.md`

## Summary

Build a beginner-friendly, in-memory Todo CLI application in Python that allows users to manage tasks through a simple menu-driven interface. The app will support CRUD operations (Create, Read, Update, Delete) plus task completion tracking, all stored in a Python list with zero persistence.

**Technical Approach**: Pure Python 3.13+ with standard library only, simple procedural programming with clear function separation, CLI menu loop pattern.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Python standard library only (sys, os optional for screen management)
**Storage**: In-memory Python list (no files, no database)
**Testing**: Manual testing via CLI interaction (automated tests out of scope for Phase 1)
**Target Platform**: Cross-platform (Windows, macOS, Linux) - any terminal/console
**Project Type**: Single project - CLI application
**Performance Goals**: < 1 second for any operation with up to 100 tasks
**Constraints**: No external dependencies, no persistence, beginner-readable code
**Scale/Scope**: Single user, up to 100 tasks per session, 3 source files

## Constitution Check

*No constitution file found - skipping gate checks*

**Beginner-Friendly Principles** (from user requirements):
- ✅ Keep code simple and readable
- ✅ Follow single responsibility per function
- ✅ Use in-memory storage (Python list)
- ✅ No database, files, or external services
- ✅ No over-engineering (no unnecessary classes)
- ✅ CLI only (print + input)
- ✅ Beginner-friendly structure and naming

## Project Structure

### Documentation (this feature)

```text
specs/001-todo-cli-app/
├── spec.md              ✅ Complete (specification)
├── plan.md              ← This file (implementation plan)
├── research.md          ⚠️  Not needed (no research required - simple CLI)
├── data-model.md        ← To be created (Phase 0)
├── quickstart.md        ← To be created (Phase 1)
└── checklists/
    └── requirements.md  ✅ Complete (validation checklist)
```

### Source Code (repository root)

```text
src/
├── __init__.py          # Empty package marker
├── main.py              # Entry point + menu loop
├── task.py              # Task data structure (dict-based)
├── task_manager.py      # CRUD operations on task list
└── utils.py             # Helper functions (input validation, display)

tests/
└── manual-test-checklist.md  # Manual test scenarios
```

**Structure Decision**: Single project structure chosen because:
- Simple CLI application with no web/mobile components
- All code fits in one package
- No need for frontend/backend separation
- Beginner-friendly - everything in one place

## Architecture Overview

### Data Flow Pattern

```
User Input (stdin)
    ↓
main.py (menu loop)
    ↓
task_manager.py (business logic)
    ↓
task.py (data validation)
    ↓
In-Memory List (global state)
    ↓
utils.py (formatting)
    ↓
Display Output (stdout)
```

### Key Design Decisions

**1. Data Structure**: Dictionary-based tasks stored in a list
```python
# Task structure (dictionary):
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk and bread",
    "completed": False
}

# Storage: tasks = []  # Global list in task_manager.py
```

**2. ID Generation**: Simple counter-based approach
- Start at 1
- Increment for each new task
- Never reuse IDs (even after deletion)

**3. Menu Pattern**: Numbered menu with input loop
- Display options 1-7
- Read user choice
- Dispatch to appropriate function
- Loop until user selects "Exit"

## File-by-File Responsibilities

### `src/main.py` (Entry Point)
**Purpose**: Application entry and menu orchestration

**Responsibilities**:
- Display main menu
- Read user menu choice
- Route to task_manager functions
- Handle graceful exit
- Main loop control

**Key Functions**:
- `display_menu()` → Print menu options
- `main()` → Main application loop

**Imports**: `task_manager`, `utils`

---

### `src/task.py` (Data Layer)
**Purpose**: Task data structure and validation

**Responsibilities**:
- Define task structure (as dict template)
- Validate task data (title non-empty)
- Create new task dict with auto-ID
- No state management (stateless functions)

**Key Functions**:
- `create_task(task_id, title, description)` → Return task dict
- `validate_title(title)` → Return True/False

**Imports**: None (pure Python)

---

### `src/task_manager.py` (Business Logic)
**Purpose**: CRUD operations and state management

**Responsibilities**:
- Maintain global tasks list
- Implement all CRUD operations
- Generate new task IDs
- Find tasks by ID
- Update task fields
- Delete tasks
- Toggle completion status

**Key Functions**:
- `add_task(title, description)` → Success message
- `get_all_tasks()` → Return tasks list
- `get_task_by_id(task_id)` → Return task or None
- `update_task(task_id, title, description)` → Success/error message
- `delete_task(task_id)` → Success/error message + deleted task
- `mark_complete(task_id)` → Success/error message
- `mark_incomplete(task_id)` → Success/error message

**Global State**:
```python
tasks = []           # List of task dicts
next_task_id = 1     # Auto-increment counter
```

**Imports**: `task` (for validation and creation)

---

### `src/utils.py` (Helper Functions)
**Purpose**: Input/output utilities

**Responsibilities**:
- Format task list for display
- Validate user input (ID format, non-empty strings)
- Display success/error messages
- Pretty-print task details

**Key Functions**:
- `display_tasks(tasks)` → Print formatted task list
- `display_task(task)` → Print single task details
- `get_user_input(prompt)` → Read and return trimmed input
- `get_valid_id(prompt)` → Read and validate integer ID
- `show_success(message)` → Print success message
- `show_error(message)` → Print error message

**Imports**: None (pure Python)

---

## Implementation Phases

### Phase 0: Data Model Design

**Objective**: Define data structures before coding

**Deliverable**: `data-model.md` documenting:
- Task entity structure (fields, types, constraints)
- In-memory storage strategy (list of dicts)
- ID generation algorithm (counter-based)
- Validation rules (title required, description optional)

**Why first**: Prevents rework - everyone agrees on data shape

---

### Phase 1: Core Data Layer

**Objective**: Build task.py first (data without logic)

**Order**:
1. Create `src/__init__.py` (empty file)
2. Create `src/task.py`:
   - `create_task()` function
   - `validate_title()` function
3. Test manually in Python REPL

**Verification**:
```python
# In Python REPL:
from src.task import create_task, validate_title
task = create_task(1, "Test", "Description")
print(task)  # Should show dict with all fields
```

**Risk**: None - pure functions, no dependencies

---

### Phase 2: State Management Layer

**Objective**: Build task_manager.py (business logic + state)

**Order**:
1. Create `src/task_manager.py`
2. Implement global variables (`tasks`, `next_task_id`)
3. Implement `add_task()` first (creates and stores)
4. Implement `get_all_tasks()` (simple retrieval)
5. Implement `get_task_by_id()` (find helper)
6. Implement `update_task()` (modify existing)
7. Implement `delete_task()` (remove from list)
8. Implement `mark_complete()` / `mark_incomplete()` (toggle status)

**Verification**:
```python
# In Python REPL:
from src.task_manager import add_task, get_all_tasks
add_task("Task 1", "Description")
add_task("Task 2", "Description")
print(get_all_tasks())  # Should show 2 tasks
```

**Risk**: Global state management
- **Mitigation**: Keep functions pure (input → output), only modify global in one place

---

### Phase 3: Display Utilities

**Objective**: Build utils.py (formatting and input helpers)

**Order**:
1. Create `src/utils.py`
2. Implement `display_tasks()` (pretty-print list)
3. Implement `display_task()` (single task details)
4. Implement `get_user_input()` (read with trim)
5. Implement `get_valid_id()` (read + validate integer)
6. Implement `show_success()` / `show_error()` (colored/formatted messages)

**Verification**:
```python
# In Python REPL:
from src.utils import display_tasks
from src.task_manager import get_all_tasks
display_tasks(get_all_tasks())  # Should show formatted output
```

**Risk**: Input validation edge cases
- **Mitigation**: Test with empty strings, non-integers, negative numbers

---

### Phase 4: Menu and Main Loop

**Objective**: Build main.py (tie everything together)

**Order**:
1. Create `src/main.py`
2. Implement `display_menu()` (print 7 options)
3. Implement menu handlers:
   - `handle_add_task()` → Get input, call task_manager.add_task()
   - `handle_view_tasks()` → Call get_all_tasks(), display with utils
   - `handle_update_task()` → Get ID + new data, call update_task()
   - `handle_delete_task()` → Get ID, call delete_task()
   - `handle_mark_complete()` → Get ID, call mark_complete()
   - `handle_mark_incomplete()` → Get ID, call mark_incomplete()
4. Implement `main()` loop:
   - Display menu
   - Get choice
   - Route to handler
   - Repeat until exit

**Verification**:
```bash
python src/main.py
# Test each menu option manually
```

**Risk**: Menu loop logic, invalid input handling
- **Mitigation**: Use try-except blocks, validate all user input before processing

---

### Phase 5: Integration Testing

**Objective**: End-to-end testing via manual checklist

**Order**:
1. Create `tests/manual-test-checklist.md`
2. Test each user story from spec:
   - Add tasks (P1)
   - View tasks (P1)
   - Mark complete (P2)
   - Update tasks (P3)
   - Delete tasks (P4)
3. Test all edge cases from spec
4. Document any bugs found

**Verification**: All acceptance scenarios pass

**Risk**: Edge cases not tested
- **Mitigation**: Follow spec checklist exactly, test negative cases

---

### Phase 6: Documentation

**Objective**: Create quickstart.md for users

**Order**:
1. Create `specs/001-todo-cli-app/quickstart.md`
2. Document:
   - How to run the app
   - Menu options explained
   - Example usage session
   - Troubleshooting (common errors)

**Verification**: New user can run app following quickstart only

---

## Implementation Milestones

| Milestone | Deliverable | Verification |
|-----------|-------------|--------------|
| M1 | data-model.md created | Data structures documented |
| M2 | task.py complete | Can create task dicts in REPL |
| M3 | task_manager.py complete | Can add/retrieve tasks in REPL |
| M4 | utils.py complete | Can display formatted tasks |
| M5 | main.py complete | App runs with full menu |
| M6 | All tests passing | Manual checklist 100% green |
| M7 | quickstart.md complete | New user can run app |

## Risks and Mitigation Strategies

### Beginner-Level Risks

**Risk 1: Global State Confusion**
- **Problem**: Beginners may struggle with global variables in task_manager.py
- **Symptom**: Tasks not persisting between function calls
- **Mitigation**:
  - Use clear comments explaining global vs. local scope
  - Keep all global state in ONE file only (task_manager.py)
  - Never modify tasks list outside task_manager.py

**Risk 2: Input Validation Gaps**
- **Problem**: Forgetting to validate user input leads to crashes
- **Symptom**: ValueError, IndexError, KeyError exceptions
- **Mitigation**:
  - Centralize all input reading in utils.py
  - Use try-except blocks for all user input
  - Test with malicious input (empty strings, special chars, negative numbers)

**Risk 3: ID Management Errors**
- **Problem**: Reusing IDs after deletion causes data corruption
- **Symptom**: Wrong tasks being updated/deleted
- **Mitigation**:
  - Never decrement next_task_id
  - Never reuse IDs
  - Document this clearly in code comments

**Risk 4: Menu Loop Logic**
- **Problem**: Infinite loops or unexpected exits
- **Symptom**: Can't exit app, or app crashes on invalid choice
- **Mitigation**:
  - Use explicit exit flag or option
  - Validate menu choice before routing
  - Provide clear exit instructions

**Risk 5: Import Errors**
- **Problem**: Circular imports or missing __init__.py
- **Symptom**: ImportError, ModuleNotFoundError
- **Mitigation**:
  - Create __init__.py in src/ immediately
  - Follow import order: task → task_manager → main
  - Never import main.py into other modules

**Risk 6: Function Naming Confusion**
- **Problem**: Similar function names in different files
- **Symptom**: Calling wrong function, unexpected behavior
- **Mitigation**:
  - Use clear prefixes: display_ for output, get_ for retrieval, handle_ for menu actions
  - Keep function names descriptive and unique
  - Document each function with docstring

## Testing Strategy

### Manual Testing Checklist

**Location**: `tests/manual-test-checklist.md`

**Structure**:
```markdown
## P1: Add and View Tasks
- [ ] Add task with title + description
- [ ] Add task with title only (empty description)
- [ ] View empty task list
- [ ] View list with 1 task
- [ ] View list with 5+ tasks

## P2: Mark Complete
- [ ] Mark incomplete task as complete
- [ ] Mark complete task as incomplete
- [ ] Verify status displays correctly in list

[... and so on for each priority]
```

**Execution**: Run app, follow checklist, mark each item pass/fail

### Edge Case Testing

**Critical Tests**:
1. Empty title → Should reject with error
2. Invalid task ID → Should show "Task not found"
3. Non-numeric ID input → Should show "Please enter a number"
4. Menu choice out of range → Should show "Invalid choice"
5. Empty task list operations → Should handle gracefully
6. 100+ tasks → Should remain fast (< 1 second)

## Success Criteria Mapping

| Success Criteria | How to Verify | Target |
|------------------|---------------|--------|
| SC-001: Add task in <10s | Time from menu select to confirmation | < 10 seconds |
| SC-002: View tasks <1s | Time to display task list | < 1 second |
| SC-003: All CRUD operations work | Manual checklist 100% pass | All green |
| SC-004: No crashes on invalid input | Test all edge cases | 0 crashes |
| SC-005: Clear feedback messages | Review all output messages | 100% clear |
| SC-006: 100 tasks no degradation | Add 100 tasks, test operations | < 1 second |
| SC-007: 10+ operations no corruption | Perform 20 mixed operations | 0 errors |
| SC-008: New user understands in 5min | Give quickstart to new user | < 5 minutes |

## Next Steps After Planning

1. **Create data-model.md**: Document Task structure and storage strategy
2. **Create quickstart.md**: Skeleton only (fill after M5)
3. **Run `/sp.tasks`**: Generate detailed task breakdown from this plan
4. **Begin implementation**: Follow phases 1→6 in order

---

**Plan Version**: 1.0
**Last Updated**: 2026-01-04
**Status**: Ready for `/sp.tasks`
