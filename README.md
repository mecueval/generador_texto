# 🧠 Generador de texto probabilístico

Este proyecto implementa un **generador de texto basado en probabilidades** de aparición de caracteres y palabras, usando un texto base previamente limpiado.  
Forma parte de una práctica del curso de **Inteligencia Artificial**.

---

## 📋 Descripción

El proyecto incluye dos etapas principales:

1. **Limpieza del texto (`cambiador.py`)**  
   - Elimina tildes, signos de puntuación y convierte todo a minúsculas.  
   - Reemplaza los espacios por guiones bajos `_` para tratarlos como caracteres.

2. **Generación y análisis (`generador_texto.py`)**  
   - Calcula las distribuciones de probabilidad:
     - **P(a, b)**: probabilidad conjunta de ver el carácter `a` seguido de `b`.  
     - **P(a | b)**: probabilidad condicional de ver `a` dado `b`.  
     - Extiende a 3 y 4 caracteres (modelos de n-gramas).  
     - **P(palabra1 | palabra2)**: probabilidad condicional entre palabras.  
   - Genera texto a partir de secuencias iniciales como `el`, `el_`, `el_p` o `el_rey_hablo_con`.

---

## ⚙️ Uso

1. Limpia el texto de entrada:
   ```bash
   python cambiador.py
Esto genera un archivo texto_limpio.txt.

2.Calcula las distribuciones y genera texto:
  ```bash
  python generador_texto.py Se generarán:


