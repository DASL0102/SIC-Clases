# Guía de Convenciones para Mensajes de Commit en Git

En el desarrollo colaborativo de software, escribir mensajes de commit claros y estandarizados es una práctica fundamental. Un historial de commits ordenado permite a los equipos comprender la evolución del código, rastrear errores rápidamente y automatizar la generación de notas de versión (*changelogs*). Esta guía presenta las convenciones más utilizadas en la industria, incluyendo el estándar **Conventional Commits** y el formato alternativo con corchetes.

---

## 1. ¿Por qué estandarizar los mensajes de commit?

Cuando se trabaja en equipo o en proyectos que crecen con el tiempo, un mensaje como `git commit -m "cambios"` o `git commit -m "arreglo"` resulta insuficiente. Estandarizar los mensajes resuelve problemas clave en el flujo de trabajo:

* **Comprensión inmediata**: Permite saber en segundos qué se modificó sin necesidad de revisar las líneas de código cambiadas (*diff*).
* **Navegación eficiente**: Facilita la búsqueda de cambios específicos en el historial de Git mediante `git log`.
* **Automatización**: Herramientas integradas pueden clasificar los cambios y generar archivos `CHANGELOG.md` de forma automática.
* **Integración continua**: Los sistemas de CI/CD pueden ejecutar pruebas específicas según el tipo de commit realizado.

---

## 2. Estructura Estándar: Conventional Commits

El estándar de la industria especifica que cada mensaje de commit debe estar formado por un encabezado estructurado, opcionalmente seguido de un cuerpo descriptivo y un pie de página.

### Formato estándar

`git commit -m "<tipo>(<ámbito opcional>): <descripción corta en presente>"`

### Variante con corchetes (utilizada en diversos equipos)

`git commit -m "[TIPO] <descripción corta en presente>"`

Ambas variantes persiguen el mismo objetivo: clasificar la intención de la modificación mediante una etiqueta clara al inicio del mensaje.

---

## 3. Catálogo de Etiquetas y Tipos de Commit

A continuación se detallan los tipos principales de commit con sus prefijos estándar, su equivalente en corchetes y ejemplos de aplicación práctica.

| Tipo (Estándar) | Etiqueta | Propósito | Ejemplo de Comando |
| :--- | :--- | :--- | :--- |
| **feat** | `[FEAT]` | Añade una nueva funcionalidad o característica al proyecto. | `git commit -m "feat(auth): agregar inicio de sesión con Google"` |
| **fix** | `[FIX]` | Corrije un error o fallo en el código existente. | `git commit -m "fix(carro): corregir cálculo del impuesto total"` |
| **docs** | `[DOCS]` | Cambios exclusivamente en documentación (README, comentarios, guías). | `git commit -m "docs: actualizar instrucciones de instalación"` |
| **style** | `[STYLE]` | Cambios de formato, espacios o punto y coma que no afectan la lógica. | `git commit -m "style: arreglar sangría en el archivo index.html"` |
| **refactor** | `[REFACTOR]` | Reestructuración de código para mejorar legibilidad sin cambiar su comportamiento. | `git commit -m "refactor: simplificar función de validación de correo"` |
| **test** | `[TEST]` | Adición o modificación de pruebas unitarias o de integración. | `git commit -m "test: agregar pruebas para el módulo de pagos"` |
| **chore** | `[CHORE]` | Tareas de mantenimiento, actualización de librerías o configuración del entorno. | `git commit -m "chore: actualizar dependencias en package.json"` |
| **perf** | `[PERF]` | Cambios en el código orientados a mejorar el rendimiento o velocidad de ejecución. | `git commit -m "perf: optimizar consulta a la base de datos de usuarios"` |

---

## 4. Detalle de las Etiquetas Principales

### 4.1. `feat` / `[FEAT]` — Nuevas Funcionalidades
Se utiliza únicamente cuando se agrega una característica nueva que los usuarios o la aplicación pueden utilizar.

* **Incorrecto**: `git commit -m "agregué cosas"`
* **Correcto**: `git commit -m "feat(perfil): permitir subir foto de usuario"`

### 4.2. `fix` / `[FIX]` — Corrección de Errores
Se aplica cuando se soluciona un comportamiento incorrecto o un fallo en el software.

* **Incorrecto**: `git commit -m "ya funciona"`
* **Correcto**: `git commit -m "fix(login): solucionar bloqueo al ingresar contraseña incorrecta"`

### 4.3. `docs` / `[DOCS]` — Documentación
Mantiene la documentación alineada con el código sin alterar archivos de ejecución.

* **Correcto**: `git commit -m "docs: agregar guía de instalación en el README"`

### 4.4. `refactor` / `[REFACTOR]` — Refactorización
Se utiliza cuando se limpia o reorganiza el código para hacerlo más legible o eficiente, manteniendo el mismo resultado final.

* **Correcto**: `git commit -m "refactor(api): dividir controlador en módulos independientes"`

### 4.5. `chore` / `[CHORE]` — Mantenimiento
Cubre tareas administrativas del proyecto que no alteran la lógica de negocio ni agregan características.

* **Correcto**: `git commit -m "chore: configurar archivo .gitignore para entorno local"`

---

## 5. Anatomía de un Commit Completo

Para cambios complejos que requieren más contexto que una sola línea, el mensaje de commit se puede dividir en tres secciones principales:

```text
<tipo>(<ámbito>): <descripción corta en presente imperativo>

<cuerpo descriptivo opcional explicando el porqué del cambio y detalles adicionales>

<pie de página opcional para referencias a tickets o cambios rompedores>
```

### Ejemplo de Commit Completo

```text
fix(pagos): corregir error de redondeo en pasarela de pago

Se identificó un fallo en el cálculo de centavos al procesar transacciones en moneda extranjera.
Se aplicó la librería Decimal para evitar imprecisiones de coma flotante.

Closes #142
BREAKING CHANGE: la función calcularTotal() ahora retorna un objeto en lugar de un número.
```

---

## 6. Reglas de Oro para Escribir Buenos Commits

1. **Utiliza el imperativo**: Escribe el mensaje como si fuera una orden en presente (ej. `agregar` o `add` en lugar de `agregado` o `added`).
2. **Primera letra en minúscula**: En la descripción del tipo convencional, inicia con minúscula tras los dos puntos (`feat: agregar boton`).
3. **Sin punto final**: No coloques punto final al terminar el encabezado del commit.
4. **Sé conciso pero específico**: Mantén la primera línea por debajo de los 50-72 caracteres.
5. **Separación clara**: Si agregas un cuerpo descriptivo, déjalo separado del título por una línea en blanco.
6. **Commits atómicos**: Guarda cambios pequeños y coherentes. Un solo commit debe resolver un solo problema o agregar una sola función.
