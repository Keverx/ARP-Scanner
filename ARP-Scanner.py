import scapy.all as scapy
import argparse

def get_arguments():
    # Creamos el objeto "parser" (el que lee lo que escribes en la terminal)
    parser = argparse.ArgumentParser()
    
    # Definimos que esperamos recibir un argumento "-t" o "--target"
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP Range (Ej: 192.168.1.1/24)")


    # Leemos los argumentos
    options = parser.parse_args()
    
    # Si el usuario no puso nada, le avisamos y cerramos (Control de errores básico)
    if not options.target:
        parser.error("[-] Por favor indica un rango de IP con -t, o usa --help para más info.")
    return options

def escanear(ip_rango):
    print(f"Escaneando la red: {ip_rango} ...")
    arp_request = scapy.ARP(pdst=ip_rango) # La pregunta que hará
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # A quienes hará la pregunta, en este caso a todo mundo
    paquete_final = broadcast/arp_request
    ans = scapy.srp(paquete_final, timeout=1, verbose=False)[0]
    
    print("\nDispositivos Encontrados:")
    print("IP\t\t\tDirección MAC")
    print("-----------------------------------------")
    for enviado, recibido in ans:
        print(recibido.psrc + "\t\t" + recibido.hwsrc)
        
# --- ZONA DE EJECUCIÓN ---
if __name__ == "__main__":
    # 1. Obtenemos los argumentos de la terminal
    opciones = get_arguments()
    
    # 2. Usamos la IP que nos pasó el usuario en la variable "opciones.target"
    escanear(opciones.target)
    