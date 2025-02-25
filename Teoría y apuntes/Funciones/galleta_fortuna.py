import random

opciones = [
    "El éxito llega a quienes nunca dejan de intentarlo.",
    "Una pequeña acción hoy puede cambiar tu destino mañana.",
    "Sonríe, la fortuna favorece a los que ven la vida con alegría.",
    "No temas a los cambios, ellos traen nuevas oportunidades.",
    "Tu intuición te guiará hacia el camino correcto, confía en ella.",
    "Las mejores historias comienzan con un simple ¿y si…?",
    "La paciencia y la perseverancia abren más puertas que la fuerza.",
    "Lo que das al mundo, el mundo te lo devolverá multiplicado.",
    "Cada día es una nueva página en el libro de tu vida, escríbela bien.",
    "La felicidad no es un destino, sino la forma en que viajas."
]

def fortuna():
    fortuna_aleatoria = random.randint(0, len(opciones) - 1)
    print(opciones[fortuna_aleatoria])

fortuna()
