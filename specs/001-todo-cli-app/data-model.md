# Data Model: Todo CLI App (Phase 1)

**Feature**: 001-todo-cli-app
**Created**: 2026-01-04
**Purpose**: Define data structures and storage strategy for in-memory todo management

## Overview

This document defines the data model for Phase 1 of the Todo CLI App. The model uses simple Python dictionaries for tasks, stored in a global list with counter-based ID generation.

## Entity: Task

### Structure

**Representation**: Python dictionary

```python
{
    "id": int,           # Unique identifier (auto-generated)
    "title": str,        # Task title (required, non-empty)
    "description": str,  # Task description (optional, can be empty)
    "completed": bool    # Completion status (default: False)
}
```

### Field Specifications

| Field | Type | Required | Constraints | Default | Notes |
|-------|------|----------|-------------|---------|-------|
| `id` | int | Yes | > 0, unique | Auto-generated | Never reused after deletion |
| `title` | str | Yes | len > 0 | N/A | Must be non-empty string |
| `description` | str | No | None | "" (empty string) | Can be empty or omitted |
| `completed` | bool | Yes | True or False | False | Toggle via mark_complete/incomplete |

### Validation Rules

**Title Validation**:
```python
def validate_title(title):
    """
    Validate task title.

    Rules:
    - Must be a string
    - Must not be empty (after stripping whitespace)
    - No maximum length (but display may truncate)

    Returns: True if valid, False otherwise
    """
    return isinstance(title, str) and len(title.strip()) > 0
```

**Description Validation**:
```python
# No validation required - any string accepted (including empty)
# Description is always optional
```

**ID Validation**:
```python
def validate_id(task_id):
    """
    Validate task ID format.

    Rules:
    - Must be an integer
    - Must be positive (> 0)

    Returns: True if valid, False otherwise
    """
    return isinstance(task_id, int) and task_id > 0
```

### Example Task

```python
# Minimal task (with empty description)
{
    "id": 1,
    "title": "Buy groceries",
    "description": "",
    "completed": False
}

# Complete task (with description and completed)
{
    "id": 2,
    "title": "Finish project report",
    "description": "Include sections on methodology and results",
    "completed": True
}
```

## Storage Strategy

### In-Memory Storage

**Location**: `src/task_manager.py` (global module-level variables)

**Structure**:
```python
# Global state variables
tasks = []           # List[dict] - stores all task dictionaries
next_task_id = 1     # int - counter for generating unique IDs
```

**Characteristics**:
- **Persistence**: None - data lost on application exit
- **Capacity**: Limited by available RAM (target: 100 tasks)
- **Thread Safety**: Not required (single-threaded CLI app)
- **Access Pattern**: Linear search by ID (acceptable for small datasets)

### ID Generation Algorithm

**Strategy**: Sequential counter-based ID assignment

**Implementation**:
```python
def add_task(title, description=""):
    global tasks, next_task_id

    # Create task with current ID
    task = {
        "id": next_task_id,
        "title": title,
        "description": description,
        "completed": False
    }

    # Add to storage
    tasks.append(task)

    # Increment for next task
    next_task_id += 1

    return task
```

**Properties**:
- ✅ Unique: Each task gets a distinct ID
- ✅ Sequential: IDs increment in order (1, 2, 3, ...)
- ✅ Permanent: IDs never reused (even after deletion)
- ✅ Simple: No UUID library required
- ⚠️  Not gap-free: Deleted task IDs leave gaps (acceptable)

**Example Sequence**:
```
Add task → ID 1
Add task → ID 2
Add task → ID 3
Delete task ID 2
Add task → ID 4  (NOT 2 - never reuse)
```

## CRUD Operations Data Flow

### Create (Add Task)

```
User Input (title, description)
    ↓
Validate title (non-empty)
    ↓
Create task dict with next_task_id
    ↓
Append to tasks list
    ↓
Increment next_task_id
    ↓
Return success + new task
```

### Read (View Tasks)

```
Request to view tasks
    ↓
Return tasks list (all tasks)
    ↓
Display each task with formatting
```

