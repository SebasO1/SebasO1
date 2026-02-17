# 🏗️ Tower Builder - Constructor de Torres

Un divertido juego de construcción de torres desarrollado con Python y Pygame. ¡Apila bloques para construir la torre más alta que puedas mientras manejas la física y la estabilidad!

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.5.0%2B-green)

## 🎮 ¿Cómo Puedo Probarlo?

### Opción 1: Inicio Rápido (Recomendado)

```bash
# 1. Navega a la carpeta del juego
cd tower_builder

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. ¡Ejecuta el juego!
python3 tower_builder.py
```

### Opción 2: Usando el Script de Inicio

```bash
cd tower_builder
chmod +x start_game.sh
./start_game.sh
```

### Opción 3: Usando Python directamente

```bash
cd tower_builder
python tower_builder.py
```

## 📋 Requisitos Previos

Antes de probar el juego, asegúrate de tener:

- **Python 3.7 o superior** instalado en tu sistema
- **pip** (gestor de paquetes de Python)
- Acceso a internet para descargar Pygame

### Verificar Python

```bash
python3 --version
# Debe mostrar: Python 3.7.x o superior
```

### Verificar pip

```bash
pip --version
# o
pip3 --version
```

## 🎯 ¿Cómo Jugar?

### Controles del Juego

- **← →** (Flechas izquierda/derecha): Mover el bloque actual
- **ESPACIO**: Soltar/colocar el bloque
- **ESC**: Volver al menú principal

### Objetivo

¡Construye la torre más alta posible apilando bloques uno encima del otro!

### Mecánicas del Juego

1. Un nuevo bloque de color aparece en la parte superior de la pantalla
2. Usa las flechas para posicionarlo
3. Presiona ESPACIO para soltar el bloque
4. El bloque cae con gravedad y se asienta cuando aterriza
5. Los bloques necesitan al menos 30% de superposición para ser estables
6. Gana puntos por cada bloque colocado, con multiplicadores de altura
7. El juego termina si un bloque cae fuera de la pantalla

### Sistema de Puntuación

- **Puntos Base**: 10 puntos por bloque
- **Multiplicador de Altura**: Aumenta cada 100 píxeles de altura de torre
- **Puntuación Final**: Puntos Base × Multiplicador de Altura

**Ejemplos:**
- A altura 0-99px: 10 puntos por bloque
- A altura 100-199px: 20 puntos por bloque
- A altura 200-299px: 30 puntos por bloque
- ¡Y así sucesivamente!

## 🏆 Consejos para Puntajes Altos

1. **Centra Tus Bloques**: Intenta mantener los bloques centrados para mejor estabilidad
2. **Observa la Superposición**: Asegura una buena superposición horizontal (al menos 30%)
3. **Construye Constantemente**: No te apresures - la colocación precisa es clave
4. **Multiplicador de Altura**: Mientras más alta tu torre, más puntos por bloque
5. **Mantén la Calma**: Tómate tu tiempo posicionando cada bloque

## 🐛 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'pygame'"

**Solución**: Instala Pygame usando pip:

```bash
pip install pygame
# o
pip3 install pygame
```

### Problema: "python3: command not found"

**Solución**: En Windows, usa `python` en lugar de `python3`:

```bash
python tower_builder.py
```

### Problema: La ventana del juego no aparece

**Solución**: 
- Asegúrate de tener un entorno gráfico (no funciona en terminales sin GUI)
- Cierra otras aplicaciones para liberar recursos del sistema
- Verifica que tu sistema tenga SDL2 instalado (generalmente viene con Pygame)

### Problema: El juego va lento

**Solución**:
- Cierra otras aplicaciones para liberar recursos del sistema
- El juego está optimizado para correr a 60 FPS en la mayoría de sistemas

### Problema: Error de permisos al ejecutar

**Solución**:

```bash
# Dale permisos de ejecución al archivo
chmod +x tower_builder.py
chmod +x start_game.sh
```

## 🧪 Probar el Código

Si eres desarrollador y quieres probar que el código funciona correctamente:

```bash
cd tower_builder
python3 test_game.py
```

Esto ejecutará 9 pruebas unitarias que verifican:
- ✓ Creación de bloques
- ✓ Física de bloques y gravedad
- ✓ Detección de colisiones
- ✓ Cálculo de superposición horizontal
- ✓ Inicialización del juego
- ✓ Funcionalidad de reinicio
- ✓ Colocación de bloques y puntuación
- ✓ Cálculo de altura de torre
- ✓ Manejo de fin de juego

