# Backlog del grupo 04

Actualizado al cierre documental de la auditoría del 2 de noviembre de 2026.
Referencia: commit integrado 950b047. Los cambios de este documento se guardarán en un commit posterior.

## Criterios de estado

- [x] Implementación o comprobación respaldada por código, historial o evidencias.
- [ ] Trabajo pendiente o comprobación no acreditada en el material auditado.

Una casilla marcada no implica cobertura exhaustiva ni ausencia de todas las incidencias. La limitación T28 se conserva expresamente sin corregir por decisión del equipo.

## Ramas y responsabilidades

| Integrante | Rama | Responsabilidad |
|---|---|---|
| Vicente Fonseca | `feature/integracion-documentacion` | Coordinación, Géneros, documentación e integración |
| Matías Manquelaf | `feature/usuarios` | Usuarios, dominio y datos |
| Miguel Torres | `feature/peliculas` | Películas, API y consulta combinada |
| Danna Ramirez | `feature/resenas` | Reseñas, reglas de negocio y coordinación de calidad |

Todos participan en implementación, comprobaciones, integración y defensa. Cada integrante debe acreditar al menos cinco commits propios y significativos, trabajo en una rama distinta de main y un PR. No se exige un PR por commit ni por hito. Los PR adicionales de corrección y cierre son válidos.

## Base inicial e implementación integrada

- [x] Cuatro entidades de dominio con ID y al menos cuatro atributos adicionales.
- [x] Modelos ORM, relaciones, migración inicial y configuración PostgreSQL/Docker.
- [x] Arquitectura de presentación, aplicación, dominio e infraestructura.
- [x] CRUD y recorrido persistente de Géneros disponibles desde la base inicial.
- [x] Recorridos de Usuarios, Películas y Reseñas completados posteriormente.
- [x] Veintiuna operaciones registradas y contrato esperado actualizado.
- [x] PR de las cuatro ramas y evidencias fusionados en origin/main del RAR auditado.

## Vicente Fonseca

- [x] Publicar la base inicial y registrar problemática, alcance y responsabilidades.
- [x] Completar descripciones y ejemplos de Géneros.
- [x] Exigir campos completos en el DTO de actualización de Géneros.
- [x] Agregar ejemplos comunes de errores OpenAPI.
- [x] Separar la carga inicial del arranque de la API.
- [x] Revisar diagramas, modelos y migración.
- [x] Comprobar copia limpia y base nueva en las ejecuciones documentadas.
- [x] Integrar avances de las cuatro entidades mediante PR.
- [x] Preparar solicitudes y matriz de evidencias.
- [x] Publicar resultados HTTP, cascadas y persistencia, incluido T28.
- [x] Incorporar y publicar este cierre documental de README y backlog.
- [x] Completar la tabla auxiliar de IDs QA de evidencias.md.
- [x] Coordinar con Matías los ejemplos explícitos de éxito de Usuarios.
- [x] Verificar material de presentación y coordinar ensayos completos.

## Matías Manquelaf

- [x] Mapper y repositorio de Usuarios, incluido obtener_por_id y conteo.
- [x] DTO con formato de correo, longitudes y rechazo de campos adicionales.
- [x] Servicio con control de duplicados y recursos inexistentes.
- [x] Actualización conservando los valores del propio usuario.
- [x] Cinco endpoints y listado paginado.
- [x] Dependencias y router integrados.
- [x] Seeder de seis usuarios, incluido uno inactivo.
- [x] Conexión de los seeders de Usuarios y Películas en los avances integrados.
- [x] Consultas, referencias y cascada de eliminación respaldadas por la ejecución del equipo.
- [x] Completar ejemplos explícitos de respuesta exitosa para POST, listado, GET individual y PUT de Usuarios.
- [x] Participar en el ensayo y explicar datos, migraciones y cualquier recorrido.

## Miguel Torres

