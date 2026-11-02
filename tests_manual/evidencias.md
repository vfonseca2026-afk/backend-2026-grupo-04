# Evidencias de pruebas — Grupo 04

Estado: 27 casos de la matriz completados. T01 y la carga inicial desde cero de T02 incorporan la salida real aportada por Vicente en esta conversación; se repitieron current/check, la carga sobre tablas pobladas y las consultas. Se ejecutaron 80 solicitudes HTTP y una comprobación adicional de persistencia tras reinicio real de PostgreSQL, sin fallos en los códigos esperados de la matriz. Se detectó además una incidencia de reconexión al reiniciar solo PostgreSQL sin reiniciar la API, documentada como observación adicional. Siete pruebas automatizadas aprobadas. Los resultados detallados y los límites se registran al final.

## Entorno y versión

Completar antes de ejecutar:

| Dato | Valor |
|---|---|
| Fecha y responsable | 2 de noviembre de 2026, America/Santiago. Ejecución asistida por Codex, autorizada por Vicente Fonseca. |
| Rama y commit (`git branch --show-current`, `git rev-parse HEAD`) | feature/integracion-documentacion; `04576bee5ac560bd2d772150d6070e294666e76e`. Documentación con cambios locales durante la ejecución. |
| Base exclusiva de pruebas | `backend04_pruebas_finales_01` |
| Puerto de la API | 8001 en ejecución manual previa; 8002 en API temporal controlada para verificar explícitamente la base. |
| Revisión aplicada (`uv run alembic current`) | `0001 (head)` |
| Resultado de `uv run alembic check` | `No new upgrade operations detected.` |

## Preparación sin modificar código ni borrar datos de trabajo

Ejecutar desde la raíz de una copia actualizada con las cuatro entidades integradas. Docker debe estar funcionando. Conservar las variables de conexión del .env local, sin publicarlo ni incluirlo en capturas.

Crear una base nueva en el PostgreSQL de este proyecto (usuario `cine`; sustituir si el entorno usa otro):

```powershell
docker compose ps
docker compose exec db createdb -U cine backend04_pruebas_20261102
```

Si la base ya existe, no asumir que está limpia ni eliminarla: utilizar otro nombre y registrarlo. Si el contenedor pertenece a otra copia, ejecutar Compose desde la carpeta que lo creó o seleccionar explícitamente su proyecto con `-p`.

En una terminal dedicada a pruebas, establecer el nombre de esa base solo para el proceso actual:

```powershell
$env:DB_NAME = "backend04_pruebas_20261102"
uv sync
uv run python -c "from infrastructure.database import engine; print('Base destino:', engine.url.database)"
```

Confirmar el destino antes de continuar. Esta variable de entorno tiene prioridad sobre el valor de .env con la configuración actual de python-dotenv. Mantener esta terminal para los comandos siguientes. No ejecutar Docker Compose para crear otro contenedor después de cambiar DB_NAME: se está reutilizando PostgreSQL existente.

```powershell
uv run alembic upgrade head
uv run alembic current
uv run alembic check
uv run python -m app.seed
uv run python -m app.seed
uv run uvicorn app.main:app --reload --port 8001
```

Los seeders se ejecutan explícitamente; arrancar Uvicorn no carga datos. Registrar salidas de migración y de ambas cargas. La segunda debe omitir las cuatro tablas pobladas y conservar sus cantidades.

Antes de crear datos adicionales, verificar los datos de ejemplo mediante las colecciones: al menos dos registros por entidad, relaciones válidas y una relación 1:N observable. Según los seeders preparados se esperan 5 géneros, 6 usuarios (uno inactivo), 10 películas (una futura) y 10 reseñas en una base vacía. Contrastar estas cantidades con la versión ejecutada; cualquier diferencia se investiga, no se corrige manualmente en las evidencias.

## Datos exclusivos de los casos

Crear mediante HTTP, en orden, y registrar los IDs reales devueltos:

