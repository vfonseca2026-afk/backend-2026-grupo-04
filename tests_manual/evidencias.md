# Evidencias de pruebas (guía 5.9 / E5)

Cómo repetir las pruebas **sin tocar el código fuente**:

1. Levantar la base y aplicar migraciones (ver README, sección *Ejecución*).
2. Para volver a un estado limpio (aísla los datos de prueba):
   ```bash
   docker compose down -v        # borra el volumen con los datos
   docker compose up -d
   uv run alembic upgrade head
   uv run uvicorn app.main:app --reload   # los seeders cargan los datos base
   ```
3. Ejecutar las solicitudes de `tests_manual/pruebas.http` y completar la
   columna **Obtenido** (agregar captura o copia de la respuesta).

| # | Tipo de caso | Solicitud | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| 1 | CRUD (crear) | `POST /generos` con datos válidos | 201 + género creado | _completar_ | _pendiente_ |
| 2 | Validación inválida | `POST /generos` con nombre de 1 letra | 422 `VALIDATION_ERROR` | _completar_ | _pendiente_ |
| 3 | Recurso inexistente | `GET /generos/9999` | 404 `RESOURCE_NOT_FOUND` | _completar_ | _pendiente_ |
| 4 | Regla de negocio | _definir (ej. reseña duplicada)_ | 409 | _completar_ | _pendiente_ |
| 5 | Filtro/orden/paginación | `GET /peliculas?genero_id=..&ordenar_por=..&pagina=..` | 200 + `items,total,pagina,limite,total_paginas` | _completar_ | _pendiente_ |
| 6 | Persistencia | crear un registro, reiniciar API y base, consultarlo | el registro sigue existiendo | _completar_ | _pendiente_ |
