"""
Quick Validation Script for Todo CLI App
Tests core functionality programmatically
"""

import sys
sys.path.insert(0, '../src')

import task
import task_manager

print("=" * 60)
print("QUICK VALIDATION TEST - Todo CLI App")
print("=" * 60)

# Test 1: Task Creation
print("\n[Test 1] Task Creation")
t1 = task.create_task(1, "Test Task", "Test Description")
assert t1['id'] == 1
assert t1['title'] == "Test Task"
assert t1['description'] == "Test Description"
assert t1['completed'] == False
print("  PASS - Task created correctly")

# Test 2: Title Validation
print("\n[Test 2] Title Validation")
assert task.validate_title("Valid Title") == True
assert task.validate_title("") == False
assert task.validate_title("   ") == False
print("  PASS - Validation works correctly")

# Test 3: Add Task to Manager
print("\n[Test 3] Add Task to Manager")
result = task_manager.add_task("First Task", "Description 1")
assert result is not None
assert result['id'] == 1
print(f"  PASS - Task added with ID {result['id']}")

# Test 4: Add Multiple Tasks
print("\n[Test 4] Add Multiple Tasks")
task_manager.add_task("Second Task", "Description 2")
task_manager.add_task("Third Task", "Description 3")
all_tasks = task_manager.get_all_tasks()
assert len(all_tasks) == 3
print(f"  PASS - {len(all_tasks)} tasks in list")

# Test 5: Get Task by ID
print("\n[Test 5] Get Task by ID")
found = task_manager.get_task_by_id(2)
assert found is not None
assert found['title'] == "Second Task"
print(f"  PASS - Found task: {found['title']}")

# Test 6: Update Task
print("\n[Test 6] Update Task")
updated = task_manager.update_task(1, title="Updated Title")
assert updated['title'] == "Updated Title"
assert updated['description'] == "Description 1"  # Unchanged
print("  PASS - Task updated successfully")

# Test 7: Mark Complete
print("\n[Test 7] Mark Complete")
completed = task_manager.mark_complete(1)
assert completed['completed'] == True
print("  PASS - Task marked complete")

# Test 8: Mark Incomplete
print("\n[Test 8] Mark Incomplete")
incomplete = task_manager.mark_incomplete(1)
assert incomplete['completed'] == False
print("  PASS - Task marked incomplete")

# Test 9: Delete Task
print("\n[Test 9] Delete Task")
deleted = task_manager.delete_task(2)
assert deleted is not None
assert deleted['title'] == "Second Task"
remaining = task_manager.get_all_tasks()
assert len(remaining) == 2
print(f"  PASS - Task deleted, {len(remaining)} remain")

# Test 10: Invalid Operations
print("\n[Test 10] Invalid Operations")
assert task_manager.add_task("", "Desc") is None  # Empty title
assert task_manager.get_task_by_id(999) is None   # Non-existent ID
assert task_manager.delete_task(999) is None      # Delete non-existent
print("  PASS - Invalid operations handled correctly")

print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
print("\nCore functionality is working correctly.")
print("Ready for manual CLI testing!")
