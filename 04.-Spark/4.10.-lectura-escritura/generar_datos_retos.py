import os
import random
import pandas as pd

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    datos_dir = os.path.join(base_dir, "datos_retos")
    os.makedirs(datos_dir, exist_ok=True)

    print("Generando dataset a gran escala para los retos (100,000 filas)...")
    
    # Listas de semillas para generar nombres aleatorios
    nombres_semilla = ["Ana", "Luis", "Carla", "Pedro", "Sofía", "Jorge", "María", "Carlos", "Lucía", "Andrés", "Gabriela", "Felipe", "Elena", "Santiago", "Valeria", "Mateo"]
    apellidos_semilla = ["Gómez", "Rodríguez", "López", "Martínez", "Pérez", "González", "Sánchez", "Ramírez", "Díaz", "Hernández", "Torres", "Flores", "Morales", "Castillo"]
    departamentos = ["Ingeniería", "Marketing", "Ventas", "Finanzas", "Recursos Humanos", "Soporte"]

    # Generamos 100,000 registros aleatorios
    random.seed(42)  # Semilla fija para consistencia
    registros = []
    
    for _ in range(100000):
        nombre = f"{random.choice(nombres_semilla)} {random.choice(apellidos_semilla)}"
        edad = random.randint(18, 65)
        departamento = random.choice(departamentos)
        salario = round(random.uniform(25000.0, 150000.0), 2)
        registros.append({
            "nombre": nombre,
            "edad": edad,
            "departamento": departamento,
            "salario": salario
        })
        
    df = pd.DataFrame(registros)

    # 1. Parquet para Reto 3 (Lectura y Escritura Simple)
    path_reto3 = os.path.join(datos_dir, "reto3_empleados.parquet")
    df.to_parquet(path_reto3, index=False)
    print(f"Creado (100K filas): {path_reto3}")

    # 2. Parquet para Reto 5 (Particionado por departamento)
    path_reto5 = os.path.join(datos_dir, "reto5_particionado")
    df.to_parquet(
        path_reto5,
        partition_cols=["departamento"],
        index=False
    )
    print(f"Creado particionado (100K filas) en: {path_reto5}")

    print("¡Todos los archivos .parquet grandes para los retos han sido generados exitosamente!")

if __name__ == "__main__":
    main()
