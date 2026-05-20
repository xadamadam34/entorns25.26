from db_config import get_connection

class PistaDAO:

    def obtenir_totes(self):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT p.*, c.nom AS centre, c.ubicacio, c.ciutat
                FROM PISTA p
                JOIN CENTRE c ON p.id_centre = c.id_centre
                WHERE p.disponible = TRUE
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error obtenir_totes: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def obtenir_per_id(self, id_pista):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT p.*, c.nom AS centre, c.ubicacio, c.ciutat
                FROM PISTA p
                JOIN CENTRE c ON p.id_centre = c.id_centre
                WHERE p.id_pista = %s
            """, (id_pista,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error obtenir_per_id: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
