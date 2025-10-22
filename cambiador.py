import string
import unicodedata

# Leer el archivo original
with open("book.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Convertir a minúsculas
text = text.lower()

# Eliminar tildes
text = "".join(
    c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
)

# Eliminar signos de puntuación y comillas (mantener espacios)
punctuations = string.punctuation + "«»“”‘’—…¡¿"
translator = str.maketrans("", "", punctuations)
text = text.translate(translator)

text = text.replace(" ", "_")
text = text.replace("\n", "___")

# Guardar el archivo procesado
output_path = "new_book.txt"
with open(output_path, "w", encoding="utf-8") as file:
    file.write(text)

output_path