1. Género `QA Genero 20261102`, descripción `Datos exclusivos de pruebas`.
2. Usuario activo `qa_activo_20261102`, correo `qa.activo.20261102@example.com`.
3. Usuario `qa_inactivo_20261102`, correo `qa.inactivo.20261102@example.com`; actualizar mediante PUT conservando nombre/correo y enviando `activo: false`.
4. Tres películas del género QA: `QA Alfa` (2020, 80 minutos), `QA Beta` (2020, 120 minutos) y `QA Gamma` (2021, 100 minutos). Para todas: sinopsis `Pelicula ficticia de pruebas`, director `Director QA`, clasificación `TP`.
5. Una película futura en un género distinto al QA (puede ser un género inicial), con año posterior al año actual; usar un ID real. Así no altera las tres coincidencias del filtro QA.
6. Una reseña del usuario activo sobre QA Alfa: puntuación 8, título `Opinion QA`, comentario `Comentario suficiente para verificar la API.`

Los IDs de los ejemplos de Swagger no son datos garantizados. Guardar en las variables de pruebas.http los IDs de género, usuarios, películas y reseña. Para inexistencia usar el ID del recurso recién eliminado; no asumir que 9999 está libre.

| Referencia | ID obtenido |
|---|---|
| Género QA | Pendiente |
| Usuario activo QA | Pendiente |
| Usuario inactivo QA | Pendiente |
| QA Alfa | Pendiente |
| QA Beta | Pendiente |
| QA Gamma | Pendiente |
| Película futura | Pendiente |
| Reseña QA | Pendiente |

## Matriz de ejecución

`P` = pendiente. Completar Obtenido con estado HTTP, datos relevantes y enlace a respuesta/captura. No marcar aprobado por el ejemplo de Responses en Swagger.

