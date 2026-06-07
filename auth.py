import bcrypt

from backend.database import (
    get_connection
)


class AuthManager:

    def register_user(
        self,
        username,
        password,
        role
    ):

        conn = get_connection()

        cursor = conn.cursor()

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        try:

            cursor.execute(
                """
                INSERT INTO users
                (
                    username,
                    password,
                    role
                )
                VALUES
                (
                    ?,
                    ?,
                    ?
                )
                """,
                (
                    username,
                    hashed,
                    role
                )
            )

            conn.commit()

            return True

        except:

            return False

        finally:

            conn.close()

    def login_user(
        self,
        username,
        password
    ):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT password,
                   role
            FROM users
            WHERE username=?
            """,
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if not user:

            return None

        stored_password = user[0]
        role = user[1]

        if bcrypt.checkpw(
            password.encode(),
            stored_password
        ):

            return role

        return None