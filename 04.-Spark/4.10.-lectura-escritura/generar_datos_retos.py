import os
import pandas as pd

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    datos_dir = os.path.join(base_dir, "datos_retos")
    os.makedirs(datos_dir, exist_ok=True)

    print("Generando datos de empleados para los retos...")
    
    # Datos base
    data = [
        {"nombre": "Ana", "edad": 32, "departamento": "Ingeniería", "salario": 75000.0},
        {"nombre": "Luis", "edad": 28, "departamento": "Marketing", "salario": 55000.0},
        {"nombre": "Carla", "edad": 35, "departamento": "Ingeniería", "salario": 90000.0},
        {"nombre": "Pedro", "edad": 41, "departamento": "Ventas", "salario": 60000.0},
    ]
    df = pd.DataFrame(data)

    # 1. Parquet para Reto 3 (Lectura y Escritura Simple)
    path_reto3 = os.path.join(datos_dir, "reto3_empleados.parquet")
    df.to_parquet(path_reto3, index=False)
    print(f"Creado: {path_reto3}")

    # 2. Parquet para Reto 5 (Particionado por departamento)
    path_reto5 = os.path.join(datos_dir, "reto5_particionado")
    df.to_parquet(
        path_reto5,
        partition_cols=["departamento"],
        index=False
    )
    print(f"Creado particionado en: {path_reto5}")

    print("¡Todos los archivos .parquet para los retos de challenge.md han sido generados exitosamente!")

if __name__ == "__main__":
    main()
