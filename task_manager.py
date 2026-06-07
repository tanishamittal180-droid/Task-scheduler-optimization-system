from backend.database import get_connection


class TaskManager:

    def add_task(
        self,
        task_id,
        task_name,
        duration,
        deadline,
        priority,
        profit,
        dependency,
        skill_required
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO tasks(
                task_id,
                task_name,
                duration,
                deadline,
                priority,
                profit,
                dependency,
                skill_required,
                assigned_resource,
                start_time,
                finish_time,
                status
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                task_id,
                task_name,
                duration,
                deadline,
                priority,
                profit,
                dependency,
                skill_required,
                "",
                0,
                0,
                "Pending"
            )
        )

        conn.commit()
        conn.close()

    def get_tasks(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM tasks
            """
        )

        tasks = cursor.fetchall()

        conn.close()

        return tasks

    def delete_task(
        self,
        task_db_id
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_db_id,)
        )

        conn.commit()
        conn.close()

    def update_status(
        self,
        task_db_id,
        status
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE tasks
            SET status = ?
            WHERE id = ?
            """,
            (
                status,
                task_db_id
            )
        )

        conn.commit()
        conn.close()