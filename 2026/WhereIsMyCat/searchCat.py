import socket, warnings

try:
    socket.setdefaulttimeout(1)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(('1.1.1.1',53))
except socket.error as ex:  raise Exception("No hay connecion a Internet, verificat el cable o cambiate a un mejor servicio")