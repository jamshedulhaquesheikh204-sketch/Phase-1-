# Tasks: Todo CLI App (Phase 1)

**Input**: Design documents from `specs/001-todo-cli-app/`
**Prerequisites**: plan.md, spec.md, data-model.md

**Tests**: Manual testing only (no automated tests for Phase 1)

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

## Format: `- [ ] [ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: User story this task belongs to (US1, US2, US3, US4)
- File paths included in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and directory structure

- [ ] T001 Verify Python 3.13+ installed by running `python --version`
- [ ] T002 Create src/ directory in repository root
- [ ] T003 Create tests/ directory in repository root
- [ ] T004 Create empty src/__init__.py file to mark package

**Checkpoint**: ✅ Project structure ready

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data structures and utilities that ALL user stories depend on

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 [P] Create src/task.py with module docstring
- [ ] T006 [P] Define Task dictionary structure as comment in src/task.py (id, title, description, completed)
- [ ] T007 [P] Implement validate_title(title) function in src/task.py
- [ ] T008 [P] Implement create_task(task_id, title, description) function in src/task.py
- [ ] T009 [P] Create src/task_manager.py with module docstring
- [ ] T010 [P] Initialize global variables in src/task_manager.py: tasks = [] and next_task_id = 1
- [ ] T011 [P] Create src/utils.py with module docstring

**Checkpoint**: ✅ Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks and view all tasks in a formatted list

**Independent Test**: Launch app, add task "Buy groceries" with description "Milk and bread", view tasks, confirm task appears with ID 1 and correct details

**Acceptance Criteria**:
- User can add task with title + description
- User can add task with title only (empty description)
- User can view empty task list (shows "No tasks yet")
- User can view list with multiple tasks
- Each task displays ID, title, description, completion status

### Implementation Tasks

- [ ] T012 [US1] Implement add_task(title, description="") in src/task_manager.py
- [ ] T013 [US1] Implement get_all_tasks() in src/task_manager.py
- [ ] T014 [P] [US1] Implement display_tasks(tasks) in src/utils.py with formatted output
- [ ] T015 [P] [US1] Implement display_task(task) in src/utils.py for single task display
- [ ] T016 [P] [US1] Implement get_user_input(prompt) in src/utils.py
- [ ] T017 [P] [US1] Implement show_success(message) in src/utils.py
- [ ] T018 [P] [US1] Implement show_error(message) in src/utils.py
- [ ] T019 [US1] Create src/main.py with module docstring
- [ ] T020 [US1] Implement display_menu() function in src/main.py
- [ ] T021 [US1] Implement handle_add_task() function in src/main.py
- [ ] T022 [US1] Implement handle_view_tasks() function in src/main.py
- [ ] T023 [US1] Implement main() function with menu loop in src/main.py
- [ ] T024 [US1] Add if __name__ == "__main__": main() to src/main.py
- [ ] T025 [US1] Test adding task with title + description
- [ ] T026 [US1] Test adding task with title only (empty description)
- [ ] T027 [US1] Test viewing empty task list
- [ ] T028 [US1] Test viewing list with 3+ tasks

**Checkpoint**: ✅ MVP Complete - App can add and display tasks

---

## Phase 4: User Story 2 - Mark Tasks Complete (Priority: P2)

**Goal**: Users can mark tasks as complete or incomplete to track progress

**Independent Test**: Add 3 tasks, mark task ID 2 as complete, verify status changes to "✔" in list, mark incomplete, verify status changes to "❌"

**Acceptance Criteria**:
- User can mark incomplete task as complete by ID
- User can mark complete task as incomplete by ID
- Task status displays correctly in list (✔ / ❌)
- Only specified task status changes (others unchanged)
- Error shown for invalid task ID

### Implementation Tasks

