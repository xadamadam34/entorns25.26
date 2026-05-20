import hashlib
from db_config import get_connection

class UsuariDAO:

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def crear_usuari(self, nom, email, password):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            hashed = self._hash_password(password)
            cursor.execute(
                "INSERT INTO USUARI (nom, email, password) VALUES (%s, %s, %s)",
                (nom, email, hashed)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error crear_usuari: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def verificar_usuari(self, email, password):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            hashed = self._hash_password(password)
            cursor.execute(
                "SELECT id_usuari, nom, email FROM USUARI WHERE email=%s AND password=%s",
                (email, hashed)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Error verificar_usuari: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
