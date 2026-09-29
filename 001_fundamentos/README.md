# Fundamentos de Procesamiento Digital de Imágenes

**Laboratorio de Tecnologías de la Imagen Digital — IFTS N.º 24**  
Prof. Matías Barreto · Ciclo lectivo 2026

---

## Qué vas a hacer acá

Entender que una imagen digital es una estructura de datos matricial que podemos cargar, inspeccionar, medir y transformar con scikit-image y NumPy. Analizamos imágenes en escala de grises y color RGB, estudiamos sus histogramas y aprendemos a binarizar mediante umbralado.

---

## El camino

| | Cuaderno | Qué cubre |
|---|---|---|
| 01 | `01_intro_pdi_scikit_image_y_numpy.ipynb` | Introducción a PDI: arreglos de NumPy, dimensiones, canales, transformaciones básicas |
| 02 | `02_histogramas.ipynb` | Distribución de intensidades, lectura e interpretación de histogramas en grises y color |
| 03 | `03_umbrales.ipynb` | Segmentación inicial: binarización, umbralado manual y método de Otsu |

---

## Entorno e instalación

Desde esta carpeta:

```bash
uv venv --python 3.12
```

Activá el entorno:
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **macOS / Linux:** `source .venv/bin/activate`

Instalá las librerías:
```bash
uv pip install -r requirements.txt
```

Abrí la carpeta en **Visual Studio Code**, abrí cualquiera de los cuadernos y seleccioná el kernel `.venv/`.
