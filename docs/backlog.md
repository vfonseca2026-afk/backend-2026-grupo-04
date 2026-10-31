# Backlog del grupo 04

## Organización del trabajo

Cada integrante trabaja en una rama principal y publica sus avances mediante
commits significativos y push.

No se exige un commit por archivo ni un PR por tarea o hito.
El acuerdo es abrir un PR por integrante cuando su trabajo esté listo para
integrarse, con revisión de otro compañero. Se podrán abrir PR adicionales
si una dependencia lo requiere.

Cada integrante debe completar durante el proyecto:
- Al menos cinco commits propios y significativos.
- Trabajo en una rama distinta de main.
- Al menos un pull request.

## Ramas y responsables

| Integrante | Rama | Responsabilidad principal |
|---|---|---|
| Vicente Fonseca | `feature/integracion-documentacion` | Coordinación, Géneros, documentación e integración |
| Matías Manquelaf | `feature/usuarios` | Usuarios, dominio y datos |
| Miguel Torres | `feature/peliculas` | Películas, API y consultas |
| Danna Ramirez | `feature/resenas` | Reseñas, reglas de negocio y calidad |

Las responsabilidades no son exclusivas: todos implementan, comprueban
funcionalidades y participan en la integración y defensa.

## Base inicial disponible

Estos componentes ya estaban implementados antes de los avances posteriores:

- Arquitectura de cuatro capas y recorrido completo de Géneros.
- Cuatro entidades de dominio y cuatro modelos ORM.
- Migración inicial de las cuatro tablas y sus relaciones.
- Conexión a PostgreSQL y configuración Docker Compose.
- CRUD, servicio, repositorio, mapper y DTO iniciales de Géneros.
- Manejo central de errores uniformes.
- Seeder de Géneros.
- DTO comunes de paginación.
- Pruebas locales y plantillas de pruebas manuales.

La existencia de archivos con instrucciones TODO no significa que la
funcionalidad esté implementada.

## Vicente Fonseca

Rama: `feature/integracion-documentacion`

### Avances realizados

- [x] Publicar la base inicial del proyecto.
- [x] Completar ejemplos y descripciones OpenAPI de Géneros.
- [x] Exigir descripcion y activo en el DTO de actualización de Géneros.
- [x] Actualizar el README con el contrato y la organización del equipo.

### Pendientes

- [x] Actualizar este backlog y comprobar su coherencia con el README.
- [x] Confirmar acceso de integrantes y docente al repositorio.
- [x] Verificar protección de main contra pushes directos.
- [x] Completar ejemplos específicos de errores en OpenAPI.
- [ ] Revisar el contrato de las funcionalidades al integrarlas.
- [ ] Verificar diagramas contra la implementación final.
- [ ] Comprobar instalación y ejecución desde una copia limpia.
- [ ] Consolidar README final y recorrido de una solicitud.
- [ ] Coordinar revisión e integración de los PR.
- [ ] Preparar presentación y coordinar ensayos de defensa.

## Matías Manquelaf

Rama: `feature/usuarios`

Los avances actuales de esta rama deben confirmarse con Matías.
Marcar las tareas conforme se comprueben, sin repetir trabajo ya realizado.

- [ ] Implementar mapper y repositorio de Usuarios.
- [ ] Publicar obtener_por_id para su uso en Reseñas.
- [ ] Implementar DTO de creación, actualización y respuesta.
- [ ] Validar formato de correo, longitudes y campos adicionales.
- [ ] Implementar servicio y comprobación de correo y nombre únicos.
- [ ] Permitir actualizar conservando los valores del propio usuario.
- [ ] Implementar cinco endpoints de Usuarios.
- [ ] Implementar listado paginado y sus metadatos.
- [ ] Integrar dependencias y router de Usuarios.
- [ ] Documentar operaciones y respuestas en OpenAPI.
- [ ] Implementar seeder con usuarios activos e inactivos.
- [ ] Coordinar el orden de carga inicial con los demás responsables.
- [ ] Revisar coherencia entre modelos ORM, diagramas y migraciones.
- [ ] Comprobar funcionamiento y persistencia de Usuarios.

## Miguel Torres

Rama: `feature/peliculas`

Los avances actuales de esta rama deben confirmarse con Miguel.

