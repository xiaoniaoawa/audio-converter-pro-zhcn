
# Conversor de Audio (.m4a a .mp3)

Este proyecto tiene como objetivo convertir archivos de audio en formato `.m4a` a `.mp3` utilizando **Python** y la biblioteca **pydub** (que depende de ffmpeg).

---

## Índice
- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [Configurar Entorno Virtual](#configurar-entorno-virtual)
- [Uso](#uso)
  - [Ejemplo de Conversión de Un Archivo](#ejemplo-de-conversión-de-un-archivo)
  - [Ejemplo de Conversión de Varios Archivos en un Directorio](#ejemplo-de-conversión-de-varios-archivos-en-un-directorio)
- [Registros y Barra de Progreso](#registros-y-barra-de-progreso)
- [Otras Observaciones](#otras-observaciones)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Requisitos

- Python 3.8 o superior
- ffmpeg instalado en el sistema:

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Windows
- Descargue desde el [sitio oficial de ffmpeg](https://ffmpeg.org/) o utilice el gestor **Chocolatey**.
- Asegúrese de que el ejecutable `ffmpeg` esté en su PATH.

### macOS
```bash
brew install ffmpeg
```

---

## Instalación

Clone el repositorio (o descargue el archivo ZIP):
```bash
git clone https://github.com/usuario/audio-converter-pro-pro.git
```

Navegue a la carpeta del proyecto:
```bash
cd audio-converter-pro-pro
```

### Dependencias de Python

Instale las dependencias del archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

Las dependencias principales son:
- **pydub** – biblioteca Python para facilitar operaciones de audio.
- Otras listadas en `requirements.txt`.

---

### Configurar Entorno Virtual

Se recomienda crear y activar un entorno virtual antes de instalar las dependencias (para evitar conflictos con otras bibliotecas instaladas globalmente).

```bash
python -m venv venv
```

Active el entorno virtual:

- **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```
- **Windows**:
    ```bash
    venv\Scripts\activate
    ```

Ahora, instale las dependencias dentro del entorno virtual:
```bash
pip install -r requirements.txt
```

---

## Uso

El script principal de este proyecto es `convert_m4a_to_mp3.py`, que puede ejecutarse directamente desde la línea de comandos.

Acepta los siguientes argumentos:
1. `<input_path>`: Ruta de un archivo `.m4a` o de un directorio que contenga varios archivos `.m4a`.
2. `[output_directory]` (opcional): Directorio donde se generarán los archivos `.mp3`.

### Ejemplo de Conversión de Un Archivo

En la misma ubicación:
```bash
python convert_m4a_to_mp3.py "C:\musicas\faixa1.m4a"
```

Para un directorio de destino específico:
```bash
python convert_m4a_to_mp3.py "C:\musicas\faixa1.m4a" "C:\saida_mp3"
```

### Ejemplo de Conversión de Varios Archivos en un Directorio

En la misma ubicación:
```bash
python convert_m4a_to_mp3.py "C:\musicas"
```

Para otro directorio:
```bash
python convert_m4a_to_mp3.py "C:\musicas" "C:\saida_mp3"
```

---

## Registros y Barra de Progreso

El script muestra:
- **Barra de progreso**: indica el índice del archivo actual, el total de archivos y el porcentaje completado.
- Nombre del archivo de entrada y del archivo de salida generado (o error, en caso de fallo).
- Tiempo de procesamiento de cada archivo (en segundos).
- **Resumen final**: total de conversiones exitosas, fallos y tiempo total de ejecución.

### Ejemplo de salida:
```
Iniciando la conversión de 3 archivo(s) .m4a en 'C:\musicas'...

[1/3] |█████--------------|  33.3%  faixa1.m4a -> faixa1.mp3 : OK | tiempo: 2.37s
[2/3] |██████████---------|  66.7%  faixa2.m4a -> faixa2.mp3 : OK | tiempo: 3.10s
[3/3] |██████████████████-| 100.0%  faixa3.m4a -> ERROR: ...

¡Conversión completada!
 - Éxitos  : 2
 - Fallos  : 1
 - Total   : 3
Tiempo total de ejecución: 12.45s.
```

---

## Otras Observaciones

- Si tiene problemas con las barras invertidas (`\`), utilice comillas para rutas que contengan espacios o caracteres especiales.
- Si desea extensiones diferentes u otro formato de salida, puede adaptar el código para usar:
    ```python
    AudioSegment.from_file(input_file, format="m4a").export(output_file, format="mp3")
    ```
    Con otras configuraciones (bitrate, canales, etc.).

---

## Contribuciones

¡Las contribuciones son bienvenidas! Siéntase libre de abrir **issues** o enviar **pull requests**.

1. Realice un fork del proyecto.
2. Cree una branch para su contribución:
    ```bash
    git checkout -b feature/su-contribucion
    ```
3. Haga commit de sus cambios:
    ```bash
    git commit -m "Añade nueva funcionalidad"
    ```
4. Realice push de la branch:
    ```bash
    git push origin feature/su-contribucion
    ```
5. Abra un **Pull Request** explicando el cambio propuesto.

---

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Siéntase libre de usarlo, modificarlo y distribuirlo.

**Autor**: Su Nombre/Equipo  
**Contacto**: su.email@dominio.com
