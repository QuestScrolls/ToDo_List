from typing import List

def display_tasks(todo_list: List[str]) -> None:
    """Print all tasks with their numbers."""
    if not todo_list:
        print("\n📭 Your To-Do list is empty.\n")
    else:
        print("\n📋 Your To-Do list:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"  {idx}. {task}")
        print()

def add_task(todo_list: List[str]) -> None:
    """Prompt for a new task and append it to the list."""
    task = input("Enter the new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"✅ Added: '{task}'\n")
    else:
        print("❌ No task entered. Nothing added.\n")

def remove_task(todo_list: List[str]) -> None:
    """Remove a task by number or by name."""
    if not todo_list:
        print("⚠️  No tasks to remove.\n")
        return

    print("Remove by:")
    print("  1. Task number")
    print("  2. Task name")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print(f"✅ Removed task #{num}: '{removed}'\n")
            else:
                print(f"❌ Invalid number. Please enter 1–{len(todo_list)}.\n")
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")

    elif choice == "2":
        name = input("Enter the exact task name to remove: ").strip()
        if name in todo_list:
            todo_list.remove(name)
            print(f"✅ Removed task: '{name}'\n")
        else:
            print(f"❌ Task '{name}' not found.\n")
    else:
        print("❌ Invalid choice.\n")

def clear_all_tasks(todo_list: List[str]) -> None:
    """Remove all tasks after confirmation."""
    if not todo_list:
        print("⚠️  List is already empty.\n")
        return
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").strip().lower()
    if confirm == 'y':
        todo_list.clear()
        print("🗑️  All tasks cleared.\n")
    else:
        print("Cancelled.\n")

def main():
    todo_list: List[str] = []
    print("📝 Welcome to the To-Do List App!\n")

    while True:
        display_tasks(todo_list)
        print("Options:")
        print("  1. Add Task")
        print("  2. Remove Task")
        print("  3. Clear All Tasks")
        print("  4. Quit")

        choice = input("Enter your choice (1–4): ").strip()

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            clear_all_tasks(todo_list)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()