| Caso | Entrada o procedimiento | Resultado esperado | Obtenido / evidencia | Estado |
|---|---|---|---|---|
| T01 | Migración sobre base nueva; current; check | Se aplica 0001, current indica head y check no detecta operaciones | Aplicación inicial 0001 aportada por Vicente; current=0001 (head) y check sin diferencias, repetidos durante esta ejecución. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T02 | Carga inicial dos veces; consultar cuatro colecciones | Datos coherentes, mínimo dos por entidad; segunda ejecución no duplica | Carga inicial aportada por Vicente: 5 géneros, 6 usuarios, 10 películas y 10 reseñas. Repetición asistida conserva cantidades (incluido un género QA previo). Referencias y usuarios activos/películas estrenadas coherentes; relación 1:N confirmada. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T03 | POST del género QA; GET colección e individual | 201 con ID; 200 e inclusión en listado | POST 201 con ID 7; GET listado e individual 200, datos coincidentes e inclusión confirmada. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T04 | PUT género QA con nombre, descripción y activo | 200; se conservan ID y fecha; los nuevos datos se recuperan por GET | PUT y GET 200; descripción modificada; ID y fecha conservados. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T05 | POST género con nombre `A`; PUT sin activo; GET /generos/0 | 422 VALIDATION_ERROR en cada solicitud; details identifica el campo | Tres respuestas 422 con VALIDATION_ERROR y estructura uniforme. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T06 | POST del nombre QA existente cambiando mayúsculas | 409 RESOURCE_CONFLICT; no agrega género | 409 RESOURCE_CONFLICT ante nombre QA repetido con mayúsculas. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T07 | POST/GET/PUT usuario QA; conservar su correo al actualizar; listado pagina=1&limite=1 | 201/200; actualización propia permitida; metadatos coherentes | POST 201; GET individual, PUT con valores propios y listado paginado 200. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T08 | POST usuario con correo inválido; otro con correo QA existente y nombre distinto | 422 y 409 respectivamente; estructura uniforme | Correo inválido: 422; correo duplicado: 409; códigos de error correctos. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T09 | Crear tres películas QA; GET y PUT QA Gamma con todos los campos | 201/200; cambios persistidos e ID conservado; mantener duración 100 y año 2021 | Tres POST 201; GET y PUT 200; modificación de sinopsis confirmada e ID conservado. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T10 | POST película con genero_id de un género temporal creado y eliminado previamente | 404 RESOURCE_NOT_FOUND; no crea película | Género temporal creado y eliminado; POST película referenciándolo: 404 RESOURCE_NOT_FOUND. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T11 | POST película con duración 0 o clasificación no permitida | 422 VALIDATION_ERROR | Duración cero y clasificación inválida: 422 VALIDATION_ERROR. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T12 | GET /peliculas?genero_id=ID_QA&ordenar_por=duracion_min&direccion=desc&pagina=1&limite=2 | 200; duraciones [120,100]; total=3; pagina=1; limite=2; total_paginas=2 | 200; duraciones [120,100], total=3, pagina=1, limite=2, total_paginas=2; género filtrado correcto. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T13 | Misma consulta con pagina=2; repetir con pagina=3 | Página 2: [80]; página 3: items=[]; ambas conservan total=3 y total_paginas=2 | Página 2: [80]; página 3: []; ambas 200, total=3 y total_paginas=2. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T14 | Filtro QA y titulo=texto_sin_coincidencias; consulta con pagina=0, limite=101 o direccion=arriba | Sin coincidencias: 200,total=0,total_paginas=0; parámetros inválidos: 422 | Sin coincidencias: 200, items=[], total=0 y total_paginas=0. Tres parámetros inválidos: 422. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T15 | DELETE género QA mientras mantiene películas | 409 RESOURCE_CONFLICT; género y películas siguen disponibles | DELETE género relacionado:409; género y película siguen consultables con 200. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T16 | POST reseña QA válida; GET individual, general y por película | 201 con fecha; 200; incluida en ambas colecciones | POST 201 con fecha; GET individual, listado filtrado y consulta por película:200; reseña incluida. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T17 | Repetir POST del usuario y película de T16 | 409 RESOURCE_CONFLICT; conserva una reseña para la pareja | Segundo POST de misma pareja:409; listado conserva total=1. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T18 | POST con usuario inactivo y película estrenada; POST con usuario activo y película futura | 400 BUSINESS_RULE_VIOLATION en ambos casos | Usuario inactivo y película futura:400 BUSINESS_RULE_VIOLATION en ambos casos. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T19 | POST reseña con puntuación 11 o comentario corto; PUT incluyendo usuario_id | 422 VALIDATION_ERROR | Puntuación 11, comentario corto e intento de cambiar usuario en PUT:422. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T20 | PUT reseña QA con puntuación 9, título y comentario válidos | 200; conserva ID, usuario, película y fecha | PUT y GET 200; puntuación=9, título modificado; ID, usuario, película y fecha conservados. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T21 | Actualizar dato QA; detener/reiniciar API; GET; detener API, reiniciar db conservando volumen, esperar healthy, iniciar API con misma base y consultar | El dato modificado y sus referencias se conservan en ambos reinicios | Persistencia tras reinicio de API:200, datos conservados. Reinicio PostgreSQL confirmado por cambio de pg_postmaster_start_time, 2026-11-02 04:39:05.852476+00:00 → 2026-11-02 05:11:08.248629+00:00. Reseña adicional ID 14:GET 200 e igualdad íntegra con la modificación previa. Sin borrar volumen. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T22 | Crear reseña temporal independiente; DELETE y GET del mismo ID | 204 sin cuerpo; luego 404 RESOURCE_NOT_FOUND | DELETE 204 sin cuerpo; GET posterior:404 RESOURCE_NOT_FOUND. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T23 | Crear usuario y película temporales con reseña; eliminar usuario y consultar reseña | DELETE usuario:204; GET reseña:404; película sigue disponible | DELETE usuario:204; GET reseña:404; GET película:200. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T24 | Crear otra pareja temporal con reseña; eliminar película y consultar reseña | DELETE película:204; GET reseña:404; usuario sigue disponible | DELETE película:204; GET reseña:404; GET usuario:200. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T25 | CRUD final de un género temporal sin películas: POST, listar, GET, PUT, DELETE, GET | 201,200,200,200,204 sin cuerpo,404; verifica ciclo completo | Ciclo completo 201,200,200,200,204 y404; género listado y modificación confirmada. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T26 | GET /peliculas/ID_ELIMINADO/resenas | 404 RESOURCE_NOT_FOUND para película inexistente | GET reseñas de película eliminada:404 RESOURCE_NOT_FOUND. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |
| T27 | Ejecutar unittest | Siete pruebas aprobadas, incluido contrato de 21 operaciones | Siete tests aprobados; contrato registrado de 21 operaciones confirmado. [Detalle](resultados/20261102T050815Z/ejecucion.md). | Aprobado |

