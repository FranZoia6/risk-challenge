# Risk-challenge

## Instrucciones para el despliegue del sistema

   El sistema está preparado para ejecutarse en contenedores Docker. Para ello, es necesario tener Docker instalado previamente. Puedes consultar cómo hacerlo en el sitio oficial [aquí](https://www.docker.com/).

### Pasos para levantar el sistema:

   1.  **Construir las imágenes y levantar los contenedores**:

      Ejecuta el siguiente comando desde el directorio raíz del proyecto:

      ```bash
      docker compose up --build
      ```

      Este comando construirá las imágenes necesarias y levantará los contenedores con sus respectivas dependencias.

   2.  **Levantar los contenedores sin reconstruir las imágenes:**

      Una vez que las imágenes estén construidas, puedes levantar los contenedores sin necesidad de reconstruirlas utilizando el siguiente comando:

      ```bash
      docker compose up
      ```

   3.  **Dar de baja los contenedores:**
      Para detener y eliminar los contenedores, redes y volúmenes creados por docker compose up, ejecuta el siguiente comando:

      ```bash
      docker compose down
      ```

## Contenedores

   El sistema levanta tres contenedores:

   1.  **Frontend**: Contenedor que maneja la interfaz de usuario.
   2.  **Backend**: Contenedor que ejecuta la lógica del servidor.
   3.  **Base de datos MySQL**: Contenedor que aloja la base de datos MySQL.

   Una vez iniciados los contenedores, puedes acceder al frontend a través del siguiente enlace: [aquí](http://localhost:5173/). Este contenedor tiene un puerto expuesto para la comunicación con el usuario.

## Migración de datos

   Por defecto, el sistema ya cuenta con un usuario y varios registros cargados. Puedes acceder al sistema con las siguientes credenciales iniciales:

   ```bash
   Usuario: user
   Contraseña: abc123
   ```

## Test

   Para ejecutar las pruebas unitarias, es necesario crear un entorno virtual.

   1.  Dirígete a la carpeta /backend:

      ```bash
      cd backend

      ```

   2.  **Crear un entorno virtual**

      ```bash
      python3 -m venv venv
      ```

   3.  **Activar el entorno virtual**

      . **Windows:**

      ```bash
      .\venv\Scripts\activate
      ```

      . **Linux:**

      ```bash
      source venv/bin/activate
      ```

   4.  **Instalar todas las librerías, ejecuta:**

      ```bash
      pip install -r requirements.txt

      ```

   5.  **Desactivar el entorno:**

      ```bash
      deactivate
      ```
