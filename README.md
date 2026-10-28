# TP Integrador - Server State y Navegación - Unidad 7

**Materia:** Programación IV — Tecnicatura Universitaria en Programación a Distancia (UTN)

Aplicación **Full Stack** completa que implementa el **CRUD de Categorías** desde una interfaz de usuario en React gobernada por **TanStack Query** (`useQuery` y `useMutation` con invalidación automática de caché) y enrutada mediante **React Router** (`react-router-dom`), conectada a un backend de alto rendimiento en **FastAPI** con **SQLModel** y base de datos **PostgreSQL**. Paralelamente, se incluye la implementación completa y demostración del **CRUD de Productos** y la relación relacional muchos-a-muchos ($N:M$ entre `Producto` y `Categoria`) mediante el archivo de pruebas `productos.http` con REST Client.

---

## 🏗️ Estructura del Repositorio

```text

TP_RelacionesYestados_7/

├── fastapi-productos/ # Backend (FastAPI + SQLModel + PostgreSQL)

│ ├── app/

│ │ ├── __init__.py

│ │ ├── main.py # Instancia de FastAPI, routers, lifespan y CORS

│ │ ├── core/

│ │ │ ├── __init__.py

│ │ │ └── database.py # Engine SQLAlchemy/SQLModel, session y DDL

│ │ ├── categoria/

│ │ │ ├── __init__.py

│ │ │ ├── model.py # Modelo Categoria

│ │ │ ├── schema.py # Schemas CategoriaCreate, Update, Read

│ │ │ ├── service.py # Lógica de negocio y persistencia

│ │ │ └── router.py # Endpoints CRUD /categorias (201, 204, 404)

│ │ └── producto/

│ │ ├── __init__.py

│ │ ├── model.py # Modelo Producto y tabla intermedia ProductoCategoria

│ │ ├── schema.py # Schemas ProductoCreate, Update, Read, CategoriaAssign

│ │ ├── service.py # CRUD Producto y endpoints de asociación relacional

│ │ └── router.py # Endpoints /productos y /productos/{id}/categorias

│ ├── .env # Variable de entorno DATABASE_URL

│ ├── requirements.txt # Dependencias de Python

│ └── productos.http # Suite de pruebas de endpoints y relación N:M

│

├── tp-categorias/ # Frontend (React + TypeScript + Vite + Tailwind CSS)

│ ├── src/

│ │ ├── components/

│ │ │ ├── Navbar.tsx # Navegación SPA con Link (/categorias, /productos)

│ │ │ ├── CategoriaCard.tsx # Fila de tabla / tarjeta con botones Editar y Eliminar

│ │ │ ├── CategoriaList.tsx # Renderizado de lista con tabla responsiva

│ │ │ └── CategoriaModal.tsx# Modal controlado para altas y modificaciones

│ │ ├── pages/

│ │ │ ├── CategoriasPage.tsx# Server State con useQuery, useMutation e invalidación

│ │ │ └── ProductsPage.tsx # Vista de sección informativa para /productos

│ │ ├── services/

│ │ │ └── categoria.ts # Funciones fetch a la API con control de response.ok

│ │ ├── types/

│ │ │ ├── categoria.ts # Interfaces Categoria, CategoriaCreate, CategoriaUpdate

│ │ │ └── producto.ts # Interface Producto

│ │ ├── App.tsx # Definición pura de rutas (Routes, Route) y Navbar

│ │ ├── main.tsx # Configuración de QueryClientProvider y BrowserRouter

│ │ └── index.css # Directivas de Tailwind CSS

│ ├── package.json

│ ├── tsconfig.json

│ └── vite.config.ts

│

├── .gitignore # Exclusiones de Git (.venv, node_modules, .env, dist)

└── README.md # Documentación técnica del proyecto
```

---

## 🛠️ Tecnologías Aplicadas

  

-  **Backend:** Python 3.13, FastAPI (Standard), SQLModel / SQLAlchemy, PostgreSQL (`psycopg` / `psycopg2-binary`), Pydantic v2.

- Columnas compuestas: Arreglo de cadenas `ARRAY(String)` en `imagenes_url`.

- Validación de campos: Restricción `precio_base >= 0`.

-  **Frontend:** React 19, TypeScript, Vite, Tailwind CSS, TanStack Query v5 (`@tanstack/react-query`), React Router v7 (`react-router-dom`).

-  **Arquitectura & Estado:**

- Separación de responsabilidades: `App.tsx` desacoplado de lógica de datos.

- Manejo de estado del servidor con `useQuery` y `useMutation` + `queryClient.invalidateQueries`.

- Manejo de estado de interfaz local con `useState` (apertura y cierre de modales y entidad seleccionada).

- Tipado estricto mediante interfaces y `import type`.

---


## 🚀 Puesta en Marcha

### 1. Base de Datos (PostgreSQL)

Asegurarse de que el servicio de PostgreSQL esté en ejecución en el puerto `5432` y que la base de datos `productos_db` esté creada:

```sql

CREATE  DATABASE  productos_db;

```
---


### 2. Backend (`fastapi-productos`)

1. Ubicarse en el directorio del backend:

```powershell

cd fastapi-productos

```

2. Crear y activar el entorno virtual:

-  **En Windows (PowerShell):**

```powershell

python -m venv .venv

.\.venv\Scripts\Activate.ps1

```

-  **En Linux / macOS:**

```bash

python -m venv .venv

source .venv/bin/activate

```

3. Instalar dependencias requeridas:

```powershell

pip install -r requirements.txt

```

4. Configurar el archivo `.env` en la raíz de `fastapi-productos/`:

```env

DATABASE_URL=postgresql+psycopg://postgres:admin123@localhost:5432/productos_db

```

*(Ajustar usuario y contraseña según la configuración local de PostgreSQL)*.

5. Iniciar el servidor en modo desarrollo:

```powershell

python -m fastapi dev app/main.py

```

-  **Servidor local:**  `http://127.0.0.1:8000`

-  **Documentación Swagger UI interactiva:**  `http://127.0.0.1:8000/docs`

---

### 3. Frontend (`tp-categorias`)

1. En una nueva terminal, ubicarse en la carpeta del frontend:

```powershell

cd tp-categorias

```

2. Instalar los paquetes mediante gestor de paquetes (`npm` o `pnpm`):

```powershell

npm install

```

3. Ejecutar el servidor de desarrollo Vite:

```powershell

npm run dev

```

-  **Aplicación web:**  `http://localhost:5173`

---
## 🧪 Pruebas de Endpoints y Relación N:M

El CRUD completo de `Producto` y los endpoints de enlace de la tabla intermedia `ProductoCategoria` se demuestran mediante el archivo `productos.http` ubicado en `fastapi-productos/`:

1. Instalar la extensión **REST Client** de VS Code (`humao.rest-client`).

2. Abrir el archivo `fastapi-productos/productos.http`.

3. Ejecutar secuencialmente las solicitudes haciendo clic en **`Send Request`**:

-  `POST /categorias/`: Creación de categorías de prueba (Responde `201 Created`).

-  `GET /categorias/`: Listado general de categorías.

-  `POST /productos/`: Creación de producto con validación de precio y lista de URLs de imágenes.

-  `POST /productos/{id}/categorias`: Asignación de categorías a un producto.

-  `GET /productos/{id}/categorias`: Obtención de categorías asociadas a un producto específico.

-  `DELETE /productos/{id}/categorias/{categoria_id}`: Desvinculación de la relación relacional (Responde `204 No Content`).

-  `PUT /productos/{id}` y `DELETE /productos/{id}`: Actualización y baja de producto.

---

## ✅ Verificación de Compilación y Tipado Estricto

Para validar que el proyecto no contiene errores de TypeScript y cumple con las directivas estrictas de tipado (`tsc -b`):

```powershell

cd tp-categorias

npm run build

```

---

## 📦 Modalidad de Entrega (.zip)

Para preparar el archivo comprimido final requerido por la cátedra:

1. Eliminar la carpeta `node_modules/` y `dist/` dentro de `tp-categorias/`.

2. Eliminar la carpeta `.venv/` y cualquier directorio `__pycache__/` dentro de `fastapi-productos/`.

3. Comprimir ambas carpetas limpias en un único archivo `.zip`.

---

## 👤 Autor

**Nicolás A. Pannunzio**

- 💼 [Perfil en LinkedIn](https://www.linkedin.com)

- 📂 Repositorio en GitHub: [TPI-ServerStateYnavegacion-P4-UTN](https://github.com/nicolaspannunzio/TPI-ServerStateYnavegacion-P4-UTN.git) (Rama principal: `main`)

## Verificación final (Unidad 7)

### Frontend

Desde `tp-categorias/`, instalar dependencias y ejecutar:

```bash
npm install
npm run build
npm run dev
```

Opcionalmente, crear `tp-categorias/.env` con `VITE_API_URL=http://localhost:8000` si se desea cambiar la URL de la API. Si no se define, se utiliza ese valor por defecto.

### Backend y REST Client

Desde `fastapi-productos/`, activar el entorno virtual, instalar `requirements.txt`, configurar `DATABASE_URL` y ejecutar FastAPI. Abrir `/docs` para comprobar la documentación. En `productos.http`, actualizar `@categoriaId`, `@categoriaId2` y `@productoId` con IDs existentes en la base de datos y ejecutar las solicitudes en orden. Las solicitudes de borrado deben ejecutarse al final.

El frontend presenta errores de API en la interfaz. Las validaciones de schemas rechazan nombres vacíos y precios negativos.
