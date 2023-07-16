# Entrega-Final-Cuello-Lopez

### 1. Pruebas

La preentrega consta de 3 modelos sobre especies del mercado de capitales

1.1. BONOS
1.2. ACCIONES
1.3. FUTUROS

Cada una tiene su forma particular de carga y contienen diferentes campos.

Para la prueba de la carga de cada una en particular primero debes realizar la baja de la preentrega en tu computadora.

Luego de eso correr el servidor de la entrega. Ya con el mismo podes ingresar en el vinculo del área superior derecha de la pantalla que dice "Especies".

Una vez dentro tendrás 3 botones que te dirigirán a 3 páginas diferentes para la carga de cada tipo de especie.

#### 1.1.BONOS

En la página de especies antes mencionada. Clickear en el botón que dice "Crear Bono". El mismo te dirigirá a una nueva página para realizar la carga de una nueva especie de bono.

##### 1.1.1 Campos Bonos

Los campos con los que cuenta son los siguientes:

1. Ticker: Es el acrónimo con el cual es identificado en el mercado (Ej. AL29D = Bono Argentina 2029 y la D de expresado en dólares). Consta de 5 carácteres alfanuméricos
2. Descripción: Brinda más detalle del ticker. Consta de hasta 30 carácteres alfanuméricos.
3. Cupón: Es el interés que paga el bono acordado en el momento de la emisión. Consta de decimales que detallan el monto de interés (entre 0.01 = 1% y 1 = 100%).
4. Emisor: Es el campo en el cual detallamos a qué empresa hace referencia el bono o si hace referencia a un estado Soberano (Ej. Argentina) o SubSoberano (Ej. Provincia de Córdoba). Consta de hasta 30 carácteres alfanuméricos.
5. Fecha de emisión: Fecha en la cual se emitió el bono. Fecha en formato (MM/DD/YYYY).
6. Fecha de vencimiento: Fecha en la cual venció el bono. Fecha en formato (MM/DD/YYYY).

##### 1.1.2 Prueba Bonos

Un ejemplo para probar esta funcionalidad podría ser:

Ticker: GD35D
Descripción: GLOBAL 2035
Cupón: 0.07
Emisor: ARGENTINA
Fecha de emisión: 7/9/2020
Fecha de vencimiento: 7/9/2035

Luego del ingreso de los datos, clickear en el botón crear. Esto generará la nueva especie y los redigirá a la página de "Listado de especies" donde verán esta nueva especie ya cargada.

#### 1.2.ACCIONES

En la página de especies antes mencionada. Clickear en el botón que dice "Crear Acción". El mismo te dirigirá a una nueva página para realizar la carga de una nueva especie de bono.

##### 1.2.1 Campos Acciones

Los campos con los que cuenta son los siguientes:

1. Ticker: Es el acrónimo con el cual es identificado en el mercado (Ej. GOOG = Alphabeth - Google). Consta de hasta 4 carácteres alfanuméricos
2. Descripción: Brinda más detalle del ticker y qué tipo de acción es (Ordinaria/Extraordinaria/Preferida). Consta de hasta 30 carácteres alfanuméricos.
3. Empresa: Hace referencia a la entidad que emitió la acción. Consta de hasta 20 carácteres alfanuméricos.

##### 1.2.2 Prueba Acciones

Un ejemplo para probar esta funcionalidad podría ser:

Ticker: BBAR
Descripción: Acc. Ord. Banco Francés
Empres: Banco Francés

Luego del ingreso de los datos, clickear en el botón crear. Esto generará la nueva especie y los redigirá a la página de "Listado de especies" donde verán esta nueva especie ya cargada.

#### 1.3.Futuros

En la página de especies antes mencionada. Clickear en el botón que dice "Crear Futuro". El mismo te dirigirá a una nueva página para realizar la carga de una nueva especie de bono.

##### 1.3.1 Campos Futuros

Los campos con los que cuenta son los siguientes:

1. Ticker: Es el acrónimo con el cual es identificado en el mercado (Ej. DLR072023 - Futuro de dólar a julio 2023). Consta de 9 carácteres alfanuméricos
2. Descripción: Brinda más detalle del ticker y qué tipo de acción es (Ordinaria/Extraordinaria/Preferida). Consta de hasta 30 carácteres alfanuméricos.
6. Fecha de vencimiento: Fecha en la cual venció el bono. Fecha en formato (MM/DD/YYYY).

##### 1.3.2 Prueba Acciones

Un ejemplo para probar esta funcionalidad podría ser:

Ticker: DLR102023
Descripción: FUT DOLAR OCT 2023
Empresa: 10/31/2023

Luego del ingreso de los datos, clickear en el botón crear. Esto generará la nueva especie y los redigirá a la página de "Listado de especies" donde verán esta nueva especie ya cargada.

