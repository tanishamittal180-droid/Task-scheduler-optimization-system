from backend.database import (
    get_connection
)


class ResourceManager:

    def add_resource(
        self,
        resource_id,
        resource_name,
        skill,
        capacity
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO resources(
                resource_id,
                resource_name,
                skill,
                capacity
            )
            VALUES(?,?,?,?)
            """,
            (
                resource_id,
                resource_name,
                skill,
                capacity
            )
        )

        conn.commit()

        conn.close()

    def get_resources(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM resources
            """
        )

        data = cursor.fetchall()

        conn.close()

        return data

    def delete_resource(
        self,
        row_id
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM resources
            WHERE id=?
            """,
            (row_id,)
        )

        conn.commit()

        conn.close()