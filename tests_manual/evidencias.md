# Evidencias de pruebas — Grupo 04

Estado: planificación de pruebas. Ningún resultado esperado de este documento constituye una evidencia obtenida.

## Entorno y versión

Completar antes de ejecutar:

| Dato | Valor |
|---|---|
| Fecha y responsable | Pendiente |
| Rama y commit (`git branch --show-current`, `git rev-parse HEAD`) | Pendiente |
| Base exclusiva de pruebas | Pendiente |
| Puerto de la API | 8001 |
| Revisión aplicada (`uv run alembic current`) | Pendiente |
| Resultado de `uv run alembic check` | Pendiente |

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
| T01 | Migración sobre base nueva; current; check | Se aplica 0001, current indica head y check no detecta operaciones | Pendiente | P |
| T02 | Carga inicial dos veces; consultar cuatro colecciones | Datos coherentes, mínimo dos por entidad; segunda ejecución no duplica | Pendiente | P |
| T03 | POST del género QA; GET colección e individual | 201 con ID; 200 e inclusión en listado | Pendiente | P |
| T04 | PUT género QA con nombre, descripción y activo | 200; se conservan ID y fecha; los nuevos datos se recuperan por GET | Pendiente | P |
| T05 | POST género con nombre `A`; PUT sin activo; GET /generos/0 | 422 VALIDATION_ERROR en cada solicitud; details identifica el campo | Pendiente | P |
| T06 | POST del nombre QA existente cambiando mayúsculas | 409 RESOURCE_CONFLICT; no agrega género | Pendiente | P |
| T07 | POST/GET/PUT usuario QA; conservar su correo al actualizar; listado pagina=1&limite=1 | 201/200; actualización propia permitida; metadatos coherentes | Pendiente | P |
| T08 | POST usuario con correo inválido; otro con correo QA existente y nombre distinto | 422 y 409 respectivamente; estructura uniforme | Pendiente | P |
| T09 | Crear tres películas QA; GET y PUT QA Gamma con todos los campos | 201/200; cambios persistidos e ID conservado; mantener duración 100 y año 2021 | Pendiente | P |
| T10 | POST película con genero_id de un género temporal creado y eliminado previamente | 404 RESOURCE_NOT_FOUND; no crea película | Pendiente | P |
| T11 | POST película con duración 0 o clasificación no permitida | 422 VALIDATION_ERROR | Pendiente | P |
| T12 | GET /peliculas?genero_id=ID_QA&ordenar_por=duracion_min&direccion=desc&pagina=1&limite=2 | 200; duraciones [120,100]; total=3; pagina=1; limite=2; total_paginas=2 | Pendiente | P |
| T13 | Misma consulta con pagina=2; repetir con pagina=3 | Página 2: [80]; página 3: items=[]; ambas conservan total=3 y total_paginas=2 | Pendiente | P |
| T14 | Filtro QA y titulo=texto_sin_coincidencias; consulta con pagina=0, limite=101 o direccion=arriba | Sin coincidencias: 200,total=0,total_paginas=0; parámetros inválidos: 422 | Pendiente | P |
| T15 | DELETE género QA mientras mantiene películas | 409 RESOURCE_CONFLICT; género y películas siguen disponibles | Pendiente | P |
| T16 | POST reseña QA válida; GET individual, general y por película | 201 con fecha; 200; incluida en ambas colecciones | Pendiente | P |
| T17 | Repetir POST del usuario y película de T16 | 409 RESOURCE_CONFLICT; conserva una reseña para la pareja | Pendiente | P |
| T18 | POST con usuario inactivo y película estrenada; POST con usuario activo y película futura | 400 BUSINESS_RULE_VIOLATION en ambos casos | Pendiente | P |
| T19 | POST reseña con puntuación 11 o comentario corto; PUT incluyendo usuario_id | 422 VALIDATION_ERROR | Pendiente | P |
| T20 | PUT reseña QA con puntuación 9, título y comentario válidos | 200; conserva ID, usuario, película y fecha | Pendiente | P |
| T21 | Actualizar dato QA; detener/reiniciar API; GET; detener API, reiniciar db conservando volumen, esperar healthy, iniciar API con misma base y consultar | El dato modificado y sus referencias se conservan en ambos reinicios | Pendiente | P |
| T22 | Crear reseña temporal independiente; DELETE y GET del mismo ID | 204 sin cuerpo; luego 404 RESOURCE_NOT_FOUND | Pendiente | P |
| T23 | Crear usuario y película temporales con reseña; eliminar usuario y consultar reseña | DELETE usuario:204; GET reseña:404; película sigue disponible | Pendiente | P |
| T24 | Crear otra pareja temporal con reseña; eliminar película y consultar reseña | DELETE película:204; GET reseña:404; usuario sigue disponible | Pendiente | P |
| T25 | CRUD final de un género temporal sin películas: POST, listar, GET, PUT, DELETE, GET | 201,200,200,200,204 sin cuerpo,404; verifica ciclo completo | Pendiente | P |
| T26 | GET /peliculas/ID_ELIMINADO/resenas | 404 RESOURCE_NOT_FOUND para película inexistente | Pendiente | P |
| T27 | Ejecutar unittest | Siete pruebas aprobadas, incluido contrato de 21 operaciones | Pendiente | P |

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