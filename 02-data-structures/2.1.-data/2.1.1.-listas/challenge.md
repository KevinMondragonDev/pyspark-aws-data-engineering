# 📋 Reto 1 — Listas: La Lista de Invitados (Dinámica)

> **Objetivo:** Practicar la mutabilidad y las operaciones fundamentales sobre listas.

---

## Instrucciones

Crea una lista llamada `lista_invitados` con 3 nombres iniciales y realiza las siguientes operaciones en orden:

1. Agrega a `"Carlos"` al **final** usando `.append()`.
2. Inserta a `"Ana"` en la **posición 1** usando `.insert()`.
3. Cambia al invitado de la **posición 0** por `"Pedro"` (acceso directo por índice).
4. Elimina al invitado de la **posición 2** usando `.pop(2)` o `del`.
5. Imprime la lista final y su longitud con `len()`.

## Estructura esperada

```python
lista_invitados = ["Luis", "Sofía", "Marta"]

lista_invitados.append("Carlos")
lista_invitados.insert(1, "Ana")
lista_invitados[0] = "Pedro"
lista_invitados.pop(2)

print(lista_invitados)
print(len(lista_invitados))
```

## Conceptos clave

| Operación         | Método / Sintaxis      | Descripción                              |
|-------------------|------------------------|------------------------------------------|
| Agregar al final  | `.append(valor)`       | Añade un elemento al final               |
| Insertar en pos.  | `.insert(i, valor)`    | Inserta en el índice especificado        |
| Modificar         | `lista[i] = valor`     | Reemplaza el elemento en esa posición    |
| Eliminar por pos. | `.pop(i)` / `del`      | Quita el elemento en ese índice          |
| Longitud          | `len(lista)`           | Devuelve cuántos elementos hay           |
