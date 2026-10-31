# Backlog del equipo (copiar a GitHub Issues / Projects)

Regla: **una tarea = una rama = un pull request**, revisado por otra persona.
Cada PR debe tener varios commits pequeños con mensajes que digan la acción realizada.
Orden de integración recomendado para no bloquearse: primero `mapper + repositorio` de
Usuario y Película (Reseña los necesita), luego servicio/DTO, luego router.

## Vicente Fonseca — Coordinación + Documentación e integración
| Rama | Tarea |
|---|---|
| `chore/base-inicial` | Subir la base inicial mediante PR si el repositorio ya existe; activar y verificar protección de main |
| `docs/roles-y-backlog` | Registrar roles en el README y crear los issues de este backlog |
| `docs/openapi-ejemplos` | Revisar que cada endpoint tenga resumen, descripción, ejemplos y códigos (tags con descripción en `main.py`) |
| `docs/readme-final` | Marcar ⏳ → ✅, completar capturas y recorrido de una solicitud con una película real |
| `docs/diagramas` | Verificar diagramas de clases y de datos contra la implementación final |
| (revisión) | Revisar y fusionar los PR de los demás; ensayar la defensa desde una copia limpia |

## Matías Manquelaf — Dominio y datos
| Rama | Tarea |
|---|---|
| `feature/usuarios-mapper-repo` | `usuario_mapper.py` + `usuario_repository.py` (publicar `obtener_por_id` cuanto antes) |
| `feature/usuarios-servicio-dto` | `usuario_service.py` (email y nombre únicos) + `usuario_dto.py` (EmailStr) |
| `feature/usuarios-router` | `usuario_router.py` (5 endpoints) + registrar en `main.py` y `dependencies.py` |
| `feature/seeders-iniciales` | `usuario_seeder.py` y conectar todos los seeders en `app/seed.py` |
| `feature/revision-modelo-datos` | Revisar modelos ORM y migración contra los diagramas (`uv run alembic check`) |

## Miguel Torres — API y lógica de negocio
| Rama | Tarea |
|---|---|
| `feature/peliculas-mapper-repo` | `pelicula_mapper.py` + `pelicula_repository.py` (publicar `obtener_por_id` cuanto antes) |
| `feature/peliculas-servicio-dto` | `pelicula_service.py` (género existe) + `pelicula_dto.py` |
| `feature/peliculas-filtro-paginacion` | `listar_filtrado` + `pelicula_query_dto.py`: filtrar → ordenar → paginar |
| `feature/peliculas-router` | `pelicula_router.py` (5 endpoints) + registrar en `main.py` y `dependencies.py` |
| `feature/peliculas-seeder` | `pelicula_seeder.py` (10+ películas, una con año futuro) |

## Danna Ramirez — Calidad y pruebas
| Rama | Tarea |
|---|---|
| `feature/resenas-mapper-repo` | `resena_mapper.py` + `resena_repository.py` |
| `feature/resenas-reglas-servicio` | `resena_service.py` con las reglas RN1, RN2, RN3 y existencia de usuario/película + `resena_dto.py` |
| `feature/resenas-router` | `resena_router.py` (6 endpoints, incluye `/peliculas/{id}/resenas`) + registrar en `main.py` y `dependencies.py` |
| `feature/resenas-seeder` | `resena_seeder.py` (10+ reseñas coherentes) |
| `feature/pruebas-manuales` | Completar `tests_manual/pruebas.http` y `evidencias.md` (6+ casos con esperado/obtenido) |

## Todos
- Cada integrante: al menos 5 commits propios, una rama distinta de `main` y 1 PR.
- Antes de abrir un PR: `git pull origin main` en tu rama, resolver conflictos (los marcadores `TODO(nombre)` en `main.py`, `dependencies.py` y `seed.py` están separados para evitarlos) y probar con Swagger.
- Defensa: todos deben poder explicar router → servicio → repositorio → base de datos de **cualquier** entidad.
