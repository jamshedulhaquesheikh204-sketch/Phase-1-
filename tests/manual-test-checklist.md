# Manual Test Checklist - Todo CLI App (Phase 1)

**Date**: 2026-01-04
**Tester**: _____________
**Version**: 1.0

## Prerequisites

- [ ] Python 3.13+ installed
- [ ] Application runs: `python src/main.py`
- [ ] Menu displays correctly

---

## User Story 1: Add and View Tasks (P1) 🎯 MVP

### Test 1.1: Add Task with Title + Description
- [ ] Select option 1 (Add Task)
- [ ] Enter title: "Buy groceries"
- [ ] Enter description: "Milk and bread"
- [ ] **Expected**: Success message with task ID 1
- [ ] **Expected**: Task details displayed

### Test 1.2: Add Task with Title Only
- [ ] Select option 1 (Add Task)
- [ ] Enter title: "Read book"
- [ ] Press Enter (skip description)
- [ ] **Expected**: Success message with task ID 2
- [ ] **Expected**: Task shows empty description

### Test 1.3: View Empty Task List
- [ ] Start fresh app (restart)
- [ ] Select option 2 (View Tasks)
- [ ] **Expected**: "No tasks yet" message displayed

### Test 1.4: View Multiple Tasks
- [ ] Add 3 tasks
- [ ] Select option 2 (View Tasks)
- [ ] **Expected**: All 3 tasks displayed in formatted table
- [ ] **Expected**: Shows ID, title, status (❌), description

---

## User Story 2: Mark Tasks Complete (P2)

### Test 2.1: Mark Incomplete Task as Complete
- [ ] Add task "Test task"
- [ ] Note its ID
- [ ] Select option 5 (Mark Complete)
- [ ] Enter the task ID
- [ ] **Expected**: Success message
- [ ] **Expected**: Task shows status ✔

### Test 2.2: Mark Complete Task as Incomplete
- [ ] Use task from Test 2.1
- [ ] Select option 6 (Mark Incomplete)
- [ ] Enter the task ID
- [ ] **Expected**: Success message
- [ ] **Expected**: Task shows status ❌

### Test 2.3: Mark with Invalid ID
- [ ] Select option 5 (Mark Complete)
- [ ] Enter ID 999 (doesn't exist)
- [ ] **Expected**: Error message "Task not found"

---

## User Story 3: Update Task Details (P3)

### Test 3.1: Update Task Title Only
- [ ] Add task "Old Title" / "Old Description"
- [ ] Note its ID
- [ ] Select option 3 (Update Task)
- [ ] Enter task ID
- [ ] Enter new title: "New Title"
- [ ] Press Enter (skip description)
- [ ] **Expected**: Title updated to "New Title"
- [ ] **Expected**: Description remains "Old Description"

### Test 3.2: Update Task Description Only
- [ ] Use existing task
- [ ] Select option 3 (Update Task)
- [ ] Enter task ID
- [ ] Press Enter (skip title)
- [ ] Enter new description: "New Description"
- [ ] **Expected**: Description updated to "New Description"
- [ ] **Expected**: Title unchanged

### Test 3.3: Update Both Title and Description
- [ ] Use existing task
- [ ] Select option 3 (Update Task)
- [ ] Enter task ID
- [ ] Enter new title
- [ ] Enter new description
- [ ] **Expected**: Both fields updated
- [ ] **Expected**: ID remains the same

---

## User Story 4: Delete Tasks (P4)

### Test 4.1: Delete Task by ID
- [ ] Add 5 tasks (IDs 1-5)
- [ ] Select option 4 (Delete Task)
- [ ] Enter ID 3
- [ ] **Expected**: Success message showing deleted task
- [ ] View tasks - **Expected**: Only tasks 1,2,4,5 remain

### Test 4.2: Delete with Invalid ID
- [ ] Select option 4 (Delete Task)
- [ ] Enter ID 999
- [ ] **Expected**: Error message "Task not found"

### Test 4.3: Delete Last Remaining Task
- [ ] Start with 1 task
- [ ] Delete that task
- [ ] View tasks
- [ ] **Expected**: "No tasks yet" message

---

## Edge Cases

### Edge 1: Empty Title
- [ ] Select option 1 (Add Task)
- [ ] Enter empty title (just press Enter)
- [ ] **Expected**: Error message "Title cannot be empty"

### Edge 2: Invalid Menu Choice
- [ ] Enter "99" at main menu
- [ ] **Expected**: Error message "Invalid choice"
- [ ] Enter "abc" at main menu
- [ ] **Expected**: Error message "Invalid choice"

### Edge 3: Non-Numeric ID
- [ ] Select any option requiring ID
- [ ] Enter "abc" when prompted for ID
- [ ] **Expected**: Error message "Please enter a valid number"
- [ ] **Expected**: Prompt repeats

### Edge 4: Negative ID
- [ ] Select any option requiring ID
- [ ] Enter "-5"
- [ ] **Expected**: Error message "ID must be a positive number"
- [ ] **Expected**: Prompt repeats

### Edge 5: Very Long Title
- [ ] Add task with 500 character title
- [ ] **Expected**: Task accepted
- [ ] View tasks - **Expected**: Title truncated in list view

### Edge 6: Exit Application
- [ ] Select option 7 (Exit)
- [ ] **Expected**: Goodbye message
- [ ] **Expected**: Application terminates gracefully

### Edge 7: Ctrl+C Interrupt
- [ ] Press Ctrl+C at any point
- [ ] **Expected**: Graceful exit with message
- [ ] **Expected**: No error trace

---

## Final Checks

- [ ] All 4 user stories tested and passing
- [ ] All edge cases handled correctly
- [ ] No crashes or unhandled exceptions
- [ ] Error messages are clear and helpful
- [ ] Success messages are displayed
- [ ] Application can be restarted without issues
- [ ] Data is properly lost on exit (no persistence)

---

## Test Results

**Total Tests**: 24
**Passed**: _____
**Failed**: _____
**Completion Date**: _____________
**Notes**:
