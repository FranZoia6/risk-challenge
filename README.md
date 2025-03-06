# risk-challenge

## Instrucciones para el despliegue del sistema

El sistema está preparado para ejecutarse en contenedores Docker. Para ello, es necesario tener Docker instalado previamente. Puedes consultar cómo hacerlo en el sitio oficial [aquí](https://www.docker.com/).

### Pasos para levantar el sistema:

1. **Construir las imágenes y levantar los contenedores**:

   Ejecuta el siguiente comando desde el directorio raíz del proyecto:

   ```bash
   docker compose up --build
   ```

   Este comando construirá las imágenes necesarias y levantará los contenedores con sus respectivas dependencias.

2. **Levantar los contenedores sin reconstruir las imágenes:**

Una vez que las imágenes estén construidas, puedes levantar los contenedores sin necesidad de reconstruirlas utilizando el siguiente comando:

```bash
docker compose up
```

### Contenedores

El sistema levanta tres contenedores:

1. **Frontend**: Contenedor que maneja la interfaz de usuario.
2. **Backend**: Contenedor que ejecuta la lógica del servidor.
3. **Base de datos MySQL**: Contenedor que aloja la base de datos MySQL.

Una vez iniciados los contenedores, puedes acceder al frontend a través del siguiente enlace: [aquí](http://localhost:5173/). Este contenedor tiene un puerto expuesto para la comunicación con el usuario.
