# NOMBRE_DEL_PROYECTO

Este es un archivo que debe completarse con los datos utilizados en el TPI. Este archivo puede modificarse en el tiempo, no obstante siempre debe mantenerse en un estado consistente con el desarrollo.

**Importante:** Este archivo debe mantenerse en formato Markdown (.md) y sólo se tendrá en cuenta la versión disponible en GIT.

## Descripción del proyecto

El proyecto será un generador de playlists automático. Esta se basará en distintos tipos de información.
Si lo ingresado es una canción:
* El análisis de los datos de una canción base (ingresada por el usuario): Género, Artista, Popularidad, “Mood” (estado de ánimo), otros.
* El análisis de las playlists públicas de otros usuarios en donde se encuentre dicha canción
* El análisis del audio de la canción en sí: tonalidad (mayor o menor), tono, otros (opcional). 

Si lo ingresado es un artista:
* El análisis de los géneros producidos por el artista. 

Si lo ingresado es un género:
* El análisis de artistas que produzcan música de dicho género
* El análisis de géneros similares

Si lo ingresado es un estado de ánimo:
* El análisis de géneros que representen dicho estado de ánimo
* Comparación de audio de canciones reconocidas bajo dicho ánimo, en base a playlist automáticas (opcional)


## Modelo de Dominio

https://viewer.diagrams.net/?page-id=C5RBs43oDa-KdzZeNtuy&highlight=0000ff&edit=_blank&layers=1&nav=1#G1uU_qCRekmWq6l-pEqVN5Ul_ehPFLUa7U

## Bosquejo de Arquitectura

https://34u501.axshare.com/#id=7v3fzm&p=home


## Requerimientos

Definir los requerimientos del sistema.

### Funcionales

Listado y descripción breve de los requerimientos funcionales.

### No Funcionales

Listado y descripción breve de los requerimientos no funcionales. Utilizar las categorias dadas:

### Portability

**Obligatorios**

- El sistema debe funcionar correctamente en múltiples navegadores (Sólo Web).
- El sistema debe ejecutarse desde un único archivo .py llamado app.py (Sólo Escritorio).

### Security

**Obligatorios**

- Todas las contraseñas deben guardarse con encriptado criptográfico (SHA o equivalente).
- Todas los Tokens / API Keys o similares no deben exponerse de manera pública.

### Maintainability

**Obligatorios**

- El sistema debe diseñarse con la arquitectura en 3 capas. (Ver [checklist_capas.md](checklist_capas.md))
- El sistema debe utilizar control de versiones mediante GIT.
- El sistema debe estar programado en Python 3.8 o superior.

### Reliability

### Scalability

**Obligatorios**

- El sistema debe funcionar desde una ventana normal y una de incógnito de manera independiente (Sólo Web).
  - Aclaración: No se debe guardar el usuario en una variable local, deben usarse Tokens, Cookies o similares.

### Performance

**Obligatorios**

- El sistema debe funcionar en un equipo hogareño estándar.

### Reusability

### Flexibility

**Obligatorios**

- El sistema debe utilizar una base de datos SQL o NoSQL

## Stack Tecnológico

Definir que tecnologías se van a utilizar en cada capa y una breve descripción sobre por qué se escogió esa tecnologia.
https://viewer.diagrams.net/?page-id=d_5rEiqRbLu9tku_2uIN&highlight=0000ff&edit=_blank&layers=1&nav=1&page-id=d_5rEiqRbLu9tku_2uIN#G1uU_qCRekmWq6l-pEqVN5Ul_ehPFLUa7U

### Capa de Datos

Definir que base de datos, ORM y tecnologías se utilizaron y por qué.

### Capa de Negocio

Definir que librerías e integraciones con terceros se utilizaron y por qué. En caso de consumir APIs, definir cúales se usaron.
Se utilizan las librerías:
 * SpotiPy
 * Pandas (?
 * PyAudioAnalysis (si llegamos
 * Orange

También utiliza Spotify API

### Capa de Presentación

El framework utilizado es flask debido a que ninguno de los integrantes tenía experiencia con frameworks y a través de investigación y recomendaciones nos pareció lo suficientemente simple.
