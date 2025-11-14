# ========================================
# PROGRAMA PRINCIPAL
# ========================================
from vehiculo import Vehiculo
from motor import Motor
from auto import Automovil
from motocicleta import Motocicleta

if __name__ == "__main__":
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "SISTEMA DE GESTIÓN DE VEHÍCULOS" + " " * 27 + "║")
    print("╚" + "═" * 78 + "╝\n")

    # Crear motores
    print("  CREANDO MOTORES...")
    print("-" * 80)
    motor_auto1 = Motor("Gasolina", 6, 280)
    motor_auto2 = Motor("Gasolina", 4, 180)
    motor_moto1 = Motor("Gasolina", 2, 150)
    motor_moto2 = Motor("Eléctrico", 0, 120)
    print("✓ 4 motores creados exitosamente\n")

    # Crear automóviles
    print(" CREANDO AUTOMÓVILES...")
    print("-" * 80)
    auto1 = Automovil("Toyota", "Camry", 2023, 4, motor_auto1)
    auto2 = Automovil("Honda", "Civic", 2022, 4, motor_auto2)
    print("✓ 2 automóviles creados\n")

    # Crear motocicletas
    print("  CREANDO MOTOCICLETAS...")
    print("-" * 80)
    moto1 = Motocicleta("Yamaha", "YZF-R1", 2023, 998, motor_moto1)
    moto2 = Motocicleta("Zero", "SR/F", 2023, 0, motor_moto2)
    print("✓ 2 motocicletas creadas\n")

    # Demostración Auto 1
    print("\n" + "=" * 80)
    print("PRUEBA: AUTOMÓVIL 1 - Toyota Camry")
    print("=" * 80)
    print("\n Estado inicial:")
    print(auto1)
    print("\n Ejecutando métodos:")
    print("→", motor_auto1.encender_motor())
    print("→", auto1.encender())
    print("→", auto1.tocar_claxon())
    print("→", auto1.abrir_maletero())
    print("\n Estado actualizado:")
    print(auto1)

    # Demostración Auto 2
    print("\n" + "=" * 80)
    print("PRUEBA: AUTOMÓVIL 2 - Honda Civic")
    print("=" * 80)
    print("\n Estado inicial:")
    print(auto2)
    print("\n Ejecutando métodos:")
    print("→", motor_auto2.encender_motor())
    print("→", auto2.encender())
    print("→", auto2.tocar_claxon())
    print("→", auto2.abrir_maletero())
    print("\n Estado actualizado:")
    print(auto2)

    # Demostración Moto 1
    print("\n" + "=" * 80)
    print("PRUEBA: MOTOCICLETA 1 - Yamaha YZF-R1")
    print("=" * 80)
    print("\n Estado inicial:")
    print(moto1)
    print("\n Ejecutando métodos:")
    print("→", motor_moto1.encender_motor())
    print("→", moto1.usar_patada_arranque())
    print("→", moto1.hacer_caballito())
    print("\n Estado actualizado:")
    print(moto1)

    # Demostración Moto 2
    print("\n" + "=" * 80)
    print("PRUEBA: MOTOCICLETA 2 - Zero SR/F")
    print("=" * 80)
    print("\n Estado inicial:")
    print(moto2)
    print("\n Ejecutando métodos:")
    print("→", motor_moto2.encender_motor())
    print("→", moto2.usar_patada_arranque())
    print("→", moto2.hacer_caballito())
    print("\n Estado actualizado:")
    print(moto2)

    print("\n" + "=" * 80)
    print(" PROGRAMA EJECUTADO EXITOSAMENTE")
    print("=" * 80)