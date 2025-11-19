from django.db import models


class Task(models.Model):
    """
    Django ORM model mapped to an existing SQL table named `tasks`.

    Since the table was created manually via SQL (not by Django migrations),
    we set:
        - managed = False → Django will NOT try to create, modify or delete the table.
        - db_table = "tasks" → Explicit mapping to your SQL table name.

    Fields:
        title       : Short text title of the task
        description : Detailed task description
        due_date    : Task deadline (DATE in SQL)
        status      : pending/done or any custom state

    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "tasks"
        managed = False
