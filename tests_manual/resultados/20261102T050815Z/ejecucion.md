# Ejecución real de pruebas

Nota: el reinicio por CLI figura como fallido por permisos; fue completado después desde Docker Desktop y se respalda en persistencia_adicional.json. La etiqueta T21b de la pasada automática no demuestra por sí sola reinicio de PostgreSQL. Consultar evidencias.md para el resultado final y su procedencia.

Base: `backend04_pruebas_finales_01`. API temporal: `8002`. Commit: `04576bee5ac560bd2d772150d6070e294666e76e`.

## Comprobaciones

| Caso | Comprobación | Resultado |
|---|---|---|
| T01 | -m alembic current | Aprobado |
| T01 | -m alembic check | Aprobado |
| T02 | Carga explícita sobre tablas ya pobladas | Aprobado |
| T02 | Carga explícita sobre tablas ya pobladas | Aprobado |
| T02 | Repetir carga conserva cantidades | Aprobado |
| T27 | Contrato registrado | Aprobado |
| T02 | Referencias y elegibilidad de reseñas iniciales | Aprobado |
| T02 | Géneros relacionados existentes | Aprobado |
| T02 | Mínimo dos por entidad | Aprobado |
| T02 | Relación película-reseñas 1:N | Aprobado |
| T02 | T02. Consultar géneros iniciales — 200 | Aprobado |
| T02 | T02. Consultar usuarios iniciales — 200, total esperado 6 en base recién sembrada | Aprobado |
| T02 | T02. Consultar películas iniciales — 200, total esperado 10 | Aprobado |
| T02 | T02. Consultar reseñas iniciales — 200, total esperado 10 | Aprobado |
| T03 | T03. Crear género exclusivo QA — 201 | Aprobado |
| T03 | T03. Listar géneros — 200, incluye QA | Aprobado |
| T03 | T03. Obtener género QA — 200 | Aprobado |
| T04 | T04. Actualizar género QA — 200 | Aprobado |
| T04 | Actualización género e identidad | Aprobado |
| T04 | T04. Confirmar modificación e ID/fecha conservados — 200 | Aprobado |
| T04 | Actualización género e identidad | Aprobado |
| T05 | T05. Nombre corto — 422 VALIDATION_ERROR | Aprobado |
| T05 | Estructura uniforme de error | Aprobado |
| T05 | Código de error | Aprobado |
| T05 | T05. PUT omite activo — 422 | Aprobado |
| T05 | Estructura uniforme de error | Aprobado |
| T05 | Código de error | Aprobado |
| T05 | T05. ID cero — 422 | Aprobado |
| T05 | Estructura uniforme de error | Aprobado |
| T05 | Código de error | Aprobado |
| T06 | T06. Género duplicado con mayúsculas — 409 | Aprobado |
| T06 | Estructura uniforme de error | Aprobado |
| T06 | Código de error | Aprobado |
| T07 | T07. Crear usuario activo QA — 201 | Aprobado |
| T07 | T07. Consultar usuario — 200 | Aprobado |
| T07 | T07. Actualizar conservando correo y nombre — 200 | Aprobado |
| T07 | T07. Listado paginado — 200 | Aprobado |
| T18 | Preparación T18. Crear segundo usuario — 201 | Aprobado |
| T18 | Preparación T18. Desactivar usuario — 200 | Aprobado |
| T08 | T08. Correo inválido — 422 | Aprobado |
| T08 | Estructura uniforme de error | Aprobado |
| T08 | Código de error | Aprobado |
| T08 | T08. Correo repetido — 409 | Aprobado |
| T08 | Estructura uniforme de error | Aprobado |
| T08 | Código de error | Aprobado |
| T09 | T09. Crear QA Alfa — 201 | Aprobado |
| T09 | T09. Crear QA Beta — 201 | Aprobado |
| T09 | T09. Crear QA Gamma — 201 | Aprobado |
| T09 | T09. Consultar Alfa — 200 | Aprobado |
| T09 | T09. Actualizar Gamma conservando año y duración — 200 | Aprobado |
| T09 | T09. Confirmar Gamma — 200 | Aprobado |
| T10 | Preparación T10. Crear género sin películas — 201 | Aprobado |
| T10 | Preparación T10. Eliminar género temporal — 204 sin cuerpo | Aprobado |
| T10 | 204 sin cuerpo | Aprobado |
| T10 | T10. Película con género eliminado — 404 | Aprobado |
| T10 | Estructura uniforme de error | Aprobado |
| T10 | Código de error | Aprobado |
| T11 | T11. Duración cero — 422 | Aprobado |
| T11 | Estructura uniforme de error | Aprobado |
| T11 | Código de error | Aprobado |
| T11 | T11. Clasificación inválida — 422 | Aprobado |
| T11 | Estructura uniforme de error | Aprobado |
| T11 | Código de error | Aprobado |
| T12 | T12. Consulta combinada, página 1 — 200, duraciones [120,100]; total=3, total_paginas=2 | Aprobado |
| T12 | Filtro orden y metadatos | Aprobado |
| T13 | T13. Consulta combinada, página 2 — 200, duraciones [80]; total=3, total_paginas=2 | Aprobado |
| T13 | Filtro orden y metadatos | Aprobado |
| T13 | T13. Consulta combinada, página 3 — 200, duraciones []; total=3, total_paginas=2 | Aprobado |
| T13 | Filtro orden y metadatos | Aprobado |
| T14 | T14. Sin coincidencias — 200, items=[], total=0, total_paginas=0 | Aprobado |
| T14 | Sin coincidencias | Aprobado |
| T14 | T14. Parámetro inválido pagina=0 — 422 | Aprobado |
| T14 | Estructura uniforme de error | Aprobado |
| T14 | Código de error | Aprobado |
| T14 | T14. Parámetro inválido limite=101 — 422 | Aprobado |
| T14 | Estructura uniforme de error | Aprobado |
| T14 | Código de error | Aprobado |
| T14 | T14. Parámetro inválido direccion=arriba — 422 | Aprobado |
| T14 | Estructura uniforme de error | Aprobado |
| T14 | Código de error | Aprobado |
| T15 | T15. Eliminar género con películas — 409 | Aprobado |
| T15 | Estructura uniforme de error | Aprobado |
| T15 | Código de error | Aprobado |
| T15 | T15. Género sigue disponible — 200 | Aprobado |
| T15 | T15. Película sigue disponible — 200 | Aprobado |
| T18 | Preparación T18. Género separado para película futura — 201 | Aprobado |
| T18 | Preparación T18. Película futura — 201 | Aprobado |
| T16 | T16. Crear reseña QA — 201 | Aprobado |
| T16 | T16. Obtener reseña — 200 | Aprobado |
| T16 | T16. Listar filtrando pareja QA — 200, total=1 | Aprobado |
| T16 | T16. Reseñas de Alfa — 200, incluye QA | Aprobado |
| T17 | T17. Reseña duplicada — 409 | Aprobado |
| T17 | Estructura uniforme de error | Aprobado |
| T17 | Código de error | Aprobado |
| T17 | T17. Confirmar que no se duplicó — 200, total=1 | Aprobado |
| T17 | Sin duplicados | Aprobado |
| T18 | T18. Usuario inactivo — 400 | Aprobado |
| T18 | Estructura uniforme de error | Aprobado |
| T18 | Código de error | Aprobado |
| T18 | T18. Película futura — 400 | Aprobado |
| T18 | Estructura uniforme de error | Aprobado |
| T18 | Código de error | Aprobado |
| T19 | T19. Puntuación 11 — 422 | Aprobado |
| T19 | Estructura uniforme de error | Aprobado |
| T19 | Código de error | Aprobado |
| T19 | T19. Comentario corto — 422 | Aprobado |
| T19 | Estructura uniforme de error | Aprobado |
| T19 | Código de error | Aprobado |
| T19 | T19. PUT intenta cambiar usuario — 422 | Aprobado |
| T19 | Estructura uniforme de error | Aprobado |
| T19 | Código de error | Aprobado |
| T20 | T20. Actualizar reseña — 200; conservar referencias y fecha | Aprobado |
| T20 | Modificación e identidad conservadas | Aprobado |
| T20 | T20. Consultar modificación — 200 | Aprobado |
| T20 | Modificación e identidad conservadas | Aprobado |
| T01 | -m alembic current | Aprobado |
| T01 | -m alembic check | Aprobado |
| T02 | Carga explícita sobre tablas ya pobladas | Aprobado |
| T02 | Carga explícita sobre tablas ya pobladas | Aprobado |
| T02 | Repetir carga conserva cantidades | Aprobado |
| T27 | Contrato registrado | Aprobado |
| T02 | Referencias y elegibilidad de reseñas iniciales | Aprobado |
| T02 | Géneros relacionados existentes | Aprobado |
| T02 | Mínimo dos por entidad | Aprobado |
| T02 | Relación película-reseñas 1:N | Aprobado |
| T21 | T21a. Consultar después de reiniciar API — 200, datos conservados | Aprobado |
| T21 | Modificación e identidad conservadas | Aprobado |
| T21 | Reinicio PostgreSQL sin borrar volumen | Fallido |
| T21 | T21b. Consultar después de reiniciar PostgreSQL y API — 200, datos conservados | Aprobado |
| T21 | Modificación e identidad conservadas | Aprobado |
| T22 | T22. Eliminar reseña QA — 204 sin cuerpo | Aprobado |
| T22 | 204 sin cuerpo | Aprobado |
| T22 | T22. Recurso eliminado — 404 | Aprobado |
| T22 | Estructura uniforme de error | Aprobado |
| T22 | Código de error | Aprobado |
| T23 | T23. Crear usuario temporal — 201 | Aprobado |
| T23 | T23. Crear película temporal — 201 | Aprobado |
| T23 | T23. Crear reseña relacionada — 201 | Aprobado |
| T23 | T23. Eliminar usuario — 204 | Aprobado |
| T23 | 204 sin cuerpo | Aprobado |
| T23 | T23. Reseña eliminada por cascada — 404 | Aprobado |
| T23 | Estructura uniforme de error | Aprobado |
| T23 | Código de error | Aprobado |
| T23 | T23. Película sigue disponible — 200 | Aprobado |
| T24 | T24. Crear usuario temporal — 201 | Aprobado |
| T24 | T24. Crear película temporal — 201 | Aprobado |
| T24 | T24. Crear reseña relacionada — 201 | Aprobado |
| T24 | T24. Eliminar película — 204 | Aprobado |
| T24 | 204 sin cuerpo | Aprobado |
| T24 | T24. Reseña eliminada por cascada — 404 | Aprobado |
| T24 | Estructura uniforme de error | Aprobado |
| T24 | Código de error | Aprobado |
| T24 | T24. Usuario sigue disponible — 200 | Aprobado |
| T25 | T25. Crear género para CRUD completo — 201 | Aprobado |
| T25 | T25. Listar e identificar género del ciclo — 200 | Aprobado |
| T25 | T25. Obtener género del ciclo — 200 | Aprobado |
| T25 | T25. Actualizar género del ciclo — 200 | Aprobado |
| T25 | T25. Eliminar género del ciclo — 204 sin cuerpo | Aprobado |
| T25 | 204 sin cuerpo | Aprobado |
| T25 | T25. Obtener después de eliminar — 404 | Aprobado |
| T25 | Estructura uniforme de error | Aprobado |
| T25 | Código de error | Aprobado |
| T26 | T26. Reseñas de película eliminada en T24 — 404 | Aprobado |
| T26 | Estructura uniforme de error | Aprobado |
| T26 | Código de error | Aprobado |
| T27 | Batería automatizada | Aprobado |

## Comandos

### ENTORNO — git rev-parse HEAD

Salida: 0

```text
04576bee5ac560bd2d772150d6070e294666e76e

```

### T01 — -m alembic current

Salida: 0

```text
0001 (head)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.

```

### T01 — -m alembic check

Salida: 0

```text
No new upgrade operations detected.
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.ddl.postgresql] Detected sequence named 'resenas_id_seq' as owned by integer column 'resenas(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'peliculas_id_seq' as owned by integer column 'peliculas(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'usuarios_id_seq' as owned by integer column 'usuarios(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'generos_id_seq' as owned by integer column 'generos(id)', assuming SERIAL and omitting

```

### T02 — -m app.seed

Salida: 0

```text
Carga de g�neros omitida: la tabla ya contiene registros.
Carga de usuarios omitida: la tabla ya contiene registros.
Carga de pel�culas omitida: la tabla ya contiene registros.
Carga de rese�as omitida: la tabla ya contiene registros.

```

### T02 — -m app.seed

Salida: 0

```text
Carga de g�neros omitida: la tabla ya contiene registros.
Carga de usuarios omitida: la tabla ya contiene registros.
Carga de pel�culas omitida: la tabla ya contiene registros.
Carga de rese�as omitida: la tabla ya contiene registros.

```

### ENTORNO — git rev-parse HEAD

Salida: 0

```text
04576bee5ac560bd2d772150d6070e294666e76e

```

### T01 — -m alembic current

Salida: 0

```text
0001 (head)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.

```

### T01 — -m alembic check

Salida: 0

```text
No new upgrade operations detected.
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.schemas
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.tables
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.types
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.constraints
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.defaults
INFO  [alembic.runtime.plugins] setting up autogenerate plugin alembic.autogenerate.comments
INFO  [alembic.ddl.postgresql] Detected sequence named 'usuarios_id_seq' as owned by integer column 'usuarios(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'peliculas_id_seq' as owned by integer column 'peliculas(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'resenas_id_seq' as owned by integer column 'resenas(id)', assuming SERIAL and omitting
INFO  [alembic.ddl.postgresql] Detected sequence named 'generos_id_seq' as owned by integer column 'generos(id)', assuming SERIAL and omitting

```

### T02 — -m app.seed

Salida: 0

```text
Carga de g�neros omitida: la tabla ya contiene registros.
Carga de usuarios omitida: la tabla ya contiene registros.
Carga de pel�culas omitida: la tabla ya contiene registros.
Carga de rese�as omitida: la tabla ya contiene registros.

```

### T02 — -m app.seed

Salida: 0

```text
Carga de g�neros omitida: la tabla ya contiene registros.
Carga de usuarios omitida: la tabla ya contiene registros.
Carga de pel�culas omitida: la tabla ya contiene registros.
Carga de rese�as omitida: la tabla ya contiene registros.

```

### T21 — docker compose restart db

Salida: 1

```text
permission denied while trying to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine

```

### T27 — -B -m unittest discover -s tests -v

Salida: 0

```text
test_contrato_publica_operaciones_de_las_cuatro_entidades (test_base_inicial.BaseInicialTests.test_contrato_publica_operaciones_de_las_cuatro_entidades) ... ok
test_crud_completo (test_base_inicial.BaseInicialTests.test_crud_completo) ... ok
test_datos_sobreviven_reapertura_conexiones (test_base_inicial.BaseInicialTests.test_datos_sobreviven_reapertura_conexiones) ... ok
test_duplicado_sin_distinguir_mayusculas (test_base_inicial.BaseInicialTests.test_duplicado_sin_distinguir_mayusculas) ... ok
test_no_elimina_genero_con_peliculas (test_base_inicial.BaseInicialTests.test_no_elimina_genero_con_peliculas) ... ok
test_recurso_inexistente (test_base_inicial.BaseInicialTests.test_recurso_inexistente) ... ok
test_validacion_y_campos_extra (test_base_inicial.BaseInicialTests.test_validacion_y_campos_extra) ... ok

----------------------------------------------------------------------
Ran 7 tests in 1.556s

OK

```

## Solicitudes y respuestas

### 1. T02. Consultar géneros iniciales — 200

`GET http://127.0.0.1:8002/generos` → **200**

Respuesta:
```json
[
  {
    "id": 1,
    "nombre": "Acción",
    "descripcion": "Persecuciones, combates y mucha adrenalina.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.521156Z"
  },
  {
    "id": 4,
    "nombre": "Ciencia ficción",
    "descripcion": "Futuros posibles, tecnología y espacio.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.565760Z"
  },
  {
    "id": 3,
    "nombre": "Comedia",
    "descripcion": "Películas pensadas para hacer reír.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.556381Z"
  },
  {
    "id": 2,
    "nombre": "Drama",
    "descripcion": "Historias intensas centradas en los personajes.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.543466Z"
  },
  {
    "id": 6,
    "nombre": "QA Genero 20261102a",
    "descripcion": "Descripcion QA modificada",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:02:23.523927Z"
  },
  {
    "id": 5,
    "nombre": "Terror",
    "descripcion": "Historias diseñadas para provocar miedo.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.576599Z"
  }
]
```

### 2. T02. Consultar usuarios iniciales — 200, total esperado 6 en base recién sembrada

