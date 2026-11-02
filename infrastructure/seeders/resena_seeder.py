from application.services.resena_service import ResenaService
from infrastructure.repositories.pelicula_repository import PeliculaRepository
from infrastructure.repositories.usuario_repository import UsuarioRepository


def seed_resenas(
    service: ResenaService,
    usuario_repository: UsuarioRepository,
    pelicula_repository: PeliculaRepository,
) -> None:
    """Carga diez reseñas ficticias respetando las reglas de publicación."""
    usuarios = usuario_repository.listar(
        offset=0,
        limite=max(1, usuario_repository.contar()),
    )

    peliculas, _ = pelicula_repository.listar_filtrado(
        offset=0,
        limite=max(1, pelicula_repository.contar()),
    )

    usuarios_activos = [
        usuario
        for usuario in usuarios
        if usuario.puede_resenar() and usuario.id is not None
    ]

    peliculas_estrenadas = [
        pelicula
        for pelicula in peliculas
        if pelicula.esta_estrenada() and pelicula.id is not None
    ]

    parejas = [
        (usuario, pelicula)
        for pelicula in peliculas_estrenadas
        for usuario in usuarios_activos
    ]

    # Se comprueban las condiciones antes de crear el primer registro.
    if len(parejas) < 10:
        raise RuntimeError(
            "La carga de reseñas requiere al menos diez combinaciones "
            "de usuarios activos y películas estrenadas. "
            "Comprueba los datos iniciales de Usuarios y Películas."
        )

    for numero, (usuario, pelicula) in enumerate(parejas[:10], start=1):
        service.crear(
            usuario_id=usuario.id,
            pelicula_id=pelicula.id,
            puntuacion=6 + ((numero - 1) % 5),
            titulo=f"Opinión de ejemplo {numero}",
            comentario=(
                f"Reseña ficticia de {usuario.nombre_usuario} sobre "
                f"{pelicula.titulo}, preparada para demostrar la API."
            ),
        )