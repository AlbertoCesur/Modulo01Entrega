from src.main.utils.funciones import sumar
from src.main.utils.funciones import restar
from src.main.utils.funciones import capital_case
from src.main.utils.funciones import dividir
from src.main.utils.funciones import nombre
from src.main.utils.funciones import otro

def test_resta():
    assert restar(2, 2) == 0

def test_suma():
    assert sumar(1, 2) == 3

def test_dividir():
    assert dividir(2, 2) == 1

def test_capital_case():
    assert capital_case('madrid') == 'Madrid'

def test_nombre():
    assert nombre('Ramon') == 'Ramon'

def test_otro():
    assert otro(2) is not 1