`GET http://127.0.0.1:8002/usuarios?pagina=1&limite=100` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 1,
      "nombre_usuario": "ana_cine",
      "email": "ana.cine@example.com",
      "activo": true,
      "fecha_registro": "2026-11-02T04:40:00.586569Z"
    },
    {
      "id": 2,
      "nombre_usuario": "bruno_cine",
      "email": "bruno.cine@example.com",
      "activo": true,
      "fecha_registro": "2026-11-02T04:40:00.604415Z"
    },
    {
      "id": 3,
      "nombre_usuario": "carla_cine",
      "email": "carla.cine@example.com",
      "activo": true,
      "fecha_registro": "2026-11-02T04:40:00.617151Z"
    },
    {
      "id": 4,
      "nombre_usuario": "diego_cine",
      "email": "diego.cine@example.com",
      "activo": true,
      "fecha_registro": "2026-11-02T04:40:00.627518Z"
    },
    {
      "id": 5,
      "nombre_usuario": "elena_cine",
      "email": "elena.cine@example.com",
      "activo": true,
      "fecha_registro": "2026-11-02T04:40:00.638259Z"
    },
    {
      "id": 6,
      "nombre_usuario": "fabian_cine",
      "email": "fabian.cine@example.com",
      "activo": false,
      "fecha_registro": "2026-11-02T04:40:00.648430Z"
    }
  ],
  "total": 6,
  "pagina": 1,
  "limite": 100,
  "total_paginas": 1
}
```

### 3. T02. Consultar películas iniciales — 200, total esperado 10

`GET http://127.0.0.1:8002/peliculas?pagina=1&limite=100` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 2,
      "titulo": "Camino al norte",
      "sinopsis": "Sinopsis ficticia de Camino al norte para las demostraciones del proyecto.",
      "anio_estreno": 2021,
      "duracion_min": 95,
      "director": "Luis Ejemplo",
      "clasificacion": "+14",
      "genero_id": 1
    },
    {
      "id": 4,
      "titulo": "Ciudad de sombras",
      "sinopsis": "Sinopsis ficticia de Ciudad de sombras para las demostraciones del proyecto.",
      "anio_estreno": 2020,
      "duracion_min": 100,
      "director": "Pedro Ejemplo",
      "clasificacion": "+18",
      "genero_id": 1
    },
    {
      "id": 8,
      "titulo": "Después de medianoche",
      "sinopsis": "Sinopsis ficticia de Después de medianoche para las demostraciones del proyecto.",
      "anio_estreno": 2023,
      "duracion_min": 120,
      "director": "Diego Ejemplo",
      "clasificacion": "+18",
      "genero_id": 4
    },
    {
      "id": 7,
      "titulo": "Días de verano",
      "sinopsis": "Sinopsis ficticia de Días de verano para las demostraciones del proyecto.",
      "anio_estreno": 2022,
      "duracion_min": 90,
      "director": "Sofía Ejemplo",
      "clasificacion": "TP",
      "genero_id": 4
    },
    {
      "id": 6,
      "titulo": "El secreto del puerto",
      "sinopsis": "Sinopsis ficticia de El secreto del puerto para las demostraciones del proyecto.",
      "anio_estreno": 2021,
      "duracion_min": 115,
      "director": "Carlos Ejemplo",
      "clasificacion": "+14",
      "genero_id": 4
    },
    {
      "id": 1,
      "titulo": "Horizonte lejano",
      "sinopsis": "Sinopsis ficticia de Horizonte lejano para las demostraciones del proyecto.",
      "anio_estreno": 2020,
      "duracion_min": 110,
      "director": "Ana Ejemplo",
      "clasificacion": "TP",
      "genero_id": 1
    },
    {
      "id": 3,
      "titulo": "La última estación",
      "sinopsis": "Sinopsis ficticia de La última estación para las demostraciones del proyecto.",
      "anio_estreno": 2022,
      "duracion_min": 125,
      "director": "Marta Ejemplo",
      "clasificacion": "TP",
      "genero_id": 1
    },
    {
      "id": 10,
      "titulo": "Mañana comienza todo",
      "sinopsis": "Sinopsis ficticia de Mañana comienza todo para las demostraciones del proyecto.",
      "anio_estreno": 2027,
      "duracion_min": 130,
      "director": "Andrés Ejemplo",
      "clasificacion": "+14",
      "genero_id": 4
    },
    {
      "id": 9,
      "titulo": "Una carta pendiente",
      "sinopsis": "Sinopsis ficticia de Una carta pendiente para las demostraciones del proyecto.",
      "anio_estreno": 2024,
      "duracion_min": 98,
      "director": "Laura Ejemplo",
      "clasificacion": "TP",
      "genero_id": 4
    },
    {
      "id": 5,
      "titulo": "Un nuevo comienzo",
      "sinopsis": "Sinopsis ficticia de Un nuevo comienzo para las demostraciones del proyecto.",
      "anio_estreno": 2023,
      "duracion_min": 105,
      "director": "Elena Ejemplo",
      "clasificacion": "TP",
      "genero_id": 1
    }
  ],
  "total": 10,
  "pagina": 1,
  "limite": 100,
  "total_paginas": 1
}
```

### 4. T02. Consultar reseñas iniciales — 200, total esperado 10

`GET http://127.0.0.1:8002/resenas?pagina=1&limite=100` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 1,
      "usuario_id": 1,
      "pelicula_id": 2,
      "puntuacion": 6,
      "titulo": "Opinión de ejemplo 1",
      "comentario": "Reseña ficticia de ana_cine sobre Camino al norte, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.833813Z"
    },
    {
      "id": 2,
      "usuario_id": 2,
      "pelicula_id": 2,
      "puntuacion": 7,
      "titulo": "Opinión de ejemplo 2",
      "comentario": "Reseña ficticia de bruno_cine sobre Camino al norte, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.866174Z"
    },
    {
      "id": 3,
      "usuario_id": 3,
      "pelicula_id": 2,
      "puntuacion": 8,
      "titulo": "Opinión de ejemplo 3",
      "comentario": "Reseña ficticia de carla_cine sobre Camino al norte, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.878343Z"
    },
    {
      "id": 4,
      "usuario_id": 4,
      "pelicula_id": 2,
      "puntuacion": 9,
      "titulo": "Opinión de ejemplo 4",
      "comentario": "Reseña ficticia de diego_cine sobre Camino al norte, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.891753Z"
    },
    {
      "id": 5,
      "usuario_id": 5,
      "pelicula_id": 2,
      "puntuacion": 10,
      "titulo": "Opinión de ejemplo 5",
      "comentario": "Reseña ficticia de elena_cine sobre Camino al norte, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.906132Z"
    },
    {
      "id": 6,
      "usuario_id": 1,
      "pelicula_id": 4,
      "puntuacion": 6,
      "titulo": "Opinión de ejemplo 6",
      "comentario": "Reseña ficticia de ana_cine sobre Ciudad de sombras, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.919162Z"
    },
    {
      "id": 7,
      "usuario_id": 2,
      "pelicula_id": 4,
      "puntuacion": 7,
      "titulo": "Opinión de ejemplo 7",
      "comentario": "Reseña ficticia de bruno_cine sobre Ciudad de sombras, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.931357Z"
    },
    {
      "id": 8,
      "usuario_id": 3,
      "pelicula_id": 4,
      "puntuacion": 8,
      "titulo": "Opinión de ejemplo 8",
      "comentario": "Reseña ficticia de carla_cine sobre Ciudad de sombras, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.944111Z"
    },
    {
      "id": 9,
      "usuario_id": 4,
      "pelicula_id": 4,
      "puntuacion": 9,
      "titulo": "Opinión de ejemplo 9",
      "comentario": "Reseña ficticia de diego_cine sobre Ciudad de sombras, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.957481Z"
    },
    {
      "id": 10,
      "usuario_id": 5,
      "pelicula_id": 4,
      "puntuacion": 10,
      "titulo": "Opinión de ejemplo 10",
      "comentario": "Reseña ficticia de elena_cine sobre Ciudad de sombras, preparada para demostrar la API.",
      "fecha": "2026-11-02T04:40:00.970494Z"
    }
  ],
  "total": 10,
  "pagina": 1,
  "limite": 100,
  "total_paginas": 1
}
```

### 5. T03. Crear género exclusivo QA — 201

`POST http://127.0.0.1:8002/generos` → **201**

Solicitud:
```json
{
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Datos exclusivos de pruebas"
}
```

Respuesta:
```json
{
  "id": 7,
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Datos exclusivos de pruebas",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.065683Z"
}
```

### 6. T03. Listar géneros — 200, incluye QA

`GET http://127.0.0.1:8002/generos` → **200**

Respuesta:
```json
[
  {
    "id": 1,
    "nombre": "Acción",
    "descripcion": "Persecuciones, combates y mucha adrenalina.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.521156Z"
  },
  {
    "id": 4,
    "nombre": "Ciencia ficción",
    "descripcion": "Futuros posibles, tecnología y espacio.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.565760Z"
  },
  {
    "id": 3,
    "nombre": "Comedia",
    "descripcion": "Películas pensadas para hacer reír.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.556381Z"
  },
  {
    "id": 2,
    "nombre": "Drama",
    "descripcion": "Historias intensas centradas en los personajes.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.543466Z"
  },
  {
    "id": 6,
    "nombre": "QA Genero 20261102a",
    "descripcion": "Descripcion QA modificada",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:02:23.523927Z"
  },
  {
    "id": 7,
    "nombre": "QA Genero auto20261102t050715z",
    "descripcion": "Datos exclusivos de pruebas",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:07:28.065683Z"
  },
  {
    "id": 5,
    "nombre": "Terror",
    "descripcion": "Historias diseñadas para provocar miedo.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.576599Z"
  }
]
```

### 7. T03. Obtener género QA — 200

`GET http://127.0.0.1:8002/generos/7` → **200**

Respuesta:
```json
{
  "id": 7,
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Datos exclusivos de pruebas",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.065683Z"
}
```

### 8. T04. Actualizar género QA — 200

`PUT http://127.0.0.1:8002/generos/7` → **200**

Solicitud:
```json
{
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Descripcion QA modificada",
  "activo": true
}
```

Respuesta:
```json
{
  "id": 7,
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Descripcion QA modificada",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.065683Z"
}
```

### 9. T04. Confirmar modificación e ID/fecha conservados — 200

`GET http://127.0.0.1:8002/generos/7` → **200**

Respuesta:
```json
{
  "id": 7,
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Descripcion QA modificada",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.065683Z"
}
```

### 10. T05. Nombre corto — 422 VALIDATION_ERROR

`POST http://127.0.0.1:8002/generos` → **422**

Solicitud:
```json
{
  "nombre": "A"
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.nombre",
        "mensaje": "String should have at least 2 characters",
        "tipo": "string_too_short"
      }
    ]
  }
}
```

### 11. T05. PUT omite activo — 422

`PUT http://127.0.0.1:8002/generos/7` → **422**

Solicitud:
```json
{
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Cambio no valido"
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.activo",
        "mensaje": "Field required",
        "tipo": "missing"
      }
    ]
  }
}
```

### 12. T05. ID cero — 422

`GET http://127.0.0.1:8002/generos/0` → **422**

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "path.genero_id",
        "mensaje": "Input should be greater than 0",
        "tipo": "greater_than"
      }
    ]
  }
}
```

### 13. T06. Género duplicado con mayúsculas — 409

`POST http://127.0.0.1:8002/generos` → **409**

Solicitud:
```json
{
  "nombre": "QA GENERO auto20261102t050715z",
  "descripcion": "Duplicado"
}
```

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_CONFLICT",
    "message": "Ya existe un género con ese nombre.",
    "details": []
  }
}
```

### 14. T07. Crear usuario activo QA — 201

`POST http://127.0.0.1:8002/usuarios` → **201**

Solicitud:
```json
{
  "nombre_usuario": "qa_activo_auto20261102t050715z",
  "email": "qa.activo.auto20261102t050715z@example.com"
}
```

Respuesta:
```json
{
  "id": 7,
  "nombre_usuario": "qa_activo_auto20261102t050715z",
  "email": "qa.activo.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:07:28.155670Z"
}
```

### 15. T07. Consultar usuario — 200

`GET http://127.0.0.1:8002/usuarios/7` → **200**

Respuesta:
```json
{
  "id": 7,
  "nombre_usuario": "qa_activo_auto20261102t050715z",
  "email": "qa.activo.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:07:28.155670Z"
}
```

### 16. T07. Actualizar conservando correo y nombre — 200

`PUT http://127.0.0.1:8002/usuarios/7` → **200**

Solicitud:
```json
{
  "nombre_usuario": "qa_activo_auto20261102t050715z",
  "email": "qa.activo.auto20261102t050715z@example.com",
  "activo": true
}
```

Respuesta:
```json
{
  "id": 7,
  "nombre_usuario": "qa_activo_auto20261102t050715z",
  "email": "qa.activo.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:07:28.155670Z"
}
```

### 17. T07. Listado paginado — 200

`GET http://127.0.0.1:8002/usuarios?pagina=1&limite=1` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 1,
      "nombre_usuario": "ana_cine",
      "email": "ana.cine@example.com",
      "activo": true,
      "fecha_registro": "2026-11-02T04:40:00.586569Z"
    }
  ],
  "total": 7,
  "pagina": 1,
  "limite": 1,
  "total_paginas": 7
}
```

### 18. Preparación T18. Crear segundo usuario — 201

`POST http://127.0.0.1:8002/usuarios` → **201**

Solicitud:
```json
{
  "nombre_usuario": "qa_inactivo_auto20261102t050715z",
  "email": "qa.inactivo.auto20261102t050715z@example.com"
}
```

Respuesta:
```json
{
  "id": 8,
  "nombre_usuario": "qa_inactivo_auto20261102t050715z",
  "email": "qa.inactivo.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:07:28.212899Z"
}
```

### 19. Preparación T18. Desactivar usuario — 200

`PUT http://127.0.0.1:8002/usuarios/8` → **200**

Solicitud:
```json
{
  "nombre_usuario": "qa_inactivo_auto20261102t050715z",
  "email": "qa.inactivo.auto20261102t050715z@example.com",
  "activo": false
}
```

Respuesta:
```json
{
  "id": 8,
  "nombre_usuario": "qa_inactivo_auto20261102t050715z",
  "email": "qa.inactivo.auto20261102t050715z@example.com",
  "activo": false,
  "fecha_registro": "2026-11-02T05:07:28.212899Z"
}
```

### 20. T08. Correo inválido — 422

`POST http://127.0.0.1:8002/usuarios` → **422**

Solicitud:
```json
{
  "nombre_usuario": "qa_email_malo_auto20261102t050715z",
  "email": "correo-invalido"
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.email",
        "mensaje": "value is not a valid email address: An email address must have an @-sign.",
        "tipo": "value_error"
      }
    ]
  }
}
```

### 21. T08. Correo repetido — 409

`POST http://127.0.0.1:8002/usuarios` → **409**

Solicitud:
```json
{
  "nombre_usuario": "qa_otro_auto20261102t050715z",
  "email": "qa.activo.auto20261102t050715z@example.com"
}
```

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_CONFLICT",
    "message": "Ya existe un usuario con ese correo electrónico.",
    "details": []
  }
}
```

### 22. T09. Crear QA Alfa — 201

`POST http://127.0.0.1:8002/peliculas` → **201**

Solicitud:
```json
{
  "titulo": "QA Alfa",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 80,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "id": 11,
  "titulo": "QA Alfa",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 80,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 23. T09. Crear QA Beta — 201

`POST http://127.0.0.1:8002/peliculas` → **201**

Solicitud:
```json
{
  "titulo": "QA Beta",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 120,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "id": 12,
  "titulo": "QA Beta",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 120,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 24. T09. Crear QA Gamma — 201

`POST http://127.0.0.1:8002/peliculas` → **201**

Solicitud:
```json
{
  "titulo": "QA Gamma",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2021,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "id": 13,
  "titulo": "QA Gamma",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2021,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 25. T09. Consultar Alfa — 200

`GET http://127.0.0.1:8002/peliculas/11` → **200**

Respuesta:
```json
{
  "id": 11,
  "titulo": "QA Alfa",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 80,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 26. T09. Actualizar Gamma conservando año y duración — 200

`PUT http://127.0.0.1:8002/peliculas/13` → **200**

Solicitud:
```json
{
  "titulo": "QA Gamma",
  "sinopsis": "Sinopsis modificada para verificar actualizacion",
  "anio_estreno": 2021,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "id": 13,
  "titulo": "QA Gamma",
  "sinopsis": "Sinopsis modificada para verificar actualizacion",
  "anio_estreno": 2021,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 27. T09. Confirmar Gamma — 200

`GET http://127.0.0.1:8002/peliculas/13` → **200**

Respuesta:
```json
{
  "id": 13,
  "titulo": "QA Gamma",
  "sinopsis": "Sinopsis modificada para verificar actualizacion",
  "anio_estreno": 2021,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 28. Preparación T10. Crear género sin películas — 201

`POST http://127.0.0.1:8002/generos` → **201**

Solicitud:
```json
{
  "nombre": "QA Borrable auto20261102t050715z",
  "descripcion": "Temporal"
}
```

Respuesta:
```json
{
  "id": 8,
  "nombre": "QA Borrable auto20261102t050715z",
  "descripcion": "Temporal",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.343489Z"
}
```

### 29. Preparación T10. Eliminar género temporal — 204 sin cuerpo

`DELETE http://127.0.0.1:8002/generos/8` → **204**

Respuesta:
```json
""
```

### 30. T10. Película con género eliminado — 404

`POST http://127.0.0.1:8002/peliculas` → **404**

Solicitud:
```json
{
  "titulo": "QA Referencia inexistente",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 8
}
```

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No existe el género con ID 8.",
    "details": []
  }
}
```

### 31. T11. Duración cero — 422

`POST http://127.0.0.1:8002/peliculas` → **422**

Solicitud:
```json
{
  "titulo": "QA Duracion invalida",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 0,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.duracion_min",
        "mensaje": "Input should be greater than 0",
        "tipo": "greater_than"
      }
    ]
  }
}
```

### 32. T11. Clasificación inválida — 422

`POST http://127.0.0.1:8002/peliculas` → **422**

Solicitud:
```json
{
  "titulo": "QA Clasificacion invalida",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "INVALIDA",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.clasificacion",
        "mensaje": "Input should be 'TP', '+14' or '+18'",
        "tipo": "enum"
      }
    ]
  }
}
```

### 33. T12. Consulta combinada, página 1 — 200, duraciones [120,100]; total=3, total_paginas=2

`GET http://127.0.0.1:8002/peliculas?genero_id=7&ordenar_por=duracion_min&direccion=desc&pagina=1&limite=2` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 12,
      "titulo": "QA Beta",
      "sinopsis": "Pelicula ficticia de pruebas",
      "anio_estreno": 2020,
      "duracion_min": 120,
      "director": "Director QA",
      "clasificacion": "TP",
      "genero_id": 7
    },
    {
      "id": 13,
      "titulo": "QA Gamma",
      "sinopsis": "Sinopsis modificada para verificar actualizacion",
      "anio_estreno": 2021,
      "duracion_min": 100,
      "director": "Director QA",
      "clasificacion": "TP",
      "genero_id": 7
    }
  ],
  "total": 3,
  "pagina": 1,
  "limite": 2,
  "total_paginas": 2
}
```

### 34. T13. Consulta combinada, página 2 — 200, duraciones [80]; total=3, total_paginas=2

`GET http://127.0.0.1:8002/peliculas?genero_id=7&ordenar_por=duracion_min&direccion=desc&pagina=2&limite=2` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 11,
      "titulo": "QA Alfa",
      "sinopsis": "Pelicula ficticia de pruebas",
      "anio_estreno": 2020,
      "duracion_min": 80,
      "director": "Director QA",
      "clasificacion": "TP",
      "genero_id": 7
    }
  ],
  "total": 3,
  "pagina": 2,
  "limite": 2,
  "total_paginas": 2
}
```

### 35. T13. Consulta combinada, página 3 — 200, duraciones []; total=3, total_paginas=2

`GET http://127.0.0.1:8002/peliculas?genero_id=7&ordenar_por=duracion_min&direccion=desc&pagina=3&limite=2` → **200**

Respuesta:
```json
{
  "items": [],
  "total": 3,
  "pagina": 3,
  "limite": 2,
  "total_paginas": 2
}
```

### 36. T14. Sin coincidencias — 200, items=[], total=0, total_paginas=0

`GET http://127.0.0.1:8002/peliculas?genero_id=7&titulo=texto_sin_coincidencias_auto20261102t050715z&pagina=1&limite=2` → **200**

Respuesta:
```json
{
  "items": [],
  "total": 0,
  "pagina": 1,
  "limite": 2,
  "total_paginas": 0
}
```

### 37. T14. Parámetro inválido pagina=0 — 422

`GET http://127.0.0.1:8002/peliculas?pagina=0` → **422**

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "query.pagina",
        "mensaje": "Input should be greater than or equal to 1",
        "tipo": "greater_than_equal"
      }
    ]
  }
}
```

### 38. T14. Parámetro inválido limite=101 — 422

`GET http://127.0.0.1:8002/peliculas?limite=101` → **422**

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "query.limite",
        "mensaje": "Input should be less than or equal to 100",
        "tipo": "less_than_equal"
      }
    ]
  }
}
```

### 39. T14. Parámetro inválido direccion=arriba — 422

`GET http://127.0.0.1:8002/peliculas?direccion=arriba` → **422**

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "query.direccion",
        "mensaje": "Input should be 'asc' or 'desc'",
        "tipo": "literal_error"
      }
    ]
  }
}
```

### 40. T15. Eliminar género con películas — 409

`DELETE http://127.0.0.1:8002/generos/7` → **409**

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_CONFLICT",
    "message": "No se puede eliminar un género que tiene películas asociadas.",
    "details": []
  }
}
```

### 41. T15. Género sigue disponible — 200

`GET http://127.0.0.1:8002/generos/7` → **200**

Respuesta:
```json
{
  "id": 7,
  "nombre": "QA Genero auto20261102t050715z",
  "descripcion": "Descripcion QA modificada",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.065683Z"
}
```

### 42. T15. Película sigue disponible — 200

`GET http://127.0.0.1:8002/peliculas/11` → **200**

Respuesta:
```json
{
  "id": 11,
  "titulo": "QA Alfa",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 80,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 43. Preparación T18. Género separado para película futura — 201

`POST http://127.0.0.1:8002/generos` → **201**

Solicitud:
```json
{
  "nombre": "QA Futuro auto20261102t050715z",
  "descripcion": "Separado del filtro de tres peliculas"
}
```

Respuesta:
```json
{
  "id": 9,
  "nombre": "QA Futuro auto20261102t050715z",
  "descripcion": "Separado del filtro de tres peliculas",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:07:28.458374Z"
}
```

### 44. Preparación T18. Película futura — 201

`POST http://127.0.0.1:8002/peliculas` → **201**

Solicitud:
```json
{
  "titulo": "QA Pelicula futura",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2027,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 9
}
```

Respuesta:
```json
{
  "id": 14,
  "titulo": "QA Pelicula futura",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2027,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 9
}
```

### 45. T16. Crear reseña QA — 201

`POST http://127.0.0.1:8002/resenas` → **201**

Solicitud:
```json
{
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "id": 11,
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API.",
  "fecha": "2026-11-02T05:07:28.489133Z"
}
```

### 46. T16. Obtener reseña — 200

`GET http://127.0.0.1:8002/resenas/11` → **200**

Respuesta:
```json
{
  "id": 11,
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API.",
  "fecha": "2026-11-02T05:07:28.489133Z"
}
```

### 47. T16. Listar filtrando pareja QA — 200, total=1

`GET http://127.0.0.1:8002/resenas?usuario_id=7&pelicula_id=11&pagina=1&limite=10` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 11,
      "usuario_id": 7,
      "pelicula_id": 11,
      "puntuacion": 8,
      "titulo": "Opinion QA",
      "comentario": "Comentario suficiente para verificar la API.",
      "fecha": "2026-11-02T05:07:28.489133Z"
    }
  ],
  "total": 1,
  "pagina": 1,
  "limite": 10,
  "total_paginas": 1
}
```

### 48. T16. Reseñas de Alfa — 200, incluye QA

`GET http://127.0.0.1:8002/peliculas/11/resenas?pagina=1&limite=10` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 11,
      "usuario_id": 7,
      "pelicula_id": 11,
      "puntuacion": 8,
      "titulo": "Opinion QA",
      "comentario": "Comentario suficiente para verificar la API.",
      "fecha": "2026-11-02T05:07:28.489133Z"
    }
  ],
  "total": 1,
  "pagina": 1,
  "limite": 10,
  "total_paginas": 1
}
```

### 49. T17. Reseña duplicada — 409

`POST http://127.0.0.1:8002/resenas` → **409**

Solicitud:
```json
{
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_CONFLICT",
    "message": "El usuario ya tiene una reseña de esta película.",
    "details": []
  }
}
```

### 50. T17. Confirmar que no se duplicó — 200, total=1

`GET http://127.0.0.1:8002/resenas?usuario_id=7&pelicula_id=11` → **200**

Respuesta:
```json
{
  "items": [
    {
      "id": 11,
      "usuario_id": 7,
      "pelicula_id": 11,
      "puntuacion": 8,
      "titulo": "Opinion QA",
      "comentario": "Comentario suficiente para verificar la API.",
      "fecha": "2026-11-02T05:07:28.489133Z"
    }
  ],
  "total": 1,
  "pagina": 1,
  "limite": 10,
  "total_paginas": 1
}
```

### 51. T18. Usuario inactivo — 400

`POST http://127.0.0.1:8002/resenas` → **400**

Solicitud:
```json
{
  "usuario_id": 8,
  "pelicula_id": 11,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "error": {
    "code": "BUSINESS_RULE_VIOLATION",
    "message": "Un usuario inactivo no puede publicar ni editar reseñas.",
    "details": []
  }
}
```

### 52. T18. Película futura — 400

`POST http://127.0.0.1:8002/resenas` → **400**

Solicitud:
```json
{
  "usuario_id": 7,
  "pelicula_id": 14,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "error": {
    "code": "BUSINESS_RULE_VIOLATION",
    "message": "No se puede reseñar una película cuyo año de estreno sea posterior al año actual.",
    "details": []
  }
}
```

### 53. T19. Puntuación 11 — 422

`POST http://127.0.0.1:8002/resenas` → **422**

Solicitud:
```json
{
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 11,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.puntuacion",
        "mensaje": "Input should be less than or equal to 10",
        "tipo": "less_than_equal"
      }
    ]
  }
}
```

### 54. T19. Comentario corto — 422

`POST http://127.0.0.1:8002/resenas` → **422**

Solicitud:
```json
{
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Corto"
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.comentario",
        "mensaje": "String should have at least 10 characters",
        "tipo": "string_too_short"
      }
    ]
  }
}
```

### 55. T19. PUT intenta cambiar usuario — 422

`PUT http://127.0.0.1:8002/resenas/11` → **422**

Solicitud:
```json
{
  "puntuacion": 9,
  "titulo": "Actualizada",
  "comentario": "Comentario actualizado suficientemente largo.",
  "usuario_id": 7
}
```

Respuesta:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Los datos enviados no cumplen las validaciones.",
    "details": [
      {
        "campo": "body.usuario_id",
        "mensaje": "Extra inputs are not permitted",
        "tipo": "extra_forbidden"
      }
    ]
  }
}
```

### 56. T20. Actualizar reseña — 200; conservar referencias y fecha

`PUT http://127.0.0.1:8002/resenas/11` → **200**

Solicitud:
```json
{
  "puntuacion": 9,
  "titulo": "Opinion QA modificada",
  "comentario": "Comentario modificado para comprobar persistencia."
}
```

Respuesta:
```json
{
  "id": 11,
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 9,
  "titulo": "Opinion QA modificada",
  "comentario": "Comentario modificado para comprobar persistencia.",
  "fecha": "2026-11-02T05:07:28.489133Z"
}
```

### 57. T20. Consultar modificación — 200

`GET http://127.0.0.1:8002/resenas/11` → **200**

Respuesta:
```json
{
  "id": 11,
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 9,
  "titulo": "Opinion QA modificada",
  "comentario": "Comentario modificado para comprobar persistencia.",
  "fecha": "2026-11-02T05:07:28.489133Z"
}
```

### 58. T21a. Consultar después de reiniciar API — 200, datos conservados

`GET http://127.0.0.1:8002/resenas/11` → **200**

Respuesta:
```json
{
  "id": 11,
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 9,
  "titulo": "Opinion QA modificada",
  "comentario": "Comentario modificado para comprobar persistencia.",
  "fecha": "2026-11-02T05:07:28.489133Z"
}
```

### 59. T21b. Consultar después de reiniciar PostgreSQL y API — 200, datos conservados

`GET http://127.0.0.1:8002/resenas/11` → **200**

Respuesta:
```json
{
  "id": 11,
  "usuario_id": 7,
  "pelicula_id": 11,
  "puntuacion": 9,
  "titulo": "Opinion QA modificada",
  "comentario": "Comentario modificado para comprobar persistencia.",
  "fecha": "2026-11-02T05:07:28.489133Z"
}
```

### 60. T22. Eliminar reseña QA — 204 sin cuerpo

`DELETE http://127.0.0.1:8002/resenas/11` → **204**

Respuesta:
```json
""
```

### 61. T22. Recurso eliminado — 404

`GET http://127.0.0.1:8002/resenas/11` → **404**

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No existe una reseña con el ID solicitado.",
    "details": []
  }
}
```

### 62. T23. Crear usuario temporal — 201

`POST http://127.0.0.1:8002/usuarios` → **201**

Solicitud:
```json
{
  "nombre_usuario": "qa_cascada_usuario_auto20261102t050715z",
  "email": "qa.cascada.usuario.auto20261102t050715z@example.com"
}
```

Respuesta:
```json
{
  "id": 9,
  "nombre_usuario": "qa_cascada_usuario_auto20261102t050715z",
  "email": "qa.cascada.usuario.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:08:36.924894Z"
}
```

### 63. T23. Crear película temporal — 201

`POST http://127.0.0.1:8002/peliculas` → **201**

Solicitud:
```json
{
  "titulo": "QA Cascada Usuario",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "id": 15,
  "titulo": "QA Cascada Usuario",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 64. T23. Crear reseña relacionada — 201

`POST http://127.0.0.1:8002/resenas` → **201**

Solicitud:
```json
{
  "usuario_id": 9,
  "pelicula_id": 15,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "id": 12,
  "usuario_id": 9,
  "pelicula_id": 15,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API.",
  "fecha": "2026-11-02T05:08:36.968948Z"
}
```

