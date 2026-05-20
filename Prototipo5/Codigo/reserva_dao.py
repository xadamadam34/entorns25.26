from db_config import get_connection

class ReservaDAO:

    def crear_reserva(self, id_usuari, id_schedule):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            # Comprovar si ja existeix reserva per aquest schedule
            cursor.execute(
                "SELECT id_reserva FROM RESERVA WHERE id_schedule = %s",
                (id_schedule,)
            )
            if cursor.fetchone():
                return False
            # Obtenir data, hora_inici i hora_fi del schedule
            cursor.execute(
                "SELECT data, hora_inici, hora_fi FROM SCHEDULE WHERE id_schedule = %s",
                (id_schedule,)
            )
            schedule = cursor.fetchone()
            if not schedule:
                return False
            cursor.execute(
                "INSERT INTO RESERVA (data, hora_inici, hora_fi, id_usuari, id_schedule) VALUES (%s, %s, %s, %s, %s)",
                (schedule['data'], schedule['hora_inici'], schedule['hora_fi'], id_usuari, id_schedule)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error crear_reserva: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def obtenir_per_usuari(self, id_usuari):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT r.id_reserva, r.data, r.hora_inici, r.hora_fi,
                       p.nom AS pista, p.tipus,
                       c.nom AS centre, c.ciutat
                FROM RESERVA r
                JOIN SCHEDULE s ON r.id_schedule = s.id_schedule
                JOIN PISTA p    ON s.id_pista = p.id_pista
                JOIN CENTRE c   ON p.id_centre = c.id_centre
                WHERE r.id_usuari = %s
                ORDER BY r.data, r.hora_inici
            """, (id_usuari,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error obtenir_per_usuari: {e}")
            return []
        finally:
            cursor.close()
            conn.close()

    def eliminar_reserva(self, id_reserva):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM RESERVA WHERE id_reserva = %s", (id_reserva,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error eliminar_reserva: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
