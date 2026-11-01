# Guía Práctica de Comandos Esenciales de Git y GitHub para Estudiantes

El control de versiones es una herramienta fundamental en el desarrollo de software. Esta guía está redactada con explicaciones claras, analogías sencillas y procedimientos paso a paso para que puedas entender qué hace cada comando de Git, por qué existe y cuándo debes aplicarlo en tus proyectos de laboratorio y tareas.

---

## 1. Fundamentos: ¿Qué son Git y GitHub?

Antes de interactuar con la terminal, es imprescindible distinguir la diferencia entre Git y GitHub, ya que cumplen funciones complementarias dentro del flujo de desarrollo.

* **Git**: Es el programa que ejecutas localmente en tu computadora. Su función es tomar "fotos" (capturar versiones fijas) de tus archivos a medida que avanzas. Si cometes un error o rompes tu código, Git te permite regresar a la foto guardada en el momento en que todo funcionaba.
* **GitHub**: Es la plataforma en la nube donde almacenas y respaldas esas fotos. Permite que tu equipo de trabajo pueda visualizar el proyecto, descargar la versión más reciente y combinar sus aportes de forma organizada.

> **Analogía clave**: Piensa en un videojuego. **Git** es el botón local para "Guardar partida" en tu consola para no perder tu avance personal. **GitHub** es el servidor multijugador en la nube donde tu progreso se conecta y se une con el de tus amigos.

---

## 2. Preparación: Inicializar y Descargar el Repositorio

La forma más sencilla y libre de errores para iniciar un proyecto consiste en crear primero el repositorio en la web de GitHub e inmediatamente clonarlo (descargarlo) en tu computadora.

### 1. Clonar un repositorio (`git clone`)

Tras crear tu repositorio en GitHub con un nombre corto (por ejemplo, `mi-primer-repo`), seleccionar visibilidad pública e incluir un archivo `README`, copias la dirección HTTPS proporcionada y ejecutas en la terminal:

```bash
git clone https://github.com/tu-usuario/mi-primer-repo.git
```

* **¿Para qué sirve?**: Descarga una copia completa del repositorio remoto desde GitHub a tu equipo y establece la conexión inicial entre la carpeta local y el servidor.
* **¿Cuándo usarlo?**: Exclusivamente la primera vez que vas a comenzar a trabajar en un proyecto nuevo o existente almacenado en GitHub.

### 2. Entrar a la carpeta del proyecto (`cd`)

Una vez completada la descarga, debes ubicar la terminal dentro de la carpeta del proyecto.

```bash
cd mi-primer-repo
```

* **¿Para qué sirve?**: Cambia el directorio de trabajo activo de la consola hacia la carpeta recién creada por Git.
* **¿Cuándo usarlo?**: Justo después de clonar el repositorio, antes de ejecutar cualquier otro comando.

---

## 3. El Flujo Diario de Trabajo: El Ritual de 3 Pasos

Cada vez que creas un archivo o modificas tu código, debes realizar un ritual de tres pasos para registrar tus avances. Este proceso se comprende claramente mediante la analogía de enviar un paquete por correo:

1. **`git add`**: Elegir qué elementos vas a meter dentro de la caja de envío.
2. **`git commit`**: Cerrar la caja y colocarle una etiqueta con tu nombre y nota explicativa.
3. **`git push`**: Enviar el paquete sellado hacia el servidor de GitHub.

### Inspección previa: `git status`

Antes de comenzar el ritual, debes verificar qué archivos han cambiado en tu carpeta.

```bash
git status
```

* **¿Para qué sirve?**: Es tu herramienta de diagnóstico principal ("tu mejor amigo"). Te informa en qué rama estás parado y qué archivos han sido modificados, agregados o eliminados.
* **¿Cuándo usarlo?**: Constantemente. Utilízalo antes de preparar tus cambios y después de guardar para confirmar el estado de tu repositorio.

### Paso 1: Preparar los archivos (`git add`)

Cuando terminas una modificación y deseas incluirla en la próxima foto del proyecto:

```bash
git add .
```

* **¿Para qué sirve?**: Prepara todos los archivos nuevos o modificados de la carpeta actual (el punto `.` representa todos los archivos del directorio) para ser guardados.
* **¿Cuándo usarlo?**: Al concluir un cambio funcional en tu código que quieras empaquetar.

### Paso 2: Confirmar la versión (`git commit`)

Una vez preparados los archivos, procedes a tomar la foto oficial en tu computadora local.

```bash
git commit -m "Agrego archivo principal de saludo"
```

* **¿Para qué sirve?**: Crea un registro oficial e inmutable en el historial de tu computadora local, adjuntando un mensaje descriptivo obligatorio que explica qué hiciste.
* **¿Cuándo usarlo?**: Inmediatamente después de `git add .`, usando la bandera `-m` con una descripción breve entre comillas.