### Update (Modify Task)

```
User Input (task_id, new_title?, new_description?)
    ↓
Find task in tasks list by ID
    ↓
If found: Update fields
    ↓
Return success + updated task
```

### Delete (Remove Task)

```
User Input (task_id)
    ↓
Find task in tasks list by ID
    ↓
If found: Remove from list
    ↓
Return success + deleted task details
    ↓
(next_task_id remains unchanged)
```

### Toggle Completion

```
User Input (task_id, new_status)
    ↓
Find task in tasks list by ID
    ↓
If found: Set completed = new_status
    ↓
Return success + updated task
```

## State Transitions

### Task Lifecycle

```
[Created]
   |
   v
completed = False (Incomplete)
   |
   | mark_complete()
   v
completed = True (Complete)
   |
   | mark_incomplete()
   v
completed = False (Incomplete)
   |
   | delete_task()
   v
[Deleted from list]
```

**Valid Transitions**:
- Incomplete → Complete (mark_complete)
- Complete → Incomplete (mark_incomplete)
- Any State → Deleted (delete_task)

**Invalid Transitions**: None - all states are reversible

## Data Integrity Constraints

### Enforced Constraints

1. **Unique IDs**: Guaranteed by counter-based generation
2. **Non-empty Titles**: Validated before task creation
3. **Boolean Completion**: Type enforced by Python (True/False only)

### Not Enforced (Acceptable for Phase 1)

1. **Maximum Task Count**: No limit (relies on RAM)
2. **Title/Description Length**: No maximum (display may truncate)
3. **Duplicate Titles**: Allowed (different tasks can have same title)
4. **Task Ordering**: Insertion order maintained by list (no explicit sorting)

## Performance Characteristics

### Time Complexity

| Operation | Complexity | Notes |
|-----------|------------|-------|
| Add Task | O(1) | Append to list + increment counter |
| View All Tasks | O(n) | Iterate through n tasks |
| Find by ID | O(n) | Linear search through list |
| Update Task | O(n) | Find (O(n)) + update (O(1)) |
| Delete Task | O(n) | Find (O(n)) + remove (O(n)) |
| Mark Complete | O(n) | Find (O(n)) + update (O(1)) |

**Impact**: For 100 tasks, linear search is acceptable (< 1ms on modern hardware)

### Space Complexity

- **Per Task**: ~200 bytes (estimate for dict with 4 fields)
- **100 Tasks**: ~20 KB
- **Global State**: Negligible overhead

**Verdict**: Memory usage is trivial for target scale

## Migration Path (Future Phases)

### Phase 2: File Persistence

**Changes Required**:
- Add JSON serialization (dump/load)
- Save tasks list on exit
- Load tasks list on startup
- Persist next_task_id value

**Data Model**: Unchanged (same dict structure)

### Phase 3: Database Storage

**Changes Required**:
- Map dict fields to SQL columns
- Replace list with database queries
- Use database auto-increment for IDs

**Data Model**:
```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT DEFAULT '',
    completed BOOLEAN DEFAULT FALSE
);
```

## Testing Considerations

### Data Validation Tests

1. **Valid Task Creation**:
   - Title: "Test", Description: "Details" → Success
   - Title: "Test", Description: "" → Success (empty description OK)

2. **Invalid Task Creation**:
   - Title: "", Description: "Details" → Reject (empty title)
   - Title: "   ", Description: "Details" → Reject (whitespace-only title)

3. **ID Uniqueness**:
   - Create 10 tasks → All have distinct IDs (1-10)
   - Delete task 5 → Next task gets ID 11 (not 5)

### Edge Cases

1. **Empty List Operations**:
   - View tasks on empty list → Show "No tasks" message
   - Update non-existent ID → Show "Task not found"
   - Delete non-existent ID → Show "Task not found"

2. **Boundary Conditions**:
   - 100 tasks → All operations < 1 second
   - Very long title (500+ chars) → Accept but may truncate display

---

**Version**: 1.0
**Last Updated**: 2026-01-04
**Status**: Ready for implementation