### 65. T23. Eliminar usuario — 204

`DELETE http://127.0.0.1:8002/usuarios/9` → **204**

Respuesta:
```json
""
```

### 66. T23. Reseña eliminada por cascada — 404

`GET http://127.0.0.1:8002/resenas/12` → **404**

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No existe una reseña con el ID solicitado.",
    "details": []
  }
}
```

### 67. T23. Película sigue disponible — 200

`GET http://127.0.0.1:8002/peliculas/15` → **200**

Respuesta:
```json
{
  "id": 15,
  "titulo": "QA Cascada Usuario",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 68. T24. Crear usuario temporal — 201

`POST http://127.0.0.1:8002/usuarios` → **201**

Solicitud:
```json
{
  "nombre_usuario": "qa_cascada_pelicula_auto20261102t050715z",
  "email": "qa.cascada.pelicula.auto20261102t050715z@example.com"
}
```

Respuesta:
```json
{
  "id": 10,
  "nombre_usuario": "qa_cascada_pelicula_auto20261102t050715z",
  "email": "qa.cascada.pelicula.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:08:37.026437Z"
}
```

### 69. T24. Crear película temporal — 201

`POST http://127.0.0.1:8002/peliculas` → **201**

Solicitud:
```json
{
  "titulo": "QA Cascada Pelicula",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

Respuesta:
```json
{
  "id": 16,
  "titulo": "QA Cascada Pelicula",
  "sinopsis": "Pelicula ficticia de pruebas",
  "anio_estreno": 2020,
  "duracion_min": 100,
  "director": "Director QA",
  "clasificacion": "TP",
  "genero_id": 7
}
```

### 70. T24. Crear reseña relacionada — 201

`POST http://127.0.0.1:8002/resenas` → **201**

Solicitud:
```json
{
  "usuario_id": 10,
  "pelicula_id": 16,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API."
}
```

Respuesta:
```json
{
  "id": 13,
  "usuario_id": 10,
  "pelicula_id": 16,
  "puntuacion": 8,
  "titulo": "Opinion QA",
  "comentario": "Comentario suficiente para verificar la API.",
  "fecha": "2026-11-02T05:08:37.059625Z"
}
```

### 71. T24. Eliminar película — 204

`DELETE http://127.0.0.1:8002/peliculas/16` → **204**

Respuesta:
```json
""
```

### 72. T24. Reseña eliminada por cascada — 404

`GET http://127.0.0.1:8002/resenas/13` → **404**

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No existe una reseña con el ID solicitado.",
    "details": []
  }
}
```

### 73. T24. Usuario sigue disponible — 200

`GET http://127.0.0.1:8002/usuarios/10` → **200**

Respuesta:
```json
{
  "id": 10,
  "nombre_usuario": "qa_cascada_pelicula_auto20261102t050715z",
  "email": "qa.cascada.pelicula.auto20261102t050715z@example.com",
  "activo": true,
  "fecha_registro": "2026-11-02T05:08:37.026437Z"
}
```

### 74. T25. Crear género para CRUD completo — 201

`POST http://127.0.0.1:8002/generos` → **201**

Solicitud:
```json
{
  "nombre": "QA Ciclo auto20261102t050715z",
  "descripcion": "Inicio"
}
```

Respuesta:
```json
{
  "id": 10,
  "nombre": "QA Ciclo auto20261102t050715z",
  "descripcion": "Inicio",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:08:37.128738Z"
}
```

### 75. T25. Listar e identificar género del ciclo — 200

`GET http://127.0.0.1:8002/generos` → **200**

Respuesta:
```json
[
  {
    "id": 1,
    "nombre": "Acción",
    "descripcion": "Persecuciones, combates y mucha adrenalina.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.521156Z"
  },
  {
    "id": 4,
    "nombre": "Ciencia ficción",
    "descripcion": "Futuros posibles, tecnología y espacio.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.565760Z"
  },
  {
    "id": 3,
    "nombre": "Comedia",
    "descripcion": "Películas pensadas para hacer reír.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.556381Z"
  },
  {
    "id": 2,
    "nombre": "Drama",
    "descripcion": "Historias intensas centradas en los personajes.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.543466Z"
  },
  {
    "id": 10,
    "nombre": "QA Ciclo auto20261102t050715z",
    "descripcion": "Inicio",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:08:37.128738Z"
  },
  {
    "id": 9,
    "nombre": "QA Futuro auto20261102t050715z",
    "descripcion": "Separado del filtro de tres peliculas",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:07:28.458374Z"
  },
  {
    "id": 6,
    "nombre": "QA Genero 20261102a",
    "descripcion": "Descripcion QA modificada",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:02:23.523927Z"
  },
  {
    "id": 7,
    "nombre": "QA Genero auto20261102t050715z",
    "descripcion": "Descripcion QA modificada",
    "activo": true,
    "fecha_creacion": "2026-11-02T05:07:28.065683Z"
  },
  {
    "id": 5,
    "nombre": "Terror",
    "descripcion": "Historias diseñadas para provocar miedo.",
    "activo": true,
    "fecha_creacion": "2026-11-02T04:40:00.576599Z"
  }
]
```

### 76. T25. Obtener género del ciclo — 200

`GET http://127.0.0.1:8002/generos/10` → **200**

Respuesta:
```json
{
  "id": 10,
  "nombre": "QA Ciclo auto20261102t050715z",
  "descripcion": "Inicio",
  "activo": true,
  "fecha_creacion": "2026-11-02T05:08:37.128738Z"
}
```

### 77. T25. Actualizar género del ciclo — 200

`PUT http://127.0.0.1:8002/generos/10` → **200**

Solicitud:
```json
{
  "nombre": "QA Ciclo modificado auto20261102t050715z",
  "descripcion": "Actualizado",
  "activo": false
}
```

Respuesta:
```json
{
  "id": 10,
  "nombre": "QA Ciclo modificado auto20261102t050715z",
  "descripcion": "Actualizado",
  "activo": false,
  "fecha_creacion": "2026-11-02T05:08:37.128738Z"
}
```

### 78. T25. Eliminar género del ciclo — 204 sin cuerpo

`DELETE http://127.0.0.1:8002/generos/10` → **204**

Respuesta:
```json
""
```

### 79. T25. Obtener después de eliminar — 404

`GET http://127.0.0.1:8002/generos/10` → **404**

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No existe un género con el ID solicitado.",
    "details": []
  }
}
```

### 80. T26. Reseñas de película eliminada en T24 — 404

`GET http://127.0.0.1:8002/peliculas/16/resenas` → **404**

Respuesta:
```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "No existe una película con el ID solicitado.",
    "details": []
  }
}
```

## Hallazgo adicional

Reiniciar PostgreSQL con la API abierta produjo primero HTTP 500 y después 200; reiniciando también la API se obtuvo 200 a la primera. Ver persistencia_adicional.json y T28 en evidencias.md. No confundir la aprobación de T21 con recuperación transparente del pool.
