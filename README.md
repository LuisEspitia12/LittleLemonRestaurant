Little Lemon Restaurant

Este proyecto es un sitio web para el restaurante Little Lemon. Permite a los usuarios ver el menú, hacer reservas y obtener información sobre el restaurante.

Table of Contents / Tabla de Contenidos
Installation / Instalación
Usage / Uso
Views / Vistas
Models / Modelos
Contribution / Contribución
License / Licencia
Installation / Instalación
To install and run the project locally, follow these steps / Para instalar y ejecutar el proyecto localmente, sigue estos pasos:

Clone the repository / Clona el repositorio:
bash
Copy code
git clone https://github.com/LuisEspitia12/LittleLemonRestaurant.git
Install the dependencies / Instala las dependencias:
Copy code
pip install -r requirements.txt
Run the database migrations / Ejecuta las migraciones de la base de datos:
Copy code
python manage.py migrate
Start the development server / Inicia el servidor de desarrollo:
Copy code
python manage.py runserver
Usage / Uso
Once the server is up and running, you can access the website in your browser by entering the URL http://localhost:8000 / Una vez que el servidor esté en funcionamiento, puedes acceder al sitio web en tu navegador ingresando la URL http://localhost:8000.

Views / Vistas
The project includes the following main views / El proyecto incluye las siguientes vistas principales:

Home / Inicio: The homepage of the website / La página de inicio del sitio web.
About / Acerca: Information about the restaurant and its history / Información sobre el restaurante y su historia.
Menu / Menú: Displays the restaurant menu / Muestra el menú del restaurante.
Book / Reservar: Allows users to make reservations / Permite a los usuarios hacer reservas.
Reservations / Reservas: Displays all reservations made / Muestra todas las reservas realizadas.
Models / Modelos
The project uses the following database models / El proyecto utiliza los siguientes modelos de base de datos:

Booking / Reserva: Stores information about reservations made by users, such as name, booking date, booking time, and number of guests / Almacena información sobre las reservas realizadas por los usuarios, como el nombre, la fecha de reserva, la hora de reserva y el número de invitados.
MenuItem / Elemento de Menú: Represents individual items on the menu, including name, description, and price / Representa elementos individuales del menú, incluyendo nombre, descripción y precio.
Contribution / Contribución
Contributions are welcome. If you would like to contribute to the project, follow these steps / Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

Fork the repository / Haz un fork del repositorio.
Create a new branch (git checkout -b feature/new-feature) / Crea una nueva rama (git checkout -b feature/new-feature).
Make your changes and commit (git commit -am 'Add new feature') / Realiza tus cambios y haz commit (git commit -am 'Add new feature').
Push to the branch (git push origin feature/new-feature) / Haz push a la rama (git push origin feature/new-feature).
Open a Pull Request / Abre un Pull Request.
License / Licencia
This project is licensed under the MIT License. See the LICENSE file for details / Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
