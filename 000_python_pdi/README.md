# Python para mirar imágenes como datos

**Laboratorio de Tecnologías de la Imagen Digital — IFTS N.º 24**  
Prof. Matías Barreto · Ciclo lectivo 2026

---

## Qué vas a hacer acá

Aprender y afianzar Python mientras investigamos una imagen real. Una imagen digital puede ser, al mismo tiempo, un archivo en disco, un objeto de Pillow y una matriz de números en NumPy. En este encuentro inicial recorremos esas tres perspectivas y construimos una pequeña aplicación interactiva local con Gradio.

---

## Contenido

| Cuaderno | Tiempo | Tema |
|---|---|---|
| `01_python_para_imagenes.ipynb` | 90 min | De archivo a matriz: pathlib, Pillow, NumPy, funciones, decoradores y Gradio |

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

Abrí la carpeta en **Visual Studio Code**, abrí el cuaderno y seleccioná el kernel `.venv/`.