## Reinicio de PostgreSQL sin perder el aislamiento

Detener la API de pruebas. En otra terminal, desde el proyecto dueño del contenedor, ejecutar `docker compose restart db`, y después `docker compose ps` hasta que esté healthy. Volver a la terminal de pruebas, confirmar que DB_NAME sigue apuntando a la base de pruebas y arrancar la API en 8001. No ejecutar down -v, downgrade base ni eliminar el volumen.

## Formato de evidencia por caso

Para cada caso completado, agregar una sección con:

- Caso, responsable y fecha.
- Commit probado y precondiciones.
- Método, URL y cuerpo enviado, sin contraseñas.
- Código HTTP y cuerpo realmente recibidos.
- Comparación con el esperado y conclusión (aprobado/fallido).
- Archivo de respuesta o captura, si se utiliza.

Para CRUD o casos con varias solicitudes, conservar los resultados de todas las operaciones. Para errores controlados comprobar `error.code`, `error.message` y `error.details`, además del estado HTTP. Para 204 confirmar cuerpo vacío.

## Restablecimiento y límites

Para repetir desde cero, crear otra base exclusiva con nombre nuevo y repetir migración y seeders. Esto no requiere cambiar código ni borrar los datos anteriores. Los casos destructivos usan exclusivamente registros temporales propios. La limpieza de las bases de pruebas se realizará por separado, después de verificar sus nombres y cuando el equipo ya no necesite sus datos.

Las siete pruebas existentes usan principalmente rutas y servicios de Géneros con SQLite, además de comprobar el contrato registrado. No son pruebas HTTP de extremo a extremo ni demuestran por sí solas las reglas de Reseñas, la carga PostgreSQL o un reinicio real. T01–T26 completan esas comprobaciones manuales.

Al terminar, detener la API y cerrar la terminal de pruebas. Si se reutiliza esa terminal para la base de trabajo, eliminar la variable temporal con `Remove-Item Env:DB_NAME` y comprobar de nuevo el destino antes de ejecutar comandos.

### T01 — Migración desde cero

- Responsable: Vicente Fonseca.
- Base: backend04_pruebas_finales_01.
- Commit: 04576bee5ac560bd2d772150d6070e294666e76e.
- Obtenido: se aplicó la migración inicial 0001 sin errores.
  `alembic current` devolvió `0001 (head)` y `alembic check`
  devolvió `No new upgrade operations detected.`
- Estado: Aprobado.

### T02 — Verificación de reseñas iniciales

- Responsable: Vicente Fonseca.
- Base: backend04_pruebas_finales_01.
- Commit: 04576bee5ac560bd2d772150d6070e294666e76e.

**Solicitud:**

GET http://127.0.0.1:8001/resenas?pagina=1&limite=100

**Resultado esperado:**

Respuesta 200 con diez reseñas iniciales, referencias válidas,
puntuaciones entre 1 y 10 y metadatos de paginación correctos.

**Resultado obtenido:**

La API respondió HTTP 200 OK con diez reseñas y estos metadatos:

- total: 10.
- pagina: 1.
- limite: 100.
- total_paginas: 1.

Las reseñas tienen identificadores del 1 al 10. La película 2
tiene cinco reseñas y la película 4 tiene otras cinco, demostrando
la relación uno-a-muchos entre películas y reseñas.

Los usuarios relacionados tienen IDs del 1 al 5. Se comprobó
mediante GET /usuarios que existen y están activos.

Se comprobó mediante GET /peliculas que las películas 2 y 4
existen y tienen años de estreno 2021 y 2020, respectivamente.

Las puntuaciones están entre 6 y 10. No se repite ninguna
combinación de usuario y película.

La primera ejecución del comando de carga informó
“Reseñas iniciales cargadas.” La segunda informó
“Carga de reseñas omitida: la tabla ya contiene registros.”

**Estado: Aprobado.**