- [ ] T029 [US2] Implement get_task_by_id(task_id) in src/task_manager.py
- [ ] T030 [P] [US2] Implement mark_complete(task_id) in src/task_manager.py
- [ ] T031 [P] [US2] Implement mark_incomplete(task_id) in src/task_manager.py
- [ ] T032 [P] [US2] Implement get_valid_id(prompt) in src/utils.py with validation
- [ ] T033 [US2] Implement handle_mark_complete() in src/main.py
- [ ] T034 [US2] Implement handle_mark_incomplete() in src/main.py
- [ ] T035 [US2] Add "Mark Complete" option to display_menu() in src/main.py
- [ ] T036 [US2] Add "Mark Incomplete" option to display_menu() in src/main.py
- [ ] T037 [US2] Update main() menu routing to include mark complete/incomplete handlers
- [ ] T038 [US2] Test marking incomplete task as complete
- [ ] T039 [US2] Test marking complete task as incomplete
- [ ] T040 [US2] Test marking with invalid task ID (shows error)
- [ ] T041 [US2] Test that only specified task status changes

**Checkpoint**: ✅ Users can track task completion

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Users can modify task title and/or description when needed

**Independent Test**: Add task "Old Title" / "Old Desc", update title to "New Title", verify title changed and description unchanged

**Acceptance Criteria**:
- User can update task title only
- User can update task description only
- User can update both title and description
- Task ID remains unchanged after update
- Error shown for invalid task ID
- Error shown for empty title

### Implementation Tasks

- [ ] T042 [US3] Implement update_task(task_id, title=None, description=None) in src/task_manager.py
- [ ] T043 [US3] Implement handle_update_task() in src/main.py
- [ ] T044 [US3] Add "Update Task" option to display_menu() in src/main.py
- [ ] T045 [US3] Update main() menu routing to include update handler
- [ ] T046 [US3] Test updating task title only
- [ ] T047 [US3] Test updating task description only
- [ ] T048 [US3] Test updating both title and description
- [ ] T049 [US3] Test updating with invalid task ID (shows error)
- [ ] T050 [US3] Test updating with empty title (shows error)

**Checkpoint**: ✅ Users can modify task details

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Users can remove tasks that are no longer needed

**Independent Test**: Add 5 tasks, delete task ID 3, verify only tasks 1,2,4,5 remain in list

**Acceptance Criteria**:
- User can delete task by ID
- Deleted task no longer appears in list
- Other tasks remain unchanged
- Confirmation shown with deleted task details
- Error shown for invalid task ID
- Empty list handled correctly after deleting last task

### Implementation Tasks

- [ ] T051 [US4] Implement delete_task(task_id) in src/task_manager.py
- [ ] T052 [US4] Implement handle_delete_task() in src/main.py
- [ ] T053 [US4] Add "Delete Task" option to display_menu() in src/main.py
- [ ] T054 [US4] Update main() menu routing to include delete handler
- [ ] T055 [US4] Test deleting task from middle of list
- [ ] T056 [US4] Test deleting task with invalid ID (shows error)
- [ ] T057 [US4] Test deleting last remaining task (empty list handled)
- [ ] T058 [US4] Test that other tasks remain after deletion

**Checkpoint**: ✅ All CRUD operations complete

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Error handling, user experience improvements, and final validation

- [ ] T059 [P] Add try-except for invalid menu input in main() (non-numeric, out of range)
- [ ] T060 [P] Add try-except for invalid ID input in get_valid_id() (non-numeric, negative)
- [ ] T061 [P] Add empty title validation in handle_add_task()
- [ ] T062 [P] Add empty title validation in handle_update_task()
- [ ] T063 [P] Verify all success messages are clear and helpful
- [ ] T064 [P] Verify all error messages are clear and helpful
- [ ] T065 Create tests/manual-test-checklist.md with all user story scenarios
- [ ] T066 Execute manual test checklist and verify all scenarios pass
- [ ] T067 Test edge case: Add 10+ tasks and verify performance < 1 second
- [ ] T068 Test edge case: Invalid menu choice (99, abc) shows error
- [ ] T069 Test edge case: Very long title (500+ chars) is handled
- [ ] T070 Update specs/001-todo-cli-app/quickstart.md with usage examples
- [ ] T071 Final integration test: Complete workflow (add, view, update, complete, delete)

**Checkpoint**: ✅ Application complete and tested

---

## Implementation Strategy

