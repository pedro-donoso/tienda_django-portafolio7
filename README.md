# Gestión de Tienda – Django + ORM

Aplicación web desarrollada con Django que muestra el uso del ORM para integrar modelos simples y relacionados con una base de datos. Permite gestionar Productos, Clientes y Pedidos, incluyendo relaciones uno a muchos y muchos a muchos, migraciones, consultas de filtrado y operaciones CRUD completas.

## Tecnologías

- Python 3
- Django 5
- SQLite (por defecto)
- Bootstrap 5

## Objetivos del proyecto

- Integrar Django con una base de datos mediante su ORM.
- Definir modelos:
  - Sin relaciones: `Producto`.
  - Con relaciones:
    - Uno a muchos: `Cliente` → `Pedido`.
    - Muchos a muchos: `Pedido` ↔ `Producto`.
- Utilizar migraciones para crear y modificar el esquema.
- Realizar consultas de filtrado y personalizadas con el ORM.
- Implementar una app web estilo MVC con CRUD completo.
- Usar aplicaciones preinstaladas de Django como `admin`, `auth` y `sessions`.

## Estructura principal

- Proyecto: `gestion_tienda`
- App: `productos`
- Modelos:
  - `Producto`: `nombre`, `precio`, `cantidad`, `descripcion`.
  - `Cliente`: `nombre`, `correo`.
  - `Pedido`: `numero`, `cliente` (`ForeignKey`), `productos` (`ManyToManyField`), `fecha`.

### Acceder en el navegador:

- Página de inicio: http://127.0.0.1:8000/
- Panel admin: http://127.0.0.1:8000/admin/

## Rutas principales

- Home (explica la app y muestra enlaces):
- `/`

### Clientes (CRUD):
- Listar: `/clientes/`
- Crear: `/clientes/crear/`
- Editar: `/clientes/<id>/editar/`
- Eliminar: `/clientes/<id>/eliminar/`

### Productos (CRUD, modelo sin relaciones):
- Listar: `/productos/`
- Crear: `/productos/crear/`
- Editar: `/productos/<id>/editar/`
- Eliminar: `/productos/<id>/eliminar/`

### Pedidos (CRUD, modelo con relaciones):
- Listar: `/pedidos/`
- Crear: `/pedidos/crear/`
- Editar: `/pedidos/<id>/editar/`
- Eliminar: `/pedidos/<id>/eliminar/`

### Consultas ORM filtradas (ejemplo):
- `/pedidos/cliente/<id>/?inicio=YYYY-MM-DD&fin=YYYY-MM-DD`

