import os
import socket

def get_container_id() -> str:
    """
    Devuelve un identificador del contenedor/host.
    En Docker, suele coincidir con el hostname (short id).
    """
    # Prioriza variable de entorno si existe
    env_id = os.getenv("CONTAINER_ID")
    if env_id:
        return env_id
    # Si no, usa el hostname (Docker lo setea con el container id corto)
    return socket.gethostname()
