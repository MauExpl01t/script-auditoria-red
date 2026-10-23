# script-auditoria-red

Script en Python para auditoría y diagnóstico de redes. Genera informes automáticos de velocidad, estado de conexión local y pruebas de estabilidad.

## Qué hace

1. **Mide la velocidad** de descarga, subida y ping con la librería `speedtest`. Si la red o el firewall bloquean la prueba, lo avisa y abre Fast.com y nPerf para anotar los valores a mano.
2. **Registra la configuración de red local** con `ipconfig /all`.
3. **Prueba la estabilidad** de la conexión con `ping -n 4 8.8.8.8`.
4. **Guarda todo en un informe de texto** (`.txt`) con la fecha y la hora en el nombre del archivo.

## Requisitos

- Windows (usa los comandos `ipconfig` y `ping -n`).
- Python 3 y la librería `speedtest-cli`:

```bash
pip install speedtest-cli
```

## Uso

```bash
python "testeo red sermantec.py"
```

En la carpeta `dist/` hay una versión compilada (`.exe`) hecha con PyInstaller, que se ejecuta sin instalar Python.

## Archivos

- `testeo red sermantec.py`: script principal.
- `testeo red sermantec.spec`, `build/` y `dist/`: compilación con PyInstaller.
- `use Asignaturas_Inscritas.js`: práctica de MongoDB (base de datos no relacional). No forma parte del script de red.

## Autor

MauExpl01t, estudiante de Ingeniería en Ciberseguridad (INACAP). Proyecto de aprendizaje.
