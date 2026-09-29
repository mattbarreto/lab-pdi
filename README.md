# Laboratorio de Tecnologías de la Imagen Digital

**IFTS N.º 24 · Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial**  
Profesor: Matías Barreto (`matiasbarreto@ifts24.edu.ar`) · Ciclo lectivo 2026  
Coordinación de Trabajos Prácticos: Cynthia Marcela Villagra (`29433211@ifts24.edu.ar`)  
Repositorio: [`lab-pdi`](https://github.com/mattbarreto/lab-pdi)

---

## Empezá acá

### 1. Cómo descargar una carpeta individual
Cada unidad es modular y se puede trabajar por separado. Para descargar únicamente la carpeta de la clase o tema sin clonar todo el repositorio, podés usar cualquiera de estas herramientas web gratuitas (no requieren registro):

* **Opción 1 — Download Directory:**
  1. Copiá el enlace de la carpeta en GitHub (por ejemplo, `.../002_segmentacion` o `.../003_opencv`).
  2. Entrá en [download-directory.github.io](https://download-directory.github.io).
  3. Pegá la URL en el cuadro y presioná `Enter`. Se descargará automáticamente un archivo `.zip` con solo esa carpeta.
* **Opción 2 — DownGit:**
  1. Entrá en [downgit.github.io](https://downgit.github.io).
  2. Pegá el enlace de la carpeta en el campo *GitHub URL*.
  3. Hacé clic en **Download**.
* **Opción 3 — Git clone (para quienes ya usan Git):**
  ```bash
  git clone https://github.com/mattbarreto/lab-pdi.git
  ```
  Y luego `git pull` periódicamente para bajar las actualizaciones.

> [!TIP]
> **Nota sobre `003_opencv`:** Los cuadernos de `003_opencv` leen imágenes de prueba de la carpeta hermana `imagenes/`. Si vas a trabajar con esa unidad, te recomendamos descargar la carpeta `003_opencv` completa para mantener la carpeta de imágenes vinculada.

---

### 2. Regla de oro para trabajar en los cuadernos

> **No edites los cuadernos originales.**  
> Antes de resolver las consignas, duplicá el cuaderno y agregale `_mio` al nombre (por ejemplo: `01_python_para_imagenes_mio.ipynb`) dentro de la misma carpeta.  
> El repositorio ignora automáticamente todos los archivos `*_mio.ipynb`, lo que te permite actualizar el material con `git pull` o sobreescribir la carpeta sin perder tus notas ni generar conflictos.

---

## El recorrido de la materia

La pregunta de fondo que articula todo el laboratorio:

> **¿Cómo pasa una señal lumínica capturada por un sensor a ser una matriz computable, qué transformaciones matemáticas y espaciales la modifican, y de qué forma las redes neuronales, la visión por computadora y la IA Generativa (GenAI) nos permiten interpretar y sintetizar nuevas imágenes digitales?**

```
 ● armado      ○ en desarrollo

 TRAMO A · LA IMAGEN COMO DATO
     ● Python, Pillow, NumPy y visualización interactiva ..... 000_python_pdi
     ↓
     ● Fundamentos matriciales, histogramas y umbrales ...... 001_fundamentos

 TRAMO B · MANIPULACIÓN, CANALES Y SEGMENTACIÓN BÁSICA
     ↓
     ● Prácticas guiadas de color, geometría y corte ........ 002_segmentacion

 TRAMO C · VISIÓN POR COMPUTADORA CON OPENCV
     ↓
     ● Nivel 1 — Introducción, lectura, encuadre y fichas ... 003_opencv/001_intro
     ↓
     ○ Nivel 2 — Filtrado espacial, bordes y morfología ...... 003_opencv/002_fundamental
     ↓
     ○ Nivel 3 — Detección, descriptores, video y DNN ....... 003_opencv/003_avanzado

 TRAMO D · VISIÓN POR COMPUTADORA Y REDES NEURONALES (DEEP LEARNING)
     ↓
     ○ De filtros clásicos a convoluciones (CNNs)
     ↓
     ○ Clasificación, detección de objetos y segmentación (YOLO, transfer learning)
     ↓
     ○ Extracción de características y embeddings visuales

 TRAMO E · INTELIGENCIA ARTIFICIAL GENERATIVA (GenAI) Y MULTIMODALIDAD
     ↓
     ○ Modelos de difusión y síntesis visual (Stable Diffusion, inpainting generativo)
     ↓
     ○ Modelos de Visión y Lenguaje (VLMs: contrastivos y generativos multimodal)
     ↓
     ○ Sistemas de visión agente y pipelines interactivos

 TRAMO F · COMPLEMENTARIOS MATEMÁTICOS Y TRABAJOS APLICADOS
     ↓
     ● Transformaciones lineales 2D, autovalores y PCA ...... complementarios/numpy
     ↓
     ● TPI 1: Canvas analítica de imagen y rúbrica .......... trabajos/TPI1
```

---

## Las unidades del repositorio

| | Carpeta | Qué cubre | Entorno / Ejecución | Librerías clave |
|---|---|---|---|---|
| 0 | [`000_python_pdi/`](000_python_pdi/) | Python para imágenes, Pillow, matrices NumPy y app interactiva | Local en VS Code | `numpy`, `matplotlib`, `pillow`, `gradio` |
| 1 | [`001_fundamentos/`](001_fundamentos/) | Fundamentos matriciales, canales, histogramas y umbralado Otsu | Local en VS Code | `numpy`, `matplotlib`, `scikit-image` |
| 2 | [`002_segmentacion/`](002_segmentacion/) | 8 prácticas guiadas: color HSV, muestreo, cuantización y máscaras | Local en VS Code | `opencv-python`, `numpy`, `matplotlib`, `scikit-image` |
| 3 | [`003_opencv/`](003_opencv/) | OpenCV modular en 3 niveles (lectura, encuadre, análisis y script) | Local en VS Code | `opencv-python`, `numpy`, `matplotlib`, `scikit-image` |
| + | [`complementarios/numpy/`](complementarios/numpy/) | Álgebra lineal aplicada: rotación, escala, cizalle, autovalores y PCA | Local en VS Code | `numpy`, `matplotlib`, `scikit-learn` |
| + | [`trabajos/`](trabajos/) | Trabajos Prácticos Integradores (TPI 1: Canvas analítica de imagen) | Visualizador Web | HTML5 interactivo |
| + | [`bibliografia/`](bibliografia/) | Ensayos teóricos y lecturas críticas (Lev Manovich) | Lectura Markdown | Markdown |

---

## Cómo se trabaja

Todas las carpetas de las unidades siguen un estándar común:

| Archivo | Para qué sirve |
|---|---|
| `README.md` | Qué se hace en la unidad, en qué orden y las ideas pedagógicas centrales. |
| `requirements.txt` | Lista limpia de dependencias para recrear el entorno. |

### Cada unidad tiene su propio entorno virtual

No hay un entorno único gigante para toda la materia: cada carpeta se aísla con su propio `.venv`.

Para crearlo, parate en la terminal **dentro de la carpeta de la unidad**:

```bash
uv venv --python 3.12
```

Activá el entorno según tu sistema operativo:
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **macOS / Linux:** `source .venv/bin/activate`

Instalá las librerías:
```bash
uv pip install -r requirements.txt
```

Luego, abrís la carpeta en **Visual Studio Code**, abrís el cuaderno y elegís el kernel correspondiente a `.venv/`.

> **La carpeta `.venv` no se sube ni se comparte.**  
> Ocupa cientos de megabytes y contiene rutas absolutas de tu máquina. Lo que se comparte es `requirements.txt`.

---

## Procedencia de imágenes y autoría

Las prácticas utilizan imágenes de prueba de dominio público o bajo licencias permisivas (incluyendo imágenes clásicas de prueba en procesamiento digital de imágenes y fotografías de demostración urbana y de objetos), complementadas con capturas realizadas por los propios estudiantes en las actividades de campo.

---

## Equipo docente e invitados especiales

* **Profesor a cargo:** Matías Barreto ([matiasbarreto@ifts24.edu.ar](mailto:matiasbarreto@ifts24.edu.ar))
* **Coordinación de Trabajos Prácticos (edición 2026):** Cynthia Marcela Villagra ([29433211@ifts24.edu.ar](mailto:29433211@ifts24.edu.ar))

### Clases especiales e invitados
* **Clase de Animación Tradicional y 3D:** a cargo de **Agustín Di Tommasso**.

---

## Licencia

* **Contenidos educativos y cuadernos:** Distribuido bajo licencia [Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](LICENSE).
* **Código fuente y utilidades:** Distribuido bajo [Licencia MIT](LICENSE-CODIGO).
