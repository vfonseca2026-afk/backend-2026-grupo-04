"""TODO(Danna) — Servicio de Reseña: aquí viven las REGLAS DE NEGOCIO.

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: application/services/genero_service.py

Recibe ResenaRepository, UsuarioRepository y PeliculaRepository
(los dos últimos los publican Matías y Miguel: método obtener_por_id).

crear(usuario_id, pelicula_id, puntuacion, titulo, comentario), en este orden:
  1. El usuario existe  (EXISTENCIA RELACIONADA)  -> RecursoNoEncontradoError (404)
  2. La película existe (EXISTENCIA RELACIONADA)  -> RecursoNoEncontradoError (404)
  3. Usuario inactivo no puede reseñar             -> ReglaNegocioError (400)   [usar usuario.puede_resenar()]
  4. No se reseña una película no estrenada        -> ReglaNegocioError (400)   [usar pelicula.esta_estrenada()]
  5. Un usuario reseña una película UNA sola vez   -> ConflictoError (409)
actualizar: solo puntuacion, titulo y comentario (usuario y película no cambian).
También: obtener, listar, listar_por_pelicula (verifica que la película exista), eliminar.
"""
