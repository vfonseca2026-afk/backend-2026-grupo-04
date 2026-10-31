"""TODO(Matías) — Router de Usuarios (prefix="/usuarios", tags=["Usuarios"]).

Patrón a copiar: el recorrido completo de Género (domain -> model -> mapper -> repository -> service -> DTO -> router).
Archivo de referencia: presentation/routers/genero_router.py

  POST   /usuarios                201  crear
  GET    /usuarios                200  listar paginado (items,total,pagina,limite,total_paginas)
  GET    /usuarios/{usuario_id}   200  obtener
  PUT    /usuarios/{usuario_id}   200  actualizar
  DELETE /usuarios/{usuario_id}   204  eliminar
Sin try/except ni consultas a la BD aquí: solo llamar al servicio.
Documentar cada endpoint: summary, description y responses (RESP_404, RESP_409...).
Al terminar: registrar el router en app/main.py y get_usuario_service en
presentation/dependencies.py (reemplazando tus líneas TODO).
"""
