"""TODO(Miguel) — Mapper de Película.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: infrastructure/mappers/genero_mapper.py

Funciones: a_dominio, a_modelo, actualizar_modelo.
Ojo: en la BD "clasificacion" es str ("TP", "+14", "+18"); en el dominio es el
Enum Clasificacion -> convertir con Clasificacion(modelo.clasificacion) y
clasificacion.value.
"""
