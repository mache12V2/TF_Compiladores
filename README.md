# TP_Compiladores
UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS
FACULTAD DE INGENIERÍA

CARRERA PROFESIONAL 
DE CIENCIAS DE LA COMPUTACIÓN



Asignatura:
CC218- Teoría de Compiladores

Sección:  CC61


TRABAJO PARCIAL 

Autor
Sanchez Garay, Cesar Rafael – u202116752
Guerrero Iparraguirre, Marcelo – u202012258
Zuñiga Lovera, Angel Ruben – u202111299

Profesor
Jorge Eduardo Diaz Suarez



Lima, septiembre de 2024
Introducción
El lenguaje de programación Julia, creado en 2012 por investigadores del MIT, combina la facilidad de uso de lenguajes de alto nivel como Python y MATLAB con el rendimiento de lenguajes compilados como C y Fortran. Diseñado para la computación científica y el análisis de datos, Julia ofrece un alto rendimiento y la capacidad de manejar tareas numéricas complejas.
Sin embargo, su adopción se ve limitada por la complejidad de su sintaxis y la curva de aprendizaje que presenta. Este proyecto busca mejorar la accesibilidad de Julia a través de una gramática simplificada que reduzca la complejidad sintáctica, facilitando así la escritura de código y mejorando la experiencia de programación para investigadores y desarrolladores.

Problemática
A pesar de que Julia es conocida por su excelente rendimiento en computación científica, enfrenta desafíos significativos en términos de accesibilidad y usabilidad para investigadores y científicos. Aunque su velocidad de ejecución es comparable a la de lenguajes como C o Fortran, la complejidad de su sintaxis y su curva de aprendizaje dificultan su adopción masiva, especialmente frente a lenguajes más accesibles como R o Python Esta barrera limita su impacto en comunidades científicas que valoran tanto la rapidez como la facilidad de uso en sus herramientas. Además, aunque Julia está Compleoptimizada para alto rendimiento hay oportunidades para mejorar su backend, especialmente en el manejo de grandes volúmenes de datos y cálculos científicos complejos, lo que sigue siendo una prioridad para los investigadores que buscan un balance entre eficiencia y usabilidad.

Motivación
Este proyecto se plantea como una oportunidad para mejorar Julia, no solo en rendimiento, sino también en facilidad de uso. Al simplificar la sintaxis y mejorar la accesibilidad, esperamos que Julia sea una opción más atractiva para los investigadores que actualmente prefieren lenguajes como R o Python.

Objetivos
Desarrollar una gramática simplificada: Diseñar e implementar una nueva gramática para Julia utilizando ANTLR4 que reduzca la complejidad sintáctica, haciendo que el lenguaje sea más accesible para los investigadores.
Facilitar la escritura de código intuitivo: A través de la simplificación de la sintaxis, permite que los usuarios puedan escribir código de manera más natural y fluida, reduciendo la curva de aprendizaje y mejorando la experiencia de programación.
Reducir errores comunes en la codificación: Implementar reglas en la nueva gramática que ayuden a identificar y corregir errores comunes durante la escritura del código, aumentando así la eficiencia en el desarrollo de aplicaciones.
Realizar pruebas de usabilidad: Evaluar la efectividad de la nueva gramática mediante pruebas con investigadores y programadores, recolectando feedback para mejorar la sintaxis y asegurar que cumpla con las expectativas de facilidad de uso.
Documentar la gramática y su implementación: Crear documentación detallada que explique la nueva gramática y cómo utilizarla, facilitando su adopción por parte de la comunidad de usuarios de Julia.

Gramática
Ya que Julia es un lenguaje diseñado para la computación de alto rendimiento, su gramática debe reflejar tanto la simplicidad como la potencia que se espera de él. A continuación, se presenta la gramática en ANTLR4.
Definición de tipos de datos
Tipos básicos: La gramática debe permitir la declaración de tipos de datos fundamentales como Int (números enteros), Float (números de punto flotante), String (cadenas de texto) y Bool (valores booleanos).
Estructuras de datos: Debería incluir soporte para estructuras de datos como Array (listas), Tuple (tuplas) y Dict (diccionarios), permitiendo a los usuarios manejar colecciones de datos de manera eficiente.

Declaración de variables
Declaración de variables: Permitir la declaración de variables con o sin especificación de tipo. Por ejemplo, x = 10 o y::Float64 = 3.14.
Constantes: Incluir la palabra clave const para declarar constantes que no pueden ser reasignadas, como const PI = 3.14159.

Operadores
Operadores aritméticos: La gramática debe incluir operadores como +, -, *, / y % para realizar operaciones matemáticas básicas.
Operadores de comparación: Incluir operadores como ==, !=, <, >, <=, >= para comparar valores.
Operadores lógicos: Incluir operadores lógicos como && (AND), || (OR) y ! (NOT) para construir expresiones booleanas.

Estructuras de control
Condicionales: Permitir el uso de if, else y elseif para la toma de decisiones en el código
Bucles: Incluir for y while para iterar sobre colecciones y ejecutar bloques de código repetidamente.

Funciones
Declaración de funciones: Permitir a los usuarios declarar funciones con parámetros y valores de retorno, utilizando la sintaxis
Funciones anónimas: Soportar la creación de funciones sin nombre, conocidas como funciones lambda.

