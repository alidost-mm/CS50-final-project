from project import add_task, remove_task, show_tasks, tasks



def test_add_task():
    tasks.clear()  # لیست تسک‌ها را خالی می‌کنیم
    add_task("Task 1")
    assert len(tasks) == 1
    assert tasks[0] == "Task 1"

def test_remove_task_existing():
    tasks.clear()
    add_task("Task 1")
    remove_task("Task 1")
    assert len(tasks) == 0

def test_remove_task_non_existing():
    tasks.clear()
    add_task("Task 1")
    remove_task("Task 2")  # تسکی که وجود ندارد
    assert len(tasks) == 1  # تعداد تسک‌ها نباید تغییر کند


def test_show_tasks_with_tasks(capsys):
    tasks.clear()
    add_task("Task 1")
    add_task("Task 2")
    show_tasks()
    captured = capsys.readouterr()
    assert "To-Do List:" in captured.out
    assert "1. Task 1" in captured.out
    assert "2. Task 2" in captured.out

from io import StringIO
import sys

def test_show_tasks_empty(capsys):
    tasks.clear()
    show_tasks()
    captured = capsys.readouterr()
    assert captured.out == "Your To-Do List is empty.\n"

def test_show_tasks_non_empty(capsys):
    tasks.clear()
    add_task("Task 1")
    add_task("Task 2")
    show_tasks()
    captured = capsys.readouterr()
    assert captured.out == "To-Do List:\n1. Task 1\n2. Task 2\n"

def test_remove_task_existing(capsys):
    tasks.clear()
    add_task("Task 1")
    remove_task("Task 1")
    assert len(tasks) == 0

def test_remove_task_non_existing(capsys):
    tasks.clear()
    add_task("Task 1")
    remove_task("Task 2")  # تسکی که وجود ندارد
    assert len(tasks) == 1  # باید همچنان تسک اول موجود باشد
    captured = capsys.readouterr()
    assert captured.out == "Task not found in the list.\n"
