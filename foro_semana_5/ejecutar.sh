#!/bin/bash

# Script de ejecución rápida para Foro Semana 5
# Computación Bioinspirada - NRC-3333

echo "🧬 FORO SEMANA 5: Algoritmo Evolutivo para Análisis Genómico"
echo "=============================================================="
echo ""
echo "Participantes:"
echo "  • Jessica Silva (ID: 000918680)"
echo "  • Leonardo Mosquera (ID: 000922268)"
echo ""
echo "=============================================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "main_foro_semana_5.py" ]; then
    echo "❌ Error: Ejecute este script desde el directorio foro_semana_5/"
    exit 1
fi

# Verificar instalación de Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    exit 1
fi

echo "📦 Verificando dependencias..."
pip3 install -q -r requirements.txt

echo "✅ Dependencias instaladas"
echo ""
echo "🚀 Ejecutando análisis completo..."
echo ""

# Ejecutar script principal
python3 main_foro_semana_5.py

echo ""
echo "=============================================================="
echo "✅ FORO SEMANA 5 COMPLETADO"
echo "=============================================================="
echo ""
echo "📁 Archivos generados:"
echo "  ✓ foro_semana_5_participaciones.md"
echo "  ✓ reporte_tecnico_detallado.md"
echo "  ✓ analisis_comparativo_completo.png"
echo "  ✓ infografia_ejecutiva.png"
echo ""
echo "🎯 Revisar archivos generados para respuestas del foro"
echo ""
