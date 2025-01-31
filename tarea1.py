from datetime import datetime
import pytz

# Zona horaria de EE.UU/New York
ny_timezone = pytz.timezone('America/New_York')

# Obtener la fecha y hora actual en la zona horaria especificada
ny_time = datetime.now(ny_timezone)

# Mostrar la fecha y hora formateada
print("Fecha y hora actual en Nueva York:", ny_time.strftime('%Y-%m-%d %H:%M:%S'))