**Alcance:**

Esta comprobación valida los datos iniciales consultados.
El rechazo de reseñas duplicadas, usuarios inactivos y películas
futuras se verifica en casos separados.

### T03 — Crear, listar y consultar género

- POST /generos: 201 Created; género creado con ID 6,
  nombre QA Genero 20261102a y activo=true.
- GET /generos: 200; incluye el género creado.
- GET /generos/6: 200; devuelve los mismos datos.
- Estado: Aprobado.

## Ejecución asistida completada — 2 de noviembre de 2026

- Autorización: Vicente autorizó ejecutar y documentar las pruebas sobre `backend04_pruebas_finales_01`.
- Se utilizó una API temporal en 8002 con DB_NAME explícito para garantizar el destino; no se cambió .env ni código de aplicación.
- Se ejecutaron las 80 solicitudes de pruebas.http con una etiqueta QA nueva para evitar repetir las creaciones manuales. Todas devolvieron los códigos esperados. Se verificaron adicionalmente contenido, identidad, orden, filtro, totales, errores uniformes y cuerpos vacíos 204 según cada caso.
- Las creaciones QA y las eliminaciones de los casos se limitaron a la base de pruebas. Los datos de trabajo no se borraron. Se conservaron registros QA para revisión; los casos de eliminación y cascadas sí eliminaron sus recursos temporales previstos.
- La primera pasada se interrumpió al reiniciar la API temporal y continuó desde la solicitud siguiente, sin repetir sus creaciones. Los registros de ambos tramos se conservan.
- El intento de reiniciar PostgreSQL mediante Docker CLI fue rechazado por permisos del entorno. No se considera un fallo del backend ni una prueba de reinicio aprobada. Se completó después desde Docker Desktop mediante Restart del proyecto `backend-2026-grupo-04`, conservando el volumen, y se comprobó el cambio real de inicio de PostgreSQL y la igualdad íntegra de una reseña modificada antes y después.
- La carga desde cero T01/T02 se respalda con las salidas reales aportadas por Vicente y las consultas iniciales revisadas. La ejecución automática partió de esa misma base ya poblada: no representa una segunda creación de esquema desde cero. Se repitieron la revisión Alembic y dos cargas sin cambios de cantidades.
- Las siete pruebas unitarias/de integración existentes aprobaron. Su alcance sigue siendo principalmente Géneros y el registro OpenAPI; los resultados HTTP de esta ejecución complementan ese alcance.
- Alcance de aprobación: estos datos y casos concretos. No se afirma cobertura exhaustiva, pruebas de carga, concurrencia ni autenticación.

### Archivos de respaldo

- [Solicitudes, respuestas y comandos completos](resultados/20261102T050815Z/ejecucion.md).
- [Resultados estructurados](resultados/20261102T050815Z/resultados.json).
- [Prueba adicional de persistencia PostgreSQL](resultados/20261102T050815Z/persistencia_adicional.json).
- [Primer tramo de la ejecución](resultados/20261102T050715Z/ejecucion.md).

No se creó commit ni se publicaron estos archivos automáticamente.

## Observación adicional T28 — Reconexión con API abierta (fallida)

Esta comprobación amplía T21: se reinició solo PostgreSQL mientras la API temporal seguía abierta. La primera consulta a la reseña 14 devolvió HTTP 500 por `psycopg2.OperationalError: could not receive data from server: Software caused connection abort`. El reintento devolvió 200, con la modificación íntegra. Después de reiniciar también la API, la primera consulta devolvió 200 y conservó ID, referencias, puntuación, comentario y fecha.

Conclusión: la persistencia y el procedimiento planificado de reiniciar base y API aprobaron. La recuperación transparente de una conexión del pool caducada no aprobó en esta comprobación adicional. Debe revisarse la configuración del engine (por ejemplo, validación de conexiones al recuperarlas) en una corrección separada y repetirse este escenario. No se modificó código para ocultar el fallo.

Los detalles y los estados de ambos intentos están en `persistencia_adicional.json`. Los registros de prueba se conservan para revisión. La API temporal de esta ejecución se detuvo al terminar; Docker y el volumen permanecen disponibles.