Manejo de errores
Manejo de excepciones: Incluir soporte para try, catch y finally para gestionar errores en tiempo de ejecución.

Comentarios
Comentarios de una línea: La gramática debe permitir comentarios que comienzan con #, ignorando el resto de la línea.
Comentarios multilínea: Incluir soporte para comentarios que se extienden por varias líneas usando la sintaxis #= ... =#.

Módulos y paquetes
Declaración de módulos: Permitir la creación de módulos para organizar y encapsular código utilizando la palabra clave module.
Uso de paquetes: Incluir la sintaxis para importar y utilizar paquetes con using o import.

Métodos
Definición de métodos: Soportar la definición de métodos que permiten sobrecargar funciones según los tipos de los argumentos.

Lexer: El código del lexer (JuliaSimplificadaLexer.g4) define los tokens que representan las unidades léxicas básicas del lenguaje, como palabras clave (function, if, else, etc.), operadores (+, -, *, /, etc.), literales (INT, FLOAT, STRING, BOOL) e identificadores (IDENTIFIER). También maneja espacios en blanco y comentarios, omitiéndolos para limpiar el flujo de tokens. El lexer transforma el código fuente en una secuencia de tokens que el parser utilizará para analizar la estructura sintáctica del programa.

Parser: El código del parser (JuliaSimplificadaParser.g4) utiliza los tokens proporcionados por el lexer para construir el árbol sintáctico del programa según las reglas gramaticales definidas. Estas reglas incluyen sentencias (statement), expresiones (expression), asignaciones, declaraciones de funciones, estructuras de control (como condicionales y bucles) y operaciones aritméticas y lógicas. El parser organiza estos elementos jerárquicamente, respetando la precedencia y asociatividad de los operadores, asegurando así que el código fuente sigue la sintaxis correcta del lenguaje simplificado.

Input: El archivo de entrada (input.jl) es un ejemplo de código escrito en la gramática simplificada de Julia. Contiene declaraciones de variables, una función llamada sumar, llamadas a funciones, una estructura condicional if-else y un bucle for. Este input demuestra cómo el lexer y el parser procesan un programa real, convirtiendo el código en tokens y luego en un árbol sintáctico que refleja la lógica y estructura del programa, permitiendo así su interpretación o compilación posterior.

Resultados
El proyecto culminó exitosamente con el desarrollo de una gramática simplificada para el lenguaje Julia utilizando ANTLR4, logrando reducir significativamente la complejidad sintáctica del lenguaje original y facilitando su aprendizaje y uso por parte de investigadores y desarrolladores. Se diseñó un lexer que identifica eficientemente los elementos léxicos fundamentales como palabras clave, operadores, literales e identificadores transformando el código fuente en una secuencia de tokens manejables. El parser utiliza estos tokens para construir un árbol sintáctico que representa la estructura lógica del programa, implementando reglas gramaticales que respetan la precedencia y asociatividad de los operadores, y manejan adecuadamente estructuras de control y funciones. Al procesar un código de ejemplo que incluye declaraciones de variables, funciones, estructuras condicionales y bucles, se demostró la eficacia de la gramática simplificada al generar correctamente el árbol sintáctico esperado. Las pruebas con usuarios revelaron que la nueva gramática facilita la escritura de código más intuitivo y reduce errores comunes, mejorando la experiencia de programación y posicionando a Julia como una opción más accesible y atractiva para la comunidad científica y de desarrollo.



Conclusiones
La simplificación de la gramática de Julia ha demostrado ser efectiva para mejorar su accesibilidad y usabilidad entre investigadores y científicos. Al reducir la complejidad sintáctica, el lenguaje se vuelve una opción más atractiva frente a otros lenguajes de programación utilizados en la comunidad científica. Este proyecto sienta las bases para futuras mejoras en Julia, tanto en términos de rendimiento como de facilidad de uso, y abre la puerta a una adopción más amplia en diversos campos de investigación.
Anexos
Repositorio:
Video: 

Bibliografía
Bezanson, J., Edelman, A., Karpinski, S., & Shah, V. B. (2017). Julia: A fresh approach to numerical computing. SIAM Review, 59(1), 65-98. https://julialang.org

Parr, T., & Fisher, K. (2011). LL(*): The foundation of the ANTLR parser generator. ACM SIGPLAN Notices, 46(6), 425-436. https://www.antlr.org

Bezanson, J., Karpinski, S., Shah, V. B., & Edelman, A. (2012). Julia: A fast dynamic language for technical computing. arXiv preprint arXiv:1209.5145. Disponible en: https://arxiv.org/abs/1209.5145

Perkel, J. M. (2019). Why scientists are turning to the Julia language for their next project. Nature, 572(7767), 141-142. https://doi.org/10.1038/d41586-019-02310-3

Parr, T. (2013). The Definitive ANTLR 4 Reference. The Pragmatic Bookshelf. ISBN-13: 978-1934356999.

Parr, T. (2007). Language Implementation Patterns: Create Your Own Domain-Specific and General Programming Languages. The Pragmatic Bookshelf. ISBN-13: 978-1934356456.



