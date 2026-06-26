import os
import pandas as pd

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    datos_dir = os.path.join(base_dir, "datos")
    os.makedirs(datos_dir, exist_ok=True)

    print("Generando datos de ventas particionados...")
    # 1. Ventas particionadas por pais y anio
    ventas_data = [
        {"id": 1, "producto": "Laptop", "precio": 1200.0, "pais": "España", "anio": 2023},
        {"id": 2, "producto": "Smartphone", "precio": 800.0, "pais": "España", "anio": 2023},
        {"id": 3, "producto": "Monitor", "precio": 300.0, "pais": "México", "anio": 2023},
        {"id": 4, "producto": "Teclado", "precio": 50.0, "pais": "México", "anio": 2024},
        {"id": 5, "producto": "Mouse", "precio": 25.0, "pais": "Colombia", "anio": 2024},
        {"id": 6, "producto": "Laptop", "precio": 1300.0, "pais": "Colombia", "anio": 2024},
        {"id": 7, "producto": "Smartphone", "precio": 850.0, "pais": "España", "anio": 2024},
        {"id": 8, "producto": "Monitor", "precio": 320.0, "pais": "México", "anio": 2024},
    ]
    df_ventas = pd.DataFrame(ventas_data)
    
    path_ventas = os.path.join(datos_dir, "ventas_particionadas")
    # Para guardar particionado con pandas/pyarrow:
    df_ventas.to_parquet(
        path_ventas,
        partition_cols=["pais", "anio"],
        index=False
    )

    print("Generando datos de usuarios para Schema Merging...")
    # 2. Schema Merging (usuarios_a y usuarios_b)
    # Parte A: id, nombre, email
    usr_a_data = [
        {"id": 1, "nombre": "Alice", "email": "alice@example.com"},
        {"id": 2, "nombre": "Bob", "email": "bob@example.com"},
    ]
    df_usr_a = pd.DataFrame(usr_a_data)
    
    path_usr_a = os.path.join(datos_dir, "usuarios_esquema", "parte_a")
    os.makedirs(path_usr_a, exist_ok=True)
    df_usr_a.to_parquet(os.path.join(path_usr_a, "data.parquet"), index=False)

    # Parte B: id, nombre, telefono (nueva columna, sin email)
    usr_b_data = [
        {"id": 3, "nombre": "Charlie", "telefono": "+5212345678"},
        {"id": 4, "nombre": "David", "telefono": "+346543210"},
    ]
    df_usr_b = pd.DataFrame(usr_b_data)
    
    path_usr_b = os.path.join(datos_dir, "usuarios_esquema", "parte_b")
    os.makedirs(path_usr_b, exist_ok=True)
    df_usr_b.to_parquet(os.path.join(path_usr_b, "data.parquet"), index=False)

    print("¡Archivos Parquet generados correctamente en la carpeta 'datos'!")

if __name__ == "__main__":
    main()
