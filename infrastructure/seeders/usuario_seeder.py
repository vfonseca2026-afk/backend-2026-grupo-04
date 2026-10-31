from application.services.usuario_service import UsuarioService


def seed_usuarios(service: UsuarioService) -> None:
    datos = [
        ("ana_cine", "ana.cine@example.com", True),
        ("bruno_cine", "bruno.cine@example.com", True),
        ("carla_cine", "carla.cine@example.com", True),
        ("diego_cine", "diego.cine@example.com", True),
        ("elena_cine", "elena.cine@example.com", True),
        ("fabian_cine", "fabian.cine@example.com", False),
    ]

    for nombre_usuario, email, activo in datos:
        usuario = service.crear(
            nombre_usuario=nombre_usuario,
            email=email,
        )

        if not activo:
            service.actualizar(
                usuario_id=usuario.id,
                nombre_usuario=usuario.nombre_usuario,
                email=usuario.email,
                activo=False,
            )