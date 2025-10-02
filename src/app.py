# src/app.py
class Microgrid:

    def __init__(self):
        self.battery_soc = 75.0  # Nivel de batería (%)
        self.solar_power = 0.0   # Generación solar (kW)
        self.load_power = 2.5    # Demanda de carga (kW)
        self.plc_status = "RUNNING"

    def simulate_hour(self, hour):
        """Simular la operación en una hora del día"""
        print(f"\n=== Hora {hour}:00 ===")
        
        # Generación solar simple  (6am a 6pm, max 5kW)
        self.solar_power = 5.0 if 10 <= hour <= 14 else (2.5 if 6 <= hour <= 18 else 0.0)
        
        # Demanda simple (más alta en la noche)
        self.load_power = 4.0 if 18 <= hour <= 22 else 2.0

        # Balance solar - demanda
        balance = self.solar_power - self.load_power

        # Reglas simples del controlador
        if balance > 0:
            self.battery_soc = min(100, self.battery_soc + 5)  # Carga
            action = "CARGANDO"
        elif balance < 0:
            if self.battery_soc > 20:
                self.battery_soc = max(0, self.battery_soc - 5)  # Descarga
                action = "DESCARGANDO"
            else:
                action = "SIN ENERGÍA"
        else:
            action = "BALANCEADO"

        # Verificar alarmas BMS
        if self.battery_soc < 20:
            self.plc_status = "ALERTA - SOC BAJO"
        elif self.battery_soc > 95:
            self.plc_status = "ALERTA - SOC ALTO"
        else:
            self.plc_status = "RUNNING"

        # Mostrar estado
        print(f"  Solar: {self.solar_power} kW |  Carga: {self.load_power} kW")
        print(f" SOC: {self.battery_soc:.1f}% | Acción: {action}")
        print(f" Estado PLC: {self.plc_status}")

def main():
    print("=== SIMULACIÓN MICRORED  ===")
    grid = Microgrid()
    
    for hour in range(24):
        grid.simulate_hour(hour)
    print("=== SIMULACIÓN COMPLETADA ===")

if __name__ == "__main__":
    main()