#### 1.4 Listado de Especies

Para ir a esta página deben ingresar en el vinculo del área superior derecha de la pantalla que dice "Especies" que los llevará a la página del listado de especies. En ella de desplegarán todas las especies cargadas hasta el momento.

##### 1.4.1 Prueba Listado de especies

Para realizar la prueba de esta funcionalidad, dentro de la pantalla de listado de especies mencionada en el punto anterior deben ingresar el ticker buscado en el formulario y clickear en el botón "Buscar".

Una prueba sencilla es buscar "GD" y apareceran todos los bonos globales de Argentina ingresados hasta el momento.


#### 1.5.BLOGS

Para acceder a este apartado debermos estar logueados con nuestra cuenta dentro de la página (ver 1.7)
Logueados en la misma, clickearemos en el encabezado superior donde dice "Blogs".
Una vez en la página podrán realizar una búsqwueda de los blogs creados por titulo, subtitulo o autor, además de la opción de crear un nuevo blog clickeando en el boton "Crear Nuevo Blog".

##### 1.5.1 Campos Blogs

Los campos con los que cuenta son los siguientes:

1. Título: Es el títlo del blog, puede contener hasta 30 carácteres alfanuméricos.
2. Subtitulo: Es el títlo del blog, puede contener hasta 40 carácteres alfanuméricos.
3. Autor: Es quien realizó la entrada del blog, puede contener hasta 30 carácteres alfanuméricos.
4. Fecha Publicación: Es la fecha en la cual se creó la entrada. Fecha en formato (MM/DD/YYYY).
6. Cuerpo: Contenido propiamente del Blog, consta de texto enriquecido.
7. Imagen: Campo en el cual se puede subir alguna imagen en el caso de querer realizarlo. Opcional.


#### 1.6.MENSAJES

Para acceder a este apartado debermos estar logueados con nuestra cuenta dentro de la página (ver 1.7)
Logueados en la misma, clickearemos en el encabezado superior donde dice "Mensajes".
Una vez en la página se desplegará un listado con todos los mensajes recibidos por el usuario con su correspondiente autor, además de la opción de crear un nuevo mensaje clickeando en el boton "Crear Nuevo Mensaje".

##### 1.5.1 Campos Mensajes

Los campos con los que cuenta son los siguientes:

1. Mensaje: Contenido propiamente del Blog, consta de texto enriquecido.
2. Receptor: Es el usuario al que va dirigido el mensaje.


#### 1.7 USUARIOS

En este apartado veremos lo concerniente a las cuentas de usuario de la página.

##### 1.7.1 Crear Cuenta

Para crear una cuenta, estando en la página inicial del proyecto, clickearemos en Registrase

Los campos con los que cuenta son los siguientes:

1. Username: Es el nombre de usuario.
2. Email: es el email con el que se registra el usuario.
3. Contraseña: es la contraseña con la cual el usuario va a iniciar sesión.
3. Repetir Contraseña: Repetir Contraseña.

##### 1.7.2 Iniciar Sesión

Para iniciar sesión deben clickear en el encabezado superior de la página donde dice "Iniciar Sesión".

Solicitará los siguientes campos:

1. Usuario
2. Contraseña

Validados ambos campos podrán ingresar a su cuenta.

Logueados permitira poder crear y editar las especies (Bonos, Acciones, Futuros) y leer, crear entradas de blogs y mensajes.

##### 1.7.3 Cerrar Sesión

Para cerrar sesión deben clickear en el encabezado superior de la página donde dice "Cerrar Sesión".

##### 1.7.4 Perfil de usuario

Para al perfil de usuario deben clickear en el encabezado superior de la página donde se encuentra el nombre del usuario.

Esta página muestra los datos del usuario (a excepcion de la contraseña), los cuales son los siguientes:

1. Foto de Perfil: imagen de perfil que se puede agregar desde la edición de perfil.
2. Nombre: Nombre del usuario.
3. Apellido: Apellido del usuario.
4. Email: email del usuario.
5. Descripción: una breve descripción del usuario. Opcional
6. Página Web: Página web del usuario. Opcional

##### 1.7.4.1 Editar Perfil

Desde el perfil del usuario podemos clickear en el botón Editar Perfil y podremos acceder a editar los datos de usuario.

En esta página podemos editar los siguientes campos:

1. Email
2. Nombre
3. Apellido
4. Avatar (imagen de perfil)
5. Descripción
6. Página Web

Una vez realizado los cambios, clickear en "Guardar Cambios" y se actualizará la información.

##### 1.7.4.1 Cambiar Contraseña

Desde el perfil del usuario podemos clickear en el botón "Cambiar Contraseña" y podremos acceder a editar los datos de usuario.

Se solicitará la contraseña actual y la nueva contraseña, con su posterior confirmación para realizar los cambios.