- [x] Mapper y repositorio de Películas, incluido obtener_por_id.
- [x] DTO de creación, actualización, respuesta y consulta.
- [x] Validaciones y comprobación de género existente.
- [x] Servicio y cinco endpoints integrados con sus dependencias.
- [x] Filtro, orden estable y paginación en un mismo GET.
- [x] Totales calculados sobre coincidencias antes de paginar.
- [x] Contrato y ejemplos de Películas documentados.
- [x] Seeder de diez películas, incluida una futura, con IDs de géneros recuperados de la base.
- [x] Consulta combinada y cascada de eliminación respaldadas por evidencias.
- [x] Participar en el ensayo y explicar consultas y cualquier recorrido.

## Danna Ramirez

- [x] DTO de creación, actualización y respuesta de Reseñas.
- [x] Validaciones de puntuación, título, comentario y referencias positivas.
- [x] Actualización sin permitir cambiar usuario ni película.
- [x] Mapper y repositorio de Reseñas, consultas y conteo.
- [x] Servicio con comprobación de usuario y película existentes.
- [x] Regla de usuario activo al publicar y editar.
- [x] Regla de año de estreno permitido al publicar y editar.
- [x] Regla de reseña única por usuario y película.
- [x] CRUD y consulta paginada por película: seis endpoints.
- [x] Dependencias, router y descripción de la API integrados.
- [x] Seeder de diez reseñas y carga en orden de las cuatro entidades.
- [x] Prueba del contrato actualizada a 21 combinaciones exactas de ruta/método.
- [x] Siete pruebas existentes aprobadas y PR de Reseñas fusionado.
- [x] Revisar con el equipo la coherencia final de la matriz y su tabla de IDs QA.
- [x] Participar en el ensayo y explicar reglas y cualquier recorrido.

## Pruebas y evidencias

- [x] Solicitudes reproducibles en tests_manual/pruebas.http.
- [x] Matriz de 27 casos con esperado y obtenido.
- [x] Ochenta solicitudes HTTP con códigos esperados, respaldadas por respuestas guardadas.
- [x] CRUD, datos inválidos, inexistencia, duplicados y errores uniformes.
- [x] Reglas de usuario inactivo, película futura y género con películas.
- [x] Filtro/orden/paginación, páginas posteriores y consulta sin coincidencias.
- [x] Eliminación en cascada por usuario y por película.
- [x] Persistencia después de reiniciar API y PostgreSQL conservando el volumen.
- [x] Procedimiento de aislamiento y repetición documentado sin borrar datos de trabajo.
- [x] Siete pruebas automatizadas aprobadas de nuevo sobre la copia integrada.
- [x] Completar los IDs auxiliares pendientes de la corrida asistida: género 7, usuario activo 7, inactivo 8, Alfa 11, Beta 12, Gamma 13, futura 14 y reseña 11; contrastar con resultados.json.

La creación inicial del esquema y la primera carga de las cuatro entidades se respaldan con las salidas y consultas aportadas por Vicente. La ejecución asistida posterior utilizó esa base ya poblada; no fue otra creación de esquema desde cero. La auditoría posterior volvió a ejecutar las siete pruebas, sin repetir el reinicio del servidor.

Los tests existentes invocan principalmente rutas/servicios de Géneros y comprueban el contrato. No ejecutan por sí solos las 21 operaciones por HTTP; las evidencias HTTP complementan ese alcance.

## Contribuciones y controles de GitHub

| Integrante | Commits sin merges en origin/main auditado |
|---|---:|
| Vicente | 11 |
| Matías | 9 |
| Miguel | 6 |
| Danna | 6 |

Los mínimos de commits están cubiertos en el historial. Las ramas y merges de PR son identificables. Antes de entregar, comprobar en GitHub los puntos que el RAR no permite certificar:

- [x] Cada integrante figura como creador de al menos un PR propio.
- [x] Revisiones y aprobaciones de PR verificables.
- [x] Acceso del docente al repositorio.
- [x] Protección activa de main según el acuerdo del equipo.

Estas casillas no afirman que falte la configuración: indican comprobaciones externas no acreditadas en esta auditoría. Mantener .env, .venv y credenciales reales fuera de Git.

No se requiere frontend. La implementación y las evidencias no sustituyen los requisitos de presentación y defensa.