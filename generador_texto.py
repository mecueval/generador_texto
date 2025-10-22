import random
from collections import defaultdict

# ---------- FUNCIONES N-GRAMAS DE CARACTERES ----------
def generar_ngrams(texto, n):
    ngrams = defaultdict(int)
    for i in range(len(texto) - n + 1):
        ngram = texto[i:i+n]
        ngrams[ngram] += 1
    return dict(ngrams)

def calcular_prob_condicional(ngrams):
    cond_prob = defaultdict(dict)
    for ngram, count in ngrams.items():
        clave = ngram[:-1]
        ultimo = ngram[-1]
        if clave not in cond_prob:
            cond_prob[clave] = {}
        cond_prob[clave][ultimo] = count
    for clave, siguientes in cond_prob.items():
        total = sum(siguientes.values())
        for k in siguientes:
            siguientes[k] /= total
    return cond_prob

def generar_texto(cond_prob, inicio, longitud):
    texto = inicio
    n = len(inicio)
    while len(texto) < longitud:
        clave = texto[-(n-1):] if n > 1 else texto[-1]
        if clave not in cond_prob:
            break
        siguientes = cond_prob[clave]
        siguiente_caracter = random.choices(
            list(siguientes.keys()), weights=list(siguientes.values())
        )[0]
        texto += siguiente_caracter
    return texto

# ---------- FUNCIONES N-GRAMAS DE PALABRAS ----------
def generar_ngrams_palabras(palabras, n):
    ngrams = defaultdict(int)
    for i in range(len(palabras) - n + 1):
        ngram = tuple(palabras[i:i+n])
        ngrams[ngram] += 1
    return dict(ngrams)

def calcular_prob_condicional_palabras(ngrams):
    cond_prob = defaultdict(dict)
    for ngram, count in ngrams.items():
        clave = ngram[:-1]
        ultima = ngram[-1]
        if clave not in cond_prob:
            cond_prob[clave] = {}
        cond_prob[clave][ultima] = count
    for clave, siguientes in cond_prob.items():
        total = sum(siguientes.values())
        for k in siguientes:
            siguientes[k] /= total
    return cond_prob

def generar_texto_palabras(cond_prob, inicio, num_palabras):
    palabras = inicio.split('_')
    n = len(palabras)
    resultado = palabras.copy()
    while len(resultado) < num_palabras:
        clave = tuple(resultado[-(n-1):]) if n > 1 else tuple(resultado[-1:])
        if clave not in cond_prob:
            break
        siguientes = cond_prob[clave]
        siguiente_palabra = random.choices(
            list(siguientes.keys()), weights=list(siguientes.values())
        )[0]
        resultado.append(siguiente_palabra)
    return '_'.join(resultado)

# ---------- FUNCION PARA GUARDAR DISTRIBUCIONES ----------
def guardar_distribucion_txt(diccionario, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        for clave, valor in diccionario.items():
            f.write(f"{clave} : {valor}\n")

# ---------- BLOQUE PRINCIPAL ----------
if __name__ == "__main__":
    # --- CAMBIA AQUÍ EL NOMBRE DE TU ARCHIVO DE TEXTO LIMPIO ---
    ruta_archivo = "new_book.txt"

    # Leer archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto_limpio = f.read().strip()

    # ----------------- CARACTERES -----------------
    ngrams_2 = generar_ngrams(texto_limpio, 2)
    ngrams_3 = generar_ngrams(texto_limpio, 3)
    ngrams_4 = generar_ngrams(texto_limpio, 4)

    prob_cond_2 = calcular_prob_condicional(ngrams_2)
    prob_cond_3 = calcular_prob_condicional(ngrams_3)
    prob_cond_4 = calcular_prob_condicional(ngrams_4)

    # Guardar distribuciones de caracteres
    guardar_distribucion_txt(ngrams_2, "conjunta_caracteres_2.txt")
    guardar_distribucion_txt(prob_cond_2, "condicional_caracteres_2.txt")

    guardar_distribucion_txt(ngrams_3, "conjunta_caracteres_3.txt")
    guardar_distribucion_txt(prob_cond_3, "condicional_caracteres_3.txt")

    guardar_distribucion_txt(ngrams_4, "conjunta_caracteres_4.txt")
    guardar_distribucion_txt(prob_cond_4, "condicional_caracteres_4.txt")

    # ----------------- PALABRAS -----------------
    palabras = texto_limpio.split('_')
    ngrams_2_palabras = generar_ngrams_palabras(palabras, 2)
    prob_cond_palabras = calcular_prob_condicional_palabras(ngrams_2_palabras)

    # Guardar distribuciones de palabras
    guardar_distribucion_txt(ngrams_2_palabras, "conjunta_palabras_2.txt")
    guardar_distribucion_txt(prob_cond_palabras, "condicional_palabras_2.txt")

    # ----------------- GENERACION DE TEXTO -----------------
    # Texto de caracteres
    texto_car_2 = generar_texto(prob_cond_2, inicio="el", longitud=250)
    texto_car_3 = generar_texto(prob_cond_3, inicio="el_", longitud=250)
    texto_car_4 = generar_texto(prob_cond_4, inicio="el_p", longitud=250)

    with open("texto_generado_caracteres_2.txt", "w", encoding="utf-8") as f:
        f.write(texto_car_2)
    with open("texto_generado_caracteres_3.txt", "w", encoding="utf-8") as f:
        f.write(texto_car_3)
    with open("texto_generado_caracteres_4.txt", "w", encoding="utf-8") as f:
        f.write(texto_car_4)

    # Texto de palabras
    texto_palabras_1 = generar_texto_palabras(prob_cond_palabras, inicio="el_principito", num_palabras=250)
    texto_palabras_2 = generar_texto_palabras(prob_cond_palabras, inicio="el_rey_hablo_con", num_palabras=250)

    with open("texto_generado_palabras_principito.txt", "w", encoding="utf-8") as f:
        f.write(texto_palabras_1)
    with open("texto_generado_palabras_rey.txt", "w", encoding="utf-8") as f:
        f.write(texto_palabras_2)

    print("¡Distribuciones y textos generados y guardados en archivos .txt!")
