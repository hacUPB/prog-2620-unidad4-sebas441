# 📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️

**Instrucciones para los estudiantes:**
1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre `AUTOEVALUACION.md`.
2. Lean cuidadosamente cada criterio de la rúbrica.
3. En el apartado **Nota Esperada**, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio.
4. En el apartado **Justificación**, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos.
5. En el apartado **Evidencia**, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con \`\`\`) que respalden su justificación.
6. Al final, calculen su nota definitiva esperada según los porcentajes.

---

## 👥 1. Información del Equipo

* **Miembro 1:** [Juan Sebastián Núñez Guzmán] - [000592683]
*

---

## 📊 2. Evaluación por Criterios

### Criterio 1: Diagrama y Lógica (Valor: 20%)
*Evalúa si el diagrama es claro, lógico y representa fielmente la estructura de datos utilizada (listas/diccionarios) y el flujo del programa.*

* **Nota Esperada (0.0 - 5.0):** 2.8 
* **Justificación:** 
  > *[de por si consideramos que merecemos una nota alta en este diagrama pero como yo no fui quien lo hizo entonces por eso creo que meresco un 2.8 y eso es lo maximo que podria pensaria yo]*
* **Evidencia:**
  *Inserta aquí la imagen de tu diagrama ![Diagrama de flujo](./Diagrama%20De%20Flujo.jpeg) pues primero creamos es un diccionario vacio y en el agregamos más diccionarios y todo lo hicimos apartir de funciones las cuales se representan por los cuadros grandes.*

### Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
*Evalúa si se utilizaron diccionarios y listas de manera correcta y anidada para almacenar los datos ingresados por el usuario, sin redundancias.*

* **Nota Esperada (0.0 - 5.0):** 3.7
* **Justificación:**
  > *[pues nosotros hicimos un diccionario vacio principal del cual salian o se daban otros diccionarios segundarios donde guardabamos las caracteristicas basicas de una aeronave además del de componentes el cual generara un diccionario terciario que por defecto estara vacio]*
* **Evidencia:**
  *Pega aquí el fragmento de código exacto donde inicializas y llenas estas estructuras. Usa el formato de código de Markdown:*
  ```python
  # Diccionario vacío.
  registro_aeronaves = {}
  # Se añade un diccionario al diccionario principal, el cual a su vez crea un elemento ("Componentes") que es un diccionario vacío.
  registro_aeronaves[nombre] = {
        "Matricula": matricula, "Modelo": modelo, "Horas de la aeronave": horas,
        "Componentes": {}
    }
  # En esta parte se puede ver como se agregan componentes a un diccionario de aeronave especifico.
  nombre = input("Ingrese la aeronave a la que desea agregar componentes: ")
    if nombre in registro_aeronaves:
        componente = input("Nombre del componente: ")
        horas_uso = float(input("Horas de uso: "))
        horas_limite = float(input("Horas límite antes de mantenimiento: "))

        registro_aeronaves[nombre]["Componentes"][componente] = {
            "Horas de uso": horas_uso,
            "Horas Limite": horas_limite
        }
´´´

### Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
*Evalúa el respeto total a las reglas: uso de ciclos clásicos (for/while), cero uso de list comprehensions, y ninguna librería/función avanzada no vista en clase.*

* **Nota Esperada (0.0 - 5.0):** 5
* **Justificación:**
    > *[pues si cumplimos con todas las reglas que yo sepa y lo que tengo entendido del codigo sip]*
* **Evidencia:** *Pega un fragmento de código que demuestre cómo iteraste sobre los datos de forma clásica (sin atajos avanzados).*

### Criterio 4: Funcionalidad del Código (Valor: 15%)
*Evalúa si el programa pide datos correctamente, no se "crashea" y genera el reporte final de mantenimiento esperado.*

* **Nota Esperada (0.0 - 5.0):** 5
* **Justificación:**
    > *[De por si el sistema funciona correctamente inicia dando las 6 opciones que le pusimos y agrega las aeronaves de manera exitosa cuando ya agregamos las 3 aeronaves simplemente es salirse del sistema con una de las opcione propuestas en el codigo y funciona sin ningun tipo de crasheo ni nada por el estilo entonces funciona de ka mejor manera]*
* **Evidencia:** *Inserta aquí 1 o 2 pantallazos (![ejecución](./img%201.jpeg) ![ejecución](./img%202.jpeg)) mostrando la terminal donde se vea:*
*El ingreso manual de datos.*
*El reporte final impreso en pantalla con las piezas que requieren mantenimiento.*

### Criterio 5: Preparación para Sustentación (Valor: 15%)
*Aunque esta nota la dará el profesor en la entrevista oral, autoevalúen su nivel de preparación y comprensión del código que entregaron.*

* **Nivel de Confianza (Bajo / Medio / Alto):** [Bajo]
* **Justificación:**
    > *[Reflexionen como equipo: Profe siendo sinceros mi compañero hizo la mayoria del trabajo y yo le ayudaba con lo poco que yo se por eso creo que mi nota no puede ser la más alta ni la misma que el porque no se todo lo que sabe el y a mi me falta mucho para saber todo lo de programación porque no se varias cosas que hasta entran en el parcial]*
* **Evidencia de preparación: pues siempre la mayoria de veces lo haciamos juntos pero el era el que programaba y yo solo si no sabia preguntaba y trataba de apoyarlo en lo que sabia nada más **

### 📈 3. Cálculo de Nota Definitiva Esperada
Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.

|Criterio	|Nota |Asignada	|Peso	|Subtotal |(Nota * Peso) |
|---|---|---|---|---|---|
|1. Diagrama y Lógica	|[2.8]	|20% |(0.2)	|[0.56]|
|2. Uso de Estructuras	|[3.7]	|30% |(0.3)	|[1.11]|
|3. Cumplimiento Restricciones|	[5]	|20% |(0.2)	|[1]|
|4. Funcionalidad	|[5]	|15% |(0.15)	|[0.75]|
|5. Sustentación (Estimado)|	[2.5]|	15%| (0.15)|	[0.375]|

NOTA FINAL ESPERADA		100%	[SUMA TOTAL]

✨ ""La educación es para el carácter, no solo para la mente"." ✨