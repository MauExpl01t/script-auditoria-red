import subprocess
import datetime
import webbrowser
import speedtest
import time

def generar_reporte_auditoria():
    fecha_hoy = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"Auditoria_Red_{fecha_hoy}.txt"
    
    print("--- 🚀 Iniciando Auditoria de Red y Velocidad ---")
    
    # Inicializamos variables por si el test falla
    down, up, ping_lat = 0, 0, 0
    
    try:
        # 1. Test de Velocidad Interno con Seguridad
        try:
            print("Midiendo Speedtest Interno (Espere un momento)...")
            # Usamos secure=True para evitar el Error 403 Forbidden
            st = speedtest.Speedtest(secure=True)
            st.get_best_server()
            down = st.download() / 1_000_000
            up = st.upload() / 1_000_000
            ping_lat = st.results.ping
            print("✅ Speedtest interno completado.")
        except Exception as e:
            print(f"⚠️ Aviso: Speedtest interno bloqueado ({e}).")
            print("🔗 Usaremos Fast y nPerf para los datos de velocidad.")

        # 2. Abrir herramientas para captura manual (Siempre funciona)
        print("Abriendo Fast.com y nPerf en el navegador...")
        webbrowser.open("https://fast.com/es/")
        time.sleep(2)
        webbrowser.open("https://www.nperf.com/es/")

        # 3. Datos de Red (IPCONFIG y PING)
        print("Obteniendo datos de red local...")
        ip_data = subprocess.check_output("ipconfig /all", shell=True, text=True)
        ping_data = subprocess.check_output("ping -n 4 8.8.8.8", shell=True, text=True)

        with open(filename, "w") as f:
            f.write("==============================================\n")
            f.write("        INFORME DE AUDITORIA DE RED          \n")
            f.write(f"      FECHA Y HORA: {fecha_hoy}              \n")
            f.write("==============================================\n\n")
            
            f.write("--- SECCIÓN 1: PRUEBAS DE VELOCIDAD ---\n")
            f.write(f"A) SPEEDTEST (Automático):\n")
            if down > 0:
                f.write(f"   - Descarga: {down:.2f} Mbps\n")
                f.write(f"   - Subida:   {up:.2f} Mbps\n")
                f.write(f"   - Ping:     {ping_lat:.2f} ms\n\n")
            else:
                f.write("   - (Bloqueado por Red/Firewall. Ver abajo)\n\n")
            
            f.write(f"B) FAST.COM (Anotar de la web):\n")
            f.write(f"   - Descarga: ________ Mbps\n\n")
            
            f.write(f"C) NPERF (Anotar de la web):\n")
            f.write(f"   - Descarga: ________ Mbps\n")
            f.write(f"   - Subida:   ________ Mbps\n")
            f.write(f"   - Latencia: ________ ms\n\n")
            
            f.write("--- SECCIÓN 2: CONFIGURACIÓN LOGICA (ACTA) ---\n")
            f.write(ip_data)
            f.write("\n" + "-"*45 + "\n")
            
            f.write("--- SECCIÓN 3: ESTABILIDAD (PING 8.8.8.8) ---\n")
            f.write(ping_data)
            f.write("\n==============================================\n")
            f.write("Informe generado para validación de terreno.\n")

        print(f"✅ Reporte guardado con éxito: {filename}")
        print("📸 Toma las capturas de la web y anota los valores en el .txt")
        input("Presiona Enter para finalizar...")

    except Exception as e:
        print(f"❌ Error crítico en el programa: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    generar_reporte_auditoria()