### MVP Scope (Recommended First Delivery)
- **Phase 1**: Setup ✅
- **Phase 2**: Foundational ✅
- **Phase 3**: User Story 1 (Add and View) 🎯

**Why**: Delivers a working app that can create and display tasks. Users can see immediate value.

### Incremental Delivery
1. **MVP**: US1 (Add + View) - Get feedback
2. **V1.1**: + US2 (Mark Complete) - Track progress
3. **V1.2**: + US3 (Update) - Fix mistakes
4. **V1.3**: + US4 (Delete) - Cleanup
5. **V1.4**: + Polish - Production ready

### Parallel Execution Opportunities

**Phase 2 (Foundational)**: All tasks marked [P] can run in parallel
- T005-T011 can be implemented simultaneously (different files)

**Phase 3 (US1)**: Some parallelism available
- T014-T018 (utils.py functions) can run parallel to T012-T013 (task_manager.py)
- After T012-T023 complete, T025-T028 (testing) can run in parallel

**Phase 4 (US2)**: Limited parallelism
- T030-T032 can run in parallel (different functions)

**Phase 5 (US3)**: Minimal parallelism (sequential implementation)

**Phase 6 (US4)**: Minimal parallelism (sequential implementation)

**Phase 7 (Polish)**: High parallelism
- T059-T064 can all run in parallel (different concerns)

---

## Dependencies

### User Story Completion Order

```
Phase 1 (Setup)
    ↓
Phase 2 (Foundational)
    ↓
Phase 3: US1 (P1) - Add and View Tasks 🎯 MVP
    ↓
Phase 4: US2 (P2) - Mark Complete (depends on US1 for get_task_by_id pattern)
    ↓
Phase 5: US3 (P3) - Update Tasks (depends on US2 for ID validation pattern)
    ↓
Phase 6: US4 (P4) - Delete Tasks (depends on US2 for ID validation pattern)
    ↓
Phase 7: Polish & Integration
```

### File Dependencies

```
task.py (no dependencies)
    ↓
task_manager.py (imports task)
    ↓
utils.py (no dependencies)
    ↓
main.py (imports task_manager, utils)
```

### Critical Path

**Longest sequential chain**:
1. T001-T004 (Setup) → 4 tasks
2. T005-T011 (Foundation) → 7 tasks (can parallelize)
3. T012-T013 (Task manager core) → 2 tasks
4. T019-T024 (Main loop) → 6 tasks
5. T025-T028 (US1 testing) → 4 tasks

**Total critical path**: ~23 tasks (assumes parallelization of utils.py work)

---

## Task Summary

| Phase | Tasks | Parallelizable | User Story |
|-------|-------|----------------|------------|
| Phase 1: Setup | 4 | 0 | - |
| Phase 2: Foundational | 7 | 7 | - |
| Phase 3: US1 (Add/View) | 17 | 6 | P1 (MVP) |
| Phase 4: US2 (Complete) | 13 | 3 | P2 |
| Phase 5: US3 (Update) | 9 | 0 | P3 |
| Phase 6: US4 (Delete) | 8 | 0 | P4 |
| Phase 7: Polish | 13 | 6 | - |
| **TOTAL** | **71** | **22** | **4 stories** |

**Parallel Opportunities**: 22 tasks (31%) can run in parallel with proper coordination

**MVP Task Count**: 28 tasks (Setup + Foundation + US1)

**Estimated Sequential Time**: 71 tasks
**Estimated Parallel Time**: ~49 task units (with perfect parallelization)

---

## Validation Checklist

✅ All tasks follow checkbox format: `- [ ] [ID] [P?] [Story?] Description`
✅ All tasks include file paths in descriptions
✅ Tasks organized by user story (US1, US2, US3, US4)
✅ Each user story has independent test criteria
✅ MVP scope clearly identified (US1)
✅ Dependencies documented (user story order, file order)
✅ Parallel opportunities identified ([P] marker)
✅ No automated tests (manual testing only as per spec)
✅ All 4 user stories from spec.md covered
✅ All files from plan.md included (task.py, task_manager.py, utils.py, main.py)

---

**Generated**: 2026-01-04
**Status**: Ready for implementation
**Next Step**: `/sp.implement` to begin execution
