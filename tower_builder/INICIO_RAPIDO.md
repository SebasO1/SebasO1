# 🚀 Guía de Inicio Rápido - Tower Builder

## ⚡ Inicio Rápido en 3 Pasos

### Paso 1: Instalar Dependencias
```bash
cd tower_builder
pip install pygame
```

### Paso 2: Ejecutar el Juego
```bash
python3 tower_builder.py
```

### Paso 3: ¡Juega!
- Usa **← →** para mover
- Presiona **ESPACIO** para soltar
- ¡Construye la torre más alta!

---

## 🎮 Controles Rápidos

| Tecla | Acción |
|-------|--------|
| **←** | Mover bloque a la izquierda |
| **→** | Mover bloque a la derecha |
| **ESPACIO** | Soltar/colocar bloque |
| **ESC** | Volver al menú / Salir |

---

## 📊 Sistema de Puntuación

```
Puntos = 10 × (1 + altura_torre ÷ 100)
```

| Altura Torre | Puntos por Bloque |
|--------------|-------------------|
| 0-99 px      | 10 puntos         |
| 100-199 px   | 20 puntos         |
| 200-299 px   | 30 puntos         |
| 300+ px      | ¡Aún más!         |

---

## 💡 Consejos Rápidos

1. 🎯 **Centra los bloques** - Mejor estabilidad
2. 📏 **30% de superposición** - Mínimo para estabilidad
3. 🏗️ **Construye alto** - Más altura = más puntos
4. ⏱️ **No te apresures** - Precisión > Velocidad
5. 🧘 **Mantén la calma** - Un error puede terminar el juego

---

## 🐛 Problemas Comunes

### El juego no inicia
```bash
# Verifica Python
python3 --version

# Instala Pygame
pip3 install pygame
```

### Error "ModuleNotFoundError"
```bash
pip3 install -r requirements.txt
```

### En Windows, usa `python` en lugar de `python3`
```bash
python tower_builder.py
```

---

## 🧪 Probar el Código

```bash
python3 test_game.py
```

✅ Resultado esperado: `9 passed, 0 failed`

---

## 📚 Más Información

- 📖 Documentación completa: [README_ES.md](README_ES.md)
- 🇬🇧 English version: [README.md](README.md)
- 🎨 Visual demo: [GAME_DEMO.md](GAME_DEMO.md)

---

## 🆘 ¿Necesitas Ayuda?

1. Lee la documentación completa en [README_ES.md](README_ES.md)
2. Revisa la sección de solución de problemas
3. Abre un issue en GitHub
4. Contacta al desarrollador: [GitHub](https://github.com/SebasO1)

---

**¡Disfruta construyendo torres! 🏗️**