- [ ] Implementar mapper y repositorio de Películas.
- [ ] Publicar obtener_por_id para su uso en Reseñas.
- [ ] Implementar DTO de creación, actualización y respuesta.
- [ ] Validar título, duración, año, clasificación y demás campos.
- [ ] Implementar servicio y existencia del género relacionado.
- [ ] Implementar cinco endpoints de Películas.
- [ ] Integrar dependencias y router de Películas.
- [ ] Implementar DTO de consulta.
- [ ] Combinar filtro, orden y paginación en GET /peliculas.
- [ ] Calcular total y total_paginas sobre los registros filtrados.
- [ ] Usar columnas de orden permitidas y orden estable.
- [ ] Documentar operaciones y respuestas en OpenAPI.
- [ ] Implementar seeder con varias películas por género y una futura.
- [ ] Comprobar funcionamiento y persistencia de Películas.

## Danna Ramirez

Rama: `feature/resenas`

Los avances actuales de esta rama deben confirmarse con Danna.

- [ ] Implementar DTO de creación, actualización y respuesta.
- [ ] Validar puntuación, longitudes, IDs y campos adicionales.
- [ ] Impedir cambiar usuario y película mediante el DTO de actualización.
- [ ] Implementar mapper y repositorio de Reseñas.
- [ ] Implementar servicio y comprobación de referencias existentes.
- [ ] Rechazar reseñas de usuarios inactivos.
- [ ] Rechazar reseñas de películas con año posterior al actual.
- [ ] Rechazar reseñas duplicadas del mismo usuario y película.
- [ ] Implementar cinco endpoints de Reseñas.
- [ ] Implementar GET /peliculas/{pelicula_id}/resenas.
- [ ] Implementar paginación de las colecciones previstas.
- [ ] Integrar dependencias y router de Reseñas.
- [ ] Documentar operaciones y respuestas en OpenAPI.
- [ ] Implementar seeder con relaciones coherentes.
- [ ] Comprobar funcionamiento y persistencia de Reseñas.
- [ ] Coordinar las pruebas finales y sus evidencias con todo el equipo.

## Dependencias e integración

Reseñas necesita consultar Usuarios y Películas mediante:

- UsuarioRepository.obtener_por_id(usuario_id)
- PeliculaRepository.obtener_por_id(pelicula_id)

Ambos métodos devolverán una entidad de dominio o None si no existe.

Orden de integración recomendado:
1. Usuarios.
2. Películas.
3. Reseñas.

Vicente coordinará su PR de Géneros y documentación para evitar conflictos
con los archivos compartidos.

Antes de integrar cada PR:
- Guardar y publicar los cambios de su rama.
- Actualizar referencias con git fetch origin.
- Incorporar origin/main mediante merge en su rama.
- Resolver conflictos y comprobar el funcionamiento.
- Solicitar revisión a otro integrante.

Los archivos main.py, dependencies.py y app/seed.py requieren coordinación.
Los bloques separados no garantizan ausencia de conflictos.

## Migraciones y carga inicial

- La migración inicial ya define las cuatro tablas.
- Los cambios de esquema requieren una migración versionada.
- Cada responsable implementa el seeder de su entidad.
- Matías coordina la revisión del esquema y el orden de ejecución.
- Orden de carga: Géneros, Usuarios, Películas y Reseñas.
- La entrega requiere al menos dos registros por entidad y una relación
  uno-a-muchos demostrable.
- Los seeders deben usar referencias recuperadas de la base, sin asumir IDs fijos.

## Pruebas y evidencias

Durante los hitos se comprueba el funcionamiento de cada avance.

Por acuerdo del equipo, el registro formal de evidencias se completará
cuando las funcionalidades estén terminadas.

En ese momento:
- [ ] Completar tests_manual/pruebas.http.
- [ ] Registrar entrada, esperado y obtenido en tests_manual/evidencias.md.
- [ ] Cubrir CRUD, datos inválidos, recurso inexistente y regla de negocio.
- [ ] Comprobar filtro, orden y paginación en una misma consulta.
- [ ] Comprobar persistencia tras reiniciar, conservando el volumen.
- [ ] Documentar cómo aislar o restablecer los datos de prueba.

Cada integrante ejecutará y aportará resultados de su funcionalidad.
Danna coordinará su consolidación.

## Defensa

- [ ] Preparar un máximo de 15 diapositivas.
- [ ] Ensayar una presentación y demostración de 10 minutos.
- [ ] Preparar respuestas para los 5 minutos de preguntas.
- [ ] Demostrar cuatro endpoints distintos según la rúbrica.
- [ ] Demostrar migraciones, seeders y persistencia tras reinicio.
- [ ] Todos deben poder realizar la presentación completa.
- [ ] Todos deben explicar el recorrido entre capas de cualquier entidad.