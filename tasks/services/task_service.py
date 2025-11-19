from django.db import connection


class TaskService:
    """
    Service layer for performing CRUD operations on the 'tasks' table.

    This class uses raw SQL queries through Django's database connection.
    Each method opens a cursor, executes the required SQL command,
    and returns the appropriate result.

    The table structure expected:
        id INTEGER PRIMARY KEY AUTOINCREMENT
        title TEXT NOT NULL
        description TEXT
        due_date TEXT NOT NULL
        status TEXT NOT NULL
    """

    @staticmethod
    def all():
        """
        Retrieve all tasks from the database.

        Returns:
            list[tuple]: A list of all rows from the 'tasks' table.
                         Each row is returned as a tuple in the order of columns.
        """
        with connection.cursor() as cur:
            cur.execute("SELECT * FROM tasks")
            return cur.fetchall()

    @staticmethod
    def get(task_id):
        """
        Retrieve a single task by its ID.

        Args:
            task_id (int): The primary key of the task.

        Returns:
            tuple | None: Returns a tuple containing the task record.
                           Returns None if no task exists with the given ID.
        """
        with connection.cursor() as cur:
            cur.execute("""
                SELECT * FROM tasks WHERE id=%s
            """, [task_id])
            return cur.fetchone()

    @staticmethod
    def create(title, description, due_date, status="pending"):
        """
        Create a new task and insert it into the database.

        Args:
            title (str): Title of the task.
            description (str): Detailed description.
            due_date (str): Due date (YYYY-MM-DD format recommended).
            status (str, optional): Task status. Defaults to 'pending'.

        Returns:
            None
        """
        with connection.cursor() as cur:
            cur.execute(
                """
                INSERT INTO tasks (title, description, due_date, status)
                VALUES (%s, %s, %s, %s)
                """,
                (title, description, due_date, status)
            )

    @staticmethod
    def update(task_id, title, description, due_date, status):
        """
        Update an existing task record.

        Args:
            task_id (int): ID of the task being updated.
            title (str): Updated title.
            description (str): Updated description.
            due_date (str): Updated due date.
            status (str): Updated status ('pending', 'done', etc.).

        Returns:
            None
        """
        with connection.cursor() as cur:
            cur.execute("""
                UPDATE tasks
                SET title=%s, description=%s, due_date=%s, status=%s
                WHERE id=%s
            """, (title, description, due_date, status, task_id))

    @staticmethod
    def delete(task_id):
        """
        Delete a task by ID.

        Args:
            task_id (int): ID of the task to delete.

        Returns:
            None
        """
        with connection.cursor() as cur:
            cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
