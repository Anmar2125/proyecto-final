import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import Microgrid


def test_initial_state():
    """El sistema debe iniciar con valores esperados"""
    grid = Microgrid()
    assert grid.battery_soc == 75.0
    assert grid.solar_power == 0.0
    assert grid.load_power == 2.5
    assert grid.controlador_status == "RUNNING"


def test_solar_generation_daytime():
    """Entre 6 y 18 debe haber generación solar"""
    grid = Microgrid()
    grid.simulate_hour(12)  # Mediodía
    assert grid.solar_power > 0


def test_solar_generation_night():
    """Fuera de 6-18 no hay generación solar"""
    grid = Microgrid()
    grid.simulate_hour(2)
    assert grid.solar_power == 0.0


def test_controlador_charging():
    """Si hay exceso de energía, la batería debe cargarse"""
    grid = Microgrid()
    grid.solar_power = 5.0
    grid.load_power = 2.0
    soc_before = grid.battery_soc
    grid.simulate_hour(12)  # Fuerza simulación en el día
    assert grid.battery_soc >= soc_before
