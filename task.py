import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    """Sub-task 1: Calcolare una Derivata."""
    # Definisco la variabile simbolica
    var = sympy.symbols(variabile)

    # Converto la stringa in un'espressione SymPy
    funzione = sympy.sympify(espressione)

    # Calcolo la derivata
    derivata = sympy.diff(funzione, var)

    return derivata

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    """Sub-task 2: Calcolare un Integrale Definito."""
    # Definisco la variabile simbolica
    var = sympy.symbols(variabile)

    # Converto la stringa in un'espressione SymPy
    funzione = sympy.sympify(espressione)

    # Calcolo l'integrale definito
    integrale = sympy.integrate(funzione, (var, estremo_inf, estremo_sup))

    return integrale

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""
    # Definisco la variabile simbolica
    var = sympy.symbols(variabile)

    # Converto la stringa in un'espressione SymPy
    funzione = sympy.sympify(espressione)

    # Converto il punto in un valore SymPy (può essere '0', 'oo', '-oo', ecc.)
    punto_val = sympy.sympify(punto)

    # Calcolo il limite
    limite = sympy.limit(funzione, var, punto_val)

    return limite

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    # Definisco la variabile simbolica
    var = sympy.symbols(variabile)

    # Converto la stringa in un'espressione SymPy
    funzione = sympy.sympify(espressione)

    # Calcolo la serie di Taylor fino all'ordine richiesto
    serie = sympy.series(funzione, var, punto, ordine + 1)

    # Rimuovo il termine O(...) per ottenere solo il polinomio
    polinomio = serie.removeO()

    return polinomio

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    # Definisco le variabili simboliche
    v1 = sympy.symbols(var1)
    v2 = sympy.symbols(var2)

    # Converto le stringhe in espressioni SymPy
    e1 = sympy.sympify(eq1)
    e2 = sympy.sympify(eq2)

    # Risolvo il sistema
    soluzioni = sympy.solve((e1, e2), (v1, v2))

    # Restituisco un dizionario {variabile: valore}
    return soluzioni

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
