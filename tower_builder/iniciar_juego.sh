#!/bin/bash
# Script de Inicio Rápido - Tower Builder Game
# Quick Start Script - Spanish Version

echo "🏗️  Tower Builder - Constructor de Torres"
echo "==========================================="
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "Por favor, instala Python 3.7 o superior"
    echo ""
    echo "Visita: https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python 3 encontrado"
PYTHON_VERSION=$(python3 --version)
echo "  Versión: $PYTHON_VERSION"

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 no está instalado"
    echo "Por favor, instala pip3"
    exit 1
fi

echo "✓ pip3 encontrado"

# Instalar dependencias
echo ""
echo "📦 Instalando dependencias..."
echo ""

pip3 install -r requirements.txt --quiet

if [ $? -ne 0 ]; then
    echo "❌ Error: Falló la instalación de dependencias"
    echo ""
    echo "Intenta manualmente con:"
    echo "  pip3 install pygame"
    exit 1
fi

echo "✓ Dependencias instaladas correctamente"
echo ""

# Información del juego
echo "==========================================="
echo "🎮 CÓMO JUGAR:"
echo "==========================================="
echo ""
echo "  Controles:"
echo "    ← → (Flechas)  : Mover bloque"
echo "    ESPACIO        : Soltar bloque"
echo "    ESC            : Volver al menú"
echo ""
echo "  Objetivo:"
echo "    ¡Construye la torre más alta posible!"
echo ""
echo "  Consejos:"
echo "    • Centra los bloques para mejor estabilidad"
echo "    • Asegura 30% de superposición mínima"
echo "    • Torres más altas = más puntos"
echo ""
echo "==========================================="
echo ""

# Ejecutar el juego
echo "🚀 Iniciando Tower Builder..."
echo ""
sleep 1

python3 tower_builder.py

# Mensaje de despedida
echo ""
echo "👋 ¡Gracias por jugar Tower Builder!"
echo ""
