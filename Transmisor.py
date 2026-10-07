import socket
# Importamos tu función desde el otro archivo
from lector_serial import leer_joysticks

# IP de la Thinkpad receptora
IP_RECEPTOR = '100.94.73.36'
PUERTO_UDP = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Iniciando módulo transmisor UDP...")
print(f"Destino: {IP_RECEPTOR}:{PUERTO_UDP}\n")

try:
    # Este 'for' llama a tu código. Cada vez que tu código hace un 'yield',
    # recibimos los 4 valores aquí en tiempo real.
    for x1, y1, x2, y2 in leer_joysticks():
        # Empaquetamos para envío
        mensaje = f"{x1},{y1},{x2},{y2}"
        # Disparamos por Tailscale
        sock.sendto(mensaje.encode('utf-8'), (IP_RECEPTOR, PUERTO_UDP))
except KeyboardInterrupt:
    print("\nTransmisión detenida principal.")
finally:
    sock.close()