**Resultado esperado**: `9 passed, 0 failed`

## 📱 Pantallas del Juego

### Menú Principal
- Muestra el título del juego e instrucciones
- Muestra el puntaje más alto
- Presiona ESPACIO para empezar

### Jugando
- Gameplay activo con apilamiento de bloques
- Visualización en tiempo real de puntaje y altura
- Muestra el puntaje más alto actual

### Fin del Juego
- Muestra puntaje final y razón por la que terminó el juego
- Muestra "¡NUEVO PUNTAJE ALTO!" si superaste tu récord
- Opciones para jugar de nuevo o volver al menú

## 🛠️ Detalles Técnicos

### Arquitectura
- **Bucle Principal del Juego**: Corre a 60 FPS para jugabilidad fluida
- **Física de Bloques**: Sistema personalizado de gravedad y detección de colisiones
- **Gestión de Estados**: Separación clara de estados de menú, jugando y fin de juego
- **Persistencia de Datos**: Puntajes altos guardados en `high_score.json`

### Física del Sistema
- Aceleración de gravedad: 0.5 píxeles/cuadro²
- Velocidad máxima de caída: 15 píxeles/cuadro
- Umbral de estabilidad: 30% de superposición horizontal requerida
- Detección de colisiones: Basada en rectángulos con cálculo de superposición

## 📝 Estructura de Archivos

```
tower_builder/
├── tower_builder.py      # Archivo principal del juego
├── requirements.txt      # Dependencias de Python
├── README.md            # Documentación en inglés
├── README_ES.md         # Esta documentación en español
├── GAME_DEMO.md         # Demo visual del juego
├── test_game.py         # Suite de pruebas
├── start_game.sh        # Script de inicio rápido
├── .gitignore           # Archivos a ignorar
└── high_score.json      # Archivo de puntaje alto (generado automáticamente)
```

## 🎓 Para Estudiantes y Desarrolladores

### Aprender del Código

Este juego es un excelente ejemplo de:
- Programación orientada a objetos en Python
- Integración con Pygame para gráficos
- Implementación de física simple
- Máquinas de estado para gestión de juegos
- Pruebas unitarias

### Modificar el Juego

Puedes personalizar el juego modificando estas constantes en `tower_builder.py`:

```python
GRAVITY = 0.5              # Ajusta la gravedad
BLOCK_WIDTH = 80           # Cambia el ancho de bloques
BLOCK_HEIGHT = 40          # Cambia la altura de bloques
MAX_BLOCKS = 50            # Máximo de bloques permitidos
FALL_SPEED_LIMIT = 15      # Velocidad máxima de caída
```

## 🌟 Características del Juego

- ✅ Gameplay simple y adictivo
- ✅ Sistema de física realista
- ✅ 6 variaciones de colores de bloques
- ✅ Seguimiento de puntaje alto persistente
- ✅ Gráficos estilo pixel limpios
- ✅ Controles intuitivos
- ✅ Estados del juego completos
- ✅ Multiplicador de puntuación basado en altura

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👨‍💻 Desarrollador

Creado por Sebastián Olaya Sánchez (SebasO1)

- 🌐 [GitHub](https://github.com/SebasO1)
- 💼 [LinkedIn](https://www.linkedin.com/in/sebastián-olaya-sánchez-639554348)

## 🎮 Inspiración del Juego

Inspirado en juegos clásicos de construcción de torres como:
- Juego de construcción de torres de Nokia
- Tower Bloxx
- Stack

---

**¡Disfruta construyendo tus torres! 🏗️🎮**

## ❓ Preguntas Frecuentes

### ¿Puedo jugar esto en Windows?

¡Sí! El juego funciona en Windows, macOS y Linux. Solo asegúrate de tener Python 3.7+ instalado.

### ¿Necesito conexión a internet para jugar?

Solo necesitas internet para instalar Pygame la primera vez. Después de eso, puedes jugar sin conexión.

### ¿Puedo compartir mi puntaje alto?

El puntaje alto se guarda localmente en tu computadora en el archivo `high_score.json`.

### ¿El juego tiene sonido?

La versión actual no incluye sonido, pero se enfoca en la jugabilidad y física.

### ¿Puedo modificar el código?

¡Por supuesto! El código está abierto para que lo explores, aprendas y modifiques.

---

**¿Más preguntas?** Abre un issue en el repositorio de GitHub o contacta al desarrollador.