### Paso 3: Subir a la nube (`git push`)

El paso final consiste en transferir tus fotos confirmadas hacia la plataforma web.

```bash
git push origin main
```

* **¿Para qué sirve?**: Envía los commits confirmados en tu equipo hacia el repositorio remoto en GitHub (en este caso, a la rama `main`).
* **¿Cuándo usarlo?**: Al terminar tu sesión de trabajo o cuando quieras respaldar tus cambios para que tus compañeros los vean.

---

## 4. Trabajo Colaborativo: Ramas (Branches) y Fusión (Merge)

Si dos o más personas editan la rama principal (`main`) de forma simultánea, se pueden generar conflictos en el código. Para evitarlo, cada estudiante crea su propia **rama** (un entorno de trabajo paralelo y seguro).

### Crear y trasladarse a una nueva rama

```bash
git checkout -b rama-companero
```

* **¿Para qué sirve?**: Crea una rama nueva en tu equipo y te mueve automáticamente a ella para trabajar de forma aislada.
* **¿Cuándo usarlo?**: Cada vez que vayas a desarrollar una característica o tarea nueva en el equipo.

### Cambiar entre ramas existentes

```bash
git checkout main
```

* **¿Para qué sirve?**: Te traslada a una rama que ya existe en el proyecto (por ejemplo, para volver a la rama principal).
* **¿Cuándo usarlo?**: Cuando requieras verificar el estado del código principal o trabajar en otra rama previa.

### Descargar actualizaciones (`git pull`)

```bash
git pull origin main
```

* **¿Para qué sirve?**: Descarga e integra en tu computadora los últimos cambios que tus compañeros hayan subido a GitHub.
* **¿Cuándo usarlo?**: Al iniciar tu día de trabajo o antes de fusionar código para asegurarte de estar actualizado.

---

### Escenarios de Fusión (Merge)

Una vez terminados los cambios en una rama, existen dos procedimientos para unir el trabajo a la rama principal:

#### Escenario A: Fusión visual mediante Pull Request en GitHub.com

Es la alternativa más clara y recomendada para principiantes.

1. Subes tu rama de trabajo a GitHub:
   ```bash
   git push origin rama-companero
   ```
2. Entras a la página del repositorio en **GitHub.com**.
3. Verás un aviso destacado y harás clic en el botón **Compare & pull request**.
4. Revisas los cambios en pantalla (líneas en verde para código nuevo, en rojo para borrado) y confirmas con los botones **Merge pull request** y **Confirm merge**.
5. Finalmente, en tu computadora ejecutas `git pull origin main` para descargar la unión terminada a tu equipo.

#### Escenario B: Fusión directa desde la terminal

Si prefieres realizar la unión directamente desde la consola:

1. Te ubicas en la rama principal:
   ```bash
   git checkout main
   ```
2. Descargas la información de ramas más reciente en el servidor:
   ```bash
   git fetch origin
   ```
   * *Propósito*: Actualiza la información de tu computadora para que reconozca las ramas nuevas subidas por tus compañeros a GitHub.
3. Fusionas la rama remota dentro de tu rama actual:
   ```bash
   git merge origin/rama-companero
   ```
   * *Propósito*: Une el código de la rama de tu compañero dentro de tu rama `main` local.
4. Subes la fusión resultante a GitHub:
   ```bash
   git push origin main
   ```

---

## 5. Hoja de Referencia Rápida (Cheat Sheet)

Puedes utilizar esta tabla condensada como material de apoyo rápido durante tus clases y prácticas:

| Comando | Sintaxis / Ejemplo | Descripción y Función |
| :--- | :--- | :--- |
| **`git status`** | `git status` | Muestra qué archivos modificaste y en qué rama te encuentras actualmente. |
| **`git clone`** | `git clone <url-https>` | Descarga un repositorio de GitHub por primera vez a tu computadora. |
| **`git add`** | `git add .` | Prepara todos los archivos modificados para ser incluidos en la próxima versión. |
| **`git commit`** | `git commit -m "mensaje"` | Registra una versión oficial local acompañada de un mensaje explicativo. |
| **`git push`** | `git push origin <rama>` | Sube tus versiones guardadas localmente al servidor de GitHub. |
| **`git pull`** | `git pull origin <rama>` | Descarga e integra en tu equipo los cambios más recientes de GitHub. |
| **`git checkout -b`** | `git checkout -b <rama>` | Crea una rama nueva y se posiciona en ella inmediatamente. |
| **`git checkout`** | `git checkout <rama>` | Se traslada a una rama existente dentro del proyecto. |
| **`git fetch`** | `git fetch origin` | Descarga la información y metadatos de las ramas presentes en GitHub. |
| **`git merge`** | `git merge origin/<rama>` | Fusiona los cambios de una rama especificada dentro de tu rama actual. |
