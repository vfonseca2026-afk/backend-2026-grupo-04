mejor git status







23:45






Sí, git status también te muestra la rama actual y además los archivos modificados. Usa ese 👍
git status

    
23:45







# Backlog del grupo 04 Actualizado al cierre documental de la auditoría del 2 d…

algo de ahi?







23:46






Ha trabajado durante 18s



Sí, ahí hay texto de auditoría que puedes simplificar. Conserva las responsabilidades y las listas de tareas; sirven como historial del equipo.

Cambiaría estas partes:
- Inicio: elimina la referencia al commit, al “cierre documental” y a que se guardará en otro commit. Basta con Actualizado el 3 de noviembre de 2026.
- Referencias al “RAR auditado” o a la “ejecución asistida”: reemplázalas por referencias directas al repositorio y las evidencias.
- Conteo de commits: puedes quitar esa tabla; queda desactualizada cada vez que trabajan.
- Último párrafo de controles GitHub: elimínalo. Dice “comprobaciones no acreditadas”, pero todas sus casillas están marcadas, así que se contradice.
Ojo con las casillas [x]: presentación, ensayos, acceso del docente, aprobaciones y protección de main deben estar marcados solo si realmente los comprobaron. Haber terminado el código no confirma esas tareas.

La incidencia T28 conviene conservarla mientras siga sin corregirse.

    
23:46







dame el readme







23:47






osea el backlog actualizado







23:47






Ha trabajado durante 16s






Copia esto en el archivo del backlog. Dejé por confirmar los ensayos y controles de GitHub que deben comprobar ustedes.
# Backlog del grupo 04

Actualizado el 3 de noviembre de 2026.

## Estados

- [x] Completado y respaldado por código o evidencias.
- [ ] Pendiente de realizar o confirmar.

## Responsabilidades

| Integrante | Rama | Responsabilidad |
|---|---|---|
| Vicente Fonseca | `feature/integracion-documentacion` | Géneros, integración y documentación |
| Matías Manquelaf | `feature/usuarios` | Usuarios y sus datos iniciales |
| Miguel Torres | `feature/peliculas` | Películas y consulta combinada |
| Danna Ramirez | `feature/resenas` | Reseñas y reglas de publicación |

Todos deben conocer el proyecto completo y poder explicar sus recorridos entre capas.

## Base del proyecto

- [x] Definir la problemática, los actores y el alcance.
- [x] Modelar Géneros, Usuarios, Películas y Reseñas.
- [x] Organizar el código en presentación, aplicación, dominio e infraestructura.
- [x] Configurar PostgreSQL con Docker.
- [x] Crear los modelos ORM, relaciones y restricciones.
- [x] Preparar la migración inicial con Alembic.
- [x] Implementar sesiones por solicitud y errores uniformes.
- [x] Integrar las cuatro entidades.
- [x] Registrar las 21 operaciones en OpenAPI.
- [x] Separar la carga inicial del arranque de la API.

## Géneros — Vicente

- [x] Implementar el CRUD y su recorrido persistente.
- [x] Validar los datos y controlar nombres duplicados.
- [x] Impedir la eliminación de géneros con películas asociadas.
- [x] Documentar las operaciones y sus ejemplos.
- [x] Preparar el seeder de cinco géneros.
- [x] Integrar los avances del equipo mediante PR.
- [x] Preparar solicitudes y evidencias de pruebas.

## Usuarios — Matías

- [x] Implementar el mapper entre entidad y modelo ORM.
- [x] Implementar el repositorio con CRUD, consultas y conteo.
- [x] Publicar obtener_por_id para su uso desde Reseñas.
- [x] Definir DTO de creación, actualización y respuesta.
- [x] Validar nombre, formato de correo y campos adicionales.
- [x] Controlar duplicados y usuarios inexistentes.
- [x] Conservar ID y fecha de registro al actualizar.
- [x] Implementar cinco endpoints y listado paginado.
- [x] Integrar dependencias y registrar el router.
- [x] Preparar el seeder de seis usuarios, incluido uno inactivo.
- [x] Comprobar la carga desde una base vacía y su repetición.
- [x] Completar los ejemplos de respuestas exitosas en OpenAPI.

## Películas — Miguel

- [x] Implementar mapper y repositorio.
- [x] Definir DTO de creación, actualización, respuesta y consulta.
- [x] Validar los datos y comprobar que el género exista.
- [x] Implementar servicio, dependencias y cinco endpoints.
- [x] Combinar filtros, ordenamiento y paginación en un mismo GET.
- [x] Calcular los totales antes de paginar.
- [x] Incorporar un desempate estable en el ordenamiento.
- [x] Documentar las operaciones y sus ejemplos.
- [x] Preparar diez películas de ejemplo, incluida una futura.
- [x] Recuperar los IDs reales de los géneros durante la carga.

## Reseñas — Danna

- [x] Implementar mapper y repositorio.
- [x] Definir DTO de creación, actualización y respuesta.
- [x] Validar puntuación, título, comentario y referencias.
- [x] Comprobar que el usuario y la película existan.
- [x] Impedir reseñas duplicadas por usuario y película.
- [x] Impedir que usuarios inactivos publiquen o editen reseñas.
- [x] Impedir reseñas de películas con año de estreno futuro.
- [x] Conservar autor, película, ID y fecha al actualizar.
- [x] Implementar CRUD y consulta paginada por película.
- [x] Integrar dependencias y registrar las rutas.
- [x] Preparar el seeder de diez reseñas.
- [x] Actualizar la comprobación del contrato a 21 operaciones.

## Base de datos y carga inicial

- [x] Aplicar la migración inicial en PostgreSQL.
- [x] Comprobar las cuatro tablas y sus relaciones.
- [x] Integrar los seeders en el orden Géneros → Usuarios → Películas → Reseñas.
- [x] Ejecutar la carga explícita con `uv run python -m app.seed`.
- [x] Omitir la carga de tablas que ya contienen registros.
- [x] Comprobar que los datos relacionados usan IDs existentes.

La carga inicial solo se ejecuta si la tabla correspondiente está vacía.
No completa cargas parciales ni se ejecuta al iniciar la API.

## Pruebas y evidencias

- [x] Preparar solicitudes en `tests_manual/pruebas.http`.
- [x] Registrar una matriz de 27 casos.
- [x] Guardar resultados de 80 solicitudes HTTP.
- [x] Comprobar CRUD, datos inválidos, inexistencia y duplicados.
- [x] Comprobar las reglas de publicación de reseñas.
- [x] Comprobar la eliminación de géneros con películas asociadas.
- [x] Comprobar filtros, ordenamiento y paginación combinados.
- [x] Comprobar páginas posteriores y consultas sin coincidencias.
- [x] Comprobar eliminación en cascada por usuario y película.
- [x] Comprobar persistencia tras reiniciar la API.
- [x] Comprobar conservación de datos tras reiniciar PostgreSQL.
- [x] Ejecutar las siete pruebas automatizadas existentes.
- [ ] Confirmar que la tabla auxiliar de IDs QA coincide con los resultados guardados.

Las 80 solicitudes HTTP no equivalen a 80 pruebas unitarias.
Las siete pruebas automatizadas utilizan SQLite temporal y comprueban
principalmente el recorrido de Géneros y aspectos del contrato.
Las evidencias HTTP complementan ese alcance.

## Documentación y entrega

- [x] Documentar las operaciones en OpenAPI y Swagger UI.
- [x] Registrar resultados y limitaciones conocidas.