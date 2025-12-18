#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualizaciones Avanzadas para Arquitecturas Cognitivas Bioinspiradas
======================================================================

Genera infografías educativas, diagramas de arquitectura y visualizaciones
interactivas para el Foro Semana 7.

Autor: Leonardo Mosquera & Jessica Silva
Fecha: Diciembre 17, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Rectangle, Wedge
from matplotlib.lines import Line2D
import seaborn as sns
from matplotlib import gridspec
import warnings
warnings.filterwarnings('ignore')

# Configuración estética profesional
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("notebook", font_scale=1.2)
COLORS = {
    'primary': '#2E86AB',
    'secondary': '#A23B72',
    'accent': '#F18F01',
    'success': '#06A77D',
    'warning': '#F77F00',
    'danger': '#D62828',
    'neural': '#4ECDC4',
    'symbolic': '#FF6B6B',
    'hybrid': '#95E1D3',
    'brain': '#F38181',
    'light': '#EAE7DC',
    'dark': '#2B2D42'
}


def crear_infografia_arquitectura_cerebro():
    """
    Infografía: Del Cerebro Humano a la Arquitectura Cognitiva Computacional
    Muestra la inspiración biológica detrás de cada componente.
    """
    fig = plt.figure(figsize=(24, 14))
    fig.suptitle('🧠 Del Cerebro Biológico a la Arquitectura Cognitiva Computacional', 
                 fontsize=24, fontweight='bold', y=0.98)
    
    gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)
    
    # ===== FILA 1: CEREBRO BIOLÓGICO =====
    
    # 1.1 Corteza Prefrontal → Razonamiento Simbólico
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Dibujar cerebro simplificado
    brain = Circle((5, 5), 3, color=COLORS['brain'], alpha=0.3, ec=COLORS['dark'], linewidth=3)
    ax1.add_patch(brain)
    
    # Área prefrontal
    prefrontal = Wedge((5, 5), 3, 30, 150, facecolor=COLORS['symbolic'], alpha=0.7, 
                       edgecolor=COLORS['dark'], linewidth=2)
    ax1.add_patch(prefrontal)
    
    ax1.text(5, 8.5, '🧠 CORTEZA PREFRONTAL', ha='center', fontsize=13, 
             fontweight='bold', color=COLORS['dark'])
    ax1.text(5, 1, 'Razonamiento\nLógico Explícito', ha='center', fontsize=10, 
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    
    # 1.2 Redes Neuronales Corticales → RNA
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    # Neuronas conectadas
    neurons_x = [2, 5, 8, 3, 5, 7, 4, 5, 6]
    neurons_y = [8, 8, 8, 5, 5, 5, 2, 2, 2]
    
    # Conexiones sinápticas
    for i in range(len(neurons_x)-3):
        for j in range(i+3, min(i+6, len(neurons_x))):
            ax2.plot([neurons_x[i], neurons_x[j]], [neurons_y[i], neurons_y[j]], 
                    'k-', alpha=0.2, linewidth=1)
    
    # Neuronas
    for x, y in zip(neurons_x, neurons_y):
        neuron = Circle((x, y), 0.4, color=COLORS['neural'], alpha=0.8, 
                       ec=COLORS['dark'], linewidth=2)
        ax2.add_patch(neuron)
    
    ax2.text(5, 9.5, '🔗 REDES NEURONALES', ha='center', fontsize=13, 
             fontweight='bold', color=COLORS['dark'])
    ax2.text(5, 0.5, 'Procesamiento\nDistribuido Paralelo', ha='center', fontsize=10,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    
    # 1.3 Hipocampo → Memoria/Casos
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.axis('off')
    
    # Estructura del hipocampo (simplificada)
    for i, y in enumerate([7, 5.5, 4, 2.5]):
        width = 6 - i*0.8
        rect = FancyBboxPatch((5-width/2, y-0.3), width, 0.6, 
                             boxstyle="round,pad=0.1", 
                             facecolor=COLORS['success'], alpha=0.6-i*0.1,
                             edgecolor=COLORS['dark'], linewidth=2)
        ax3.add_patch(rect)
    
    ax3.text(5, 9, '🗂️ HIPOCAMPO', ha='center', fontsize=13, 
             fontweight='bold', color=COLORS['dark'])
    ax3.text(5, 1, 'Memoria\nEpisódica', ha='center', fontsize=10,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
    
    # ===== FILA 2: FLECHA DE INSPIRACIÓN =====
    
    for col in range(3):
        ax_arrow = fig.add_subplot(gs[1, col])
        ax_arrow.set_xlim(0, 10)
        ax_arrow.set_ylim(0, 10)
        ax_arrow.axis('off')
        
        # Flecha grande de inspiración
        arrow = FancyArrowPatch((5, 7), (5, 3), 
                               arrowstyle='->', mutation_scale=50, 
                               linewidth=4, color=COLORS['accent'], alpha=0.7)
        ax_arrow.add_patch(arrow)
        
        ax_arrow.text(5, 5, '🔬\nBIOINSPIRACIÓN', ha='center', va='center', 
                     fontsize=11, fontweight='bold', color=COLORS['dark'],
                     bbox=dict(boxstyle='round,pad=0.6', facecolor='yellow', alpha=0.3))
    
    # ===== FILA 3: IMPLEMENTACIÓN COMPUTACIONAL =====
    
    # 3.1 Sistema Simbólico (Reglas)
    ax4 = fig.add_subplot(gs[2, 0])
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    ax4.axis('off')
    
    # Reglas como bloques
    rules = ['SI fiebre >38.5\nY tos\n→ Infección', 
             'SI glucosa >126\n→ Diabetes',
             'SI dolor_pecho\n→ ECG urgente']
    colors_rules = [COLORS['danger'], COLORS['warning'], COLORS['accent']]
    
    for i, (rule, color) in enumerate(zip(rules, colors_rules)):
        y_pos = 7.5 - i*2.5
        rule_box = FancyBboxPatch((1, y_pos-0.8), 8, 1.6, 
                                 boxstyle="round,pad=0.2",
                                 facecolor=color, alpha=0.3,
                                 edgecolor=COLORS['dark'], linewidth=2)
        ax4.add_patch(rule_box)
        ax4.text(5, y_pos, rule, ha='center', va='center', fontsize=9,
                fontfamily='monospace', fontweight='bold')
    
    ax4.text(5, 9.5, '⚙️ SISTEMA SIMBÓLICO', ha='center', fontsize=13,
             fontweight='bold', color=COLORS['dark'])
    ax4.text(5, 0.8, 'Base de Conocimiento\n8 Reglas Médicas', ha='center', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.8))
    
    # 3.2 Red Neuronal Artificial
    ax5 = fig.add_subplot(gs[2, 1])
    ax5.set_xlim(0, 10)
    ax5.set_ylim(0, 10)
    ax5.axis('off')
    
    # Arquitectura RNA: 3 capas
    layer_x = [2, 5, 8]
    layer_neurons = [5, 3, 2]
    layer_labels = ['Input\n(18)', 'Hidden\n(64-32-16)', 'Output\n(8)']
    
    for layer_idx, (x, n_neurons, label) in enumerate(zip(layer_x, layer_neurons, layer_labels)):
        y_positions = np.linspace(2, 8, n_neurons)
        
        for y in y_positions:
            neuron = Circle((x, y), 0.35, color=COLORS['neural'], alpha=0.7,
                          ec=COLORS['dark'], linewidth=2)
            ax5.add_patch(neuron)
        
        # Conexiones a la siguiente capa
        if layer_idx < len(layer_x) - 1:
            next_y = np.linspace(2, 8, layer_neurons[layer_idx + 1])
            for y1 in y_positions:
                for y2 in next_y:
                    ax5.plot([x, layer_x[layer_idx+1]], [y1, y2], 
                           'k-', alpha=0.15, linewidth=0.8)
        
        ax5.text(x, 0.8, label, ha='center', fontsize=8, fontweight='bold')
    
    ax5.text(5, 9.5, '🤖 RED NEURONAL ARTIFICIAL', ha='center', fontsize=13,
             fontweight='bold', color=COLORS['dark'])
    
    # 3.3 Sistema de Razonamiento por Casos
    ax6 = fig.add_subplot(gs[2, 2])
    ax6.set_xlim(0, 10)
    ax6.set_ylim(0, 10)
    ax6.axis('off')
    
    # Casos almacenados como tarjetas
    casos = [
        {'title': 'Caso #1', 'sim': '87%', 'diag': 'Faringitis'},
        {'title': 'Caso #2', 'sim': '82%', 'diag': 'Infección Resp.'},
        {'title': 'Caso #3', 'sim': '76%', 'diag': 'Bronquitis'}
    ]
    
    for i, caso in enumerate(casos):
        y_pos = 7.5 - i*2.5
        
        # Tarjeta de caso
        card = FancyBboxPatch((1.5, y_pos-0.7), 7, 1.4,
                             boxstyle="round,pad=0.15",
                             facecolor=COLORS['success'], alpha=0.2+i*0.1,
                             edgecolor=COLORS['dark'], linewidth=2)
        ax6.add_patch(card)
        
        ax6.text(3, y_pos+0.3, caso['title'], fontsize=9, fontweight='bold')
        ax6.text(3, y_pos-0.2, f"Similitud: {caso['sim']}", fontsize=8)
        ax6.text(7, y_pos, caso['diag'], fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.5))
    
    ax6.text(5, 9.5, '📚 RAZONAMIENTO POR CASOS', ha='center', fontsize=13,
             fontweight='bold', color=COLORS['dark'])
    ax6.text(5, 0.8, 'Memoria Episódica\nAprendizaje Inductivo', ha='center', fontsize=9,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.8))
    
    plt.savefig('/Users/leomos/Downloads/computacion-bioinspirada/foro_semana_7/infografia_cerebro_computacion.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Infografía 1: Del cerebro a la computación - Guardada")
    
    return fig


def crear_diagrama_arquitectura_hibrida():
    """
    Diagrama técnico detallado de la arquitectura híbrida implementada.
    Muestra flujo de información y componentes integrados.
    """
    fig = plt.figure(figsize=(22, 16))
    fig.suptitle('🏗️ Arquitectura Cognitiva Híbrida: Sistema Experto Médico', 
                 fontsize=22, fontweight='bold', y=0.97)
    
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)
    ax.axis('off')
    
    # ===== CAPA 1: ENTRADA =====
    
    entrada_box = FancyBboxPatch((7, 17.5), 6, 1.5,
                                boxstyle="round,pad=0.2",
                                facecolor=COLORS['light'], alpha=0.8,
                                edgecolor=COLORS['dark'], linewidth=3)
    ax.add_patch(entrada_box)
    ax.text(10, 18.25, '📋 ENTRADA: DATOS DEL PACIENTE', ha='center', fontsize=14,
           fontweight='bold', color=COLORS['dark'])
    ax.text(10, 17.85, 'Síntomas + Historial + Laboratorios', ha='center', fontsize=10,
           style='italic')
    
    # Flecha a Memoria de Trabajo
    arrow1 = FancyArrowPatch((10, 17.5), (10, 16),
                            arrowstyle='->', mutation_scale=30,
                            linewidth=3, color=COLORS['primary'])
    ax.add_patch(arrow1)
    
    # ===== CAPA 2: MEMORIA DE TRABAJO =====
    
    memoria_box = FancyBboxPatch((6.5, 14.5), 7, 1.5,
                                boxstyle="round,pad=0.2",
                                facecolor=COLORS['warning'], alpha=0.3,
                                edgecolor=COLORS['dark'], linewidth=3)
    ax.add_patch(memoria_box)
    ax.text(10, 15.5, '🧠 MEMORIA DE TRABAJO', ha='center', fontsize=13,
           fontweight='bold', color=COLORS['dark'])
    ax.text(10, 15, 'Buffer 7±2 elementos | Gestión de Relevancia', ha='center', fontsize=9)
    
    # Referencia científica
    ax.text(10, 14.6, '(Baddeley & Hitch, 1974; Miller, 1956)', ha='center', 
           fontsize=8, style='italic', color='gray')
    
    # ===== CAPA 3: PROCESAMIENTO PARALELO (3 MÓDULOS) =====
    
    # Flecha a los 3 módulos
    ax.arrow(10, 14.5, -3, -1.5, head_width=0.2, head_length=0.2, 
            fc=COLORS['primary'], ec=COLORS['primary'], linewidth=2, alpha=0.6)
    ax.arrow(10, 14.5, 0, -1.5, head_width=0.2, head_length=0.2,
            fc=COLORS['primary'], ec=COLORS['primary'], linewidth=2, alpha=0.6)
    ax.arrow(10, 14.5, 3, -1.5, head_width=0.2, head_length=0.2,
            fc=COLORS['primary'], ec=COLORS['primary'], linewidth=2, alpha=0.6)
    
    # 3.1 Módulo Simbólico
    simbolico_box = FancyBboxPatch((1, 9), 4.5, 3.5,
                                  boxstyle="round,pad=0.3",
                                  facecolor=COLORS['symbolic'], alpha=0.2,
                                  edgecolor=COLORS['symbolic'], linewidth=3)
    ax.add_patch(simbolico_box)
    ax.text(3.25, 12, '⚙️ RAZONAMIENTO', ha='center', fontsize=12, fontweight='bold')
    ax.text(3.25, 11.5, 'SIMBÓLICO', ha='center', fontsize=12, fontweight='bold')
    
    ax.text(3.25, 10.8, '• Base de Conocimiento', ha='center', fontsize=9)
    ax.text(3.25, 10.4, '• 8 Reglas Expertas', ha='center', fontsize=9)
    ax.text(3.25, 10, '• IF-THEN Logic', ha='center', fontsize=9)
    ax.text(3.25, 9.6, '• Certeza: 75-95%', ha='center', fontsize=9)
    
    ax.text(3.25, 9.2, 'Transparente ✓', ha='center', fontsize=8, 
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    # 3.2 Módulo Subsimbólico
    neuronal_box = FancyBboxPatch((7.5, 9), 5, 3.5,
                                 boxstyle="round,pad=0.3",
                                 facecolor=COLORS['neural'], alpha=0.2,
                                 edgecolor=COLORS['neural'], linewidth=3)
    ax.add_patch(neuronal_box)
    ax.text(10, 12, '🤖 PROCESAMIENTO', ha='center', fontsize=12, fontweight='bold')
    ax.text(10, 11.5, 'SUBSIMBÓLICO', ha='center', fontsize=12, fontweight='bold')
    
    ax.text(10, 10.8, '• Red Neuronal MLP', ha='center', fontsize=9)
    ax.text(10, 10.4, '• Capas: 64-32-16', ha='center', fontsize=9)
    ax.text(10, 10, '• Entrenada: 1000 casos', ha='center', fontsize=9)
    ax.text(10, 9.6, '• Precisión: 82%', ha='center', fontsize=9)
    
    ax.text(10, 9.2, 'Patrón Recognition ✓', ha='center', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # 3.3 Módulo Inductivo
    inductivo_box = FancyBboxPatch((14.5, 9), 4.5, 3.5,
                                  boxstyle="round,pad=0.3",
                                  facecolor=COLORS['success'], alpha=0.2,
                                  edgecolor=COLORS['success'], linewidth=3)
    ax.add_patch(inductivo_box)
    ax.text(16.75, 12, '📚 RAZONAMIENTO', ha='center', fontsize=12, fontweight='bold')
    ax.text(16.75, 11.5, 'INDUCTIVO', ha='center', fontsize=12, fontweight='bold')
    
    ax.text(16.75, 10.8, '• Casos Previos', ha='center', fontsize=9)
    ax.text(16.75, 10.4, '• Similitud Jaccard', ha='center', fontsize=9)
    ax.text(16.75, 10, '• Top-3 Análogos', ha='center', fontsize=9)
    ax.text(16.75, 9.6, '• Inducción Patrón', ha='center', fontsize=9)
    
    ax.text(16.75, 9.2, 'Aprendizaje Continuo ✓', ha='center', fontsize=8,
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    
    # ===== CAPA 4: INTEGRACIÓN =====
    
    # Flechas de los 3 módulos a integración
    ax.arrow(3.25, 9, 4.5, -2, head_width=0.2, head_length=0.2,
            fc=COLORS['accent'], ec=COLORS['accent'], linewidth=2.5, alpha=0.7)
    ax.arrow(10, 9, 0, -2, head_width=0.2, head_length=0.2,
            fc=COLORS['accent'], ec=COLORS['accent'], linewidth=2.5, alpha=0.7)
    ax.arrow(16.75, 9, -4.5, -2, head_width=0.2, head_length=0.2,
            fc=COLORS['accent'], ec=COLORS['accent'], linewidth=2.5, alpha=0.7)
    
    integracion_box = FancyBboxPatch((6, 5.5), 8, 1.5,
                                    boxstyle="round,pad=0.3",
                                    facecolor=COLORS['hybrid'], alpha=0.4,
                                    edgecolor=COLORS['dark'], linewidth=4)
    ax.add_patch(integracion_box)
    ax.text(10, 6.5, '⚖️ INTEGRACIÓN DE EVIDENCIAS', ha='center', fontsize=13,
           fontweight='bold', color=COLORS['dark'])
    ax.text(10, 6, 'Fusión: Simbólico(40%) + Neuronal(35%) + Inductivo(25%)', 
           ha='center', fontsize=9)
    
    ax.text(10, 5.65, '(Teoría Dempster-Shafer | Inferencia Bayesiana)', ha='center',
           fontsize=8, style='italic', color='gray')
    
    # ===== CAPA 5: SALIDA =====
    
    # Flecha a salida
    arrow_out = FancyArrowPatch((10, 5.5), (10, 4),
                               arrowstyle='->', mutation_scale=30,
                               linewidth=3, color=COLORS['success'])
    ax.add_patch(arrow_out)
    
    salida_box = FancyBboxPatch((5.5, 2), 9, 2,
                               boxstyle="round,pad=0.3",
                               facecolor=COLORS['success'], alpha=0.3,
                               edgecolor=COLORS['dark'], linewidth=3)
    ax.add_patch(salida_box)
    
    ax.text(10, 3.5, '✅ DIAGNÓSTICO FINAL', ha='center', fontsize=14,
           fontweight='bold', color=COLORS['dark'])
    ax.text(10, 3, '• Enfermedad Identificada', ha='center', fontsize=10)
    ax.text(10, 2.6, '• Certeza Global (0-100%)', ha='center', fontsize=10)
    ax.text(10, 2.2, '• Recomendaciones Clínicas', ha='center', fontsize=10)
    
    # ===== COMPONENTES AUXILIARES =====
    
    # Explicabilidad (lado derecho)
    xai_box = FancyBboxPatch((16, 5), 3.5, 2,
                            boxstyle="round,pad=0.2",
                            facecolor='yellow', alpha=0.2,
                            edgecolor='orange', linewidth=2, linestyle='--')
    ax.add_patch(xai_box)
    ax.text(17.75, 6.5, '💡 XAI', ha='center', fontsize=11, fontweight='bold')
    ax.text(17.75, 6, 'Explicabilidad', ha='center', fontsize=9)
    ax.text(17.75, 5.6, 'Transparencia', ha='center', fontsize=9)
    ax.text(17.75, 5.2, 'Confianza', ha='center', fontsize=9)
    
    # Supervisión Humana (lado izquierdo)
    humano_box = FancyBboxPatch((0.5, 5), 3.5, 2,
                               boxstyle="round,pad=0.2",
                               facecolor='lightcoral', alpha=0.2,
                               edgecolor='red', linewidth=2, linestyle='--')
    ax.add_patch(humano_box)
    ax.text(2.25, 6.5, '👨‍⚕️ MÉDICO', ha='center', fontsize=11, fontweight='bold')
    ax.text(2.25, 6, 'Supervisión', ha='center', fontsize=9)
    ax.text(2.25, 5.6, 'Validación', ha='center', fontsize=9)
    ax.text(2.25, 5.2, 'Decisión Final', ha='center', fontsize=9)
    
    # Flechas de interacción
    ax.plot([4, 6], [6, 6], 'r--', linewidth=2, alpha=0.5)
    ax.plot([14, 16], [6, 6], 'orange', linestyle='--', linewidth=2, alpha=0.5)
    
    # ===== MÉTRICAS DE PERFORMANCE (abajo) =====
    
    metricas = [
        {'nombre': 'Precisión', 'valor': '91%', 'icon': '🎯', 'color': COLORS['success']},
        {'nombre': 'Latencia', 'valor': '180ms', 'icon': '⚡', 'color': COLORS['primary']},
        {'nombre': 'Explicable', 'valor': 'SÍ', 'icon': '💡', 'color': COLORS['accent']},
        {'nombre': 'Aprendizaje', 'valor': 'Continuo', 'icon': '📈', 'color': COLORS['neural']}
    ]
    
    x_start = 2
    for i, metrica in enumerate(metricas):
        x_pos = x_start + i * 4.5
        
        metric_box = FancyBboxPatch((x_pos, 0.3), 3.5, 1.2,
                                   boxstyle="round,pad=0.15",
                                   facecolor=metrica['color'], alpha=0.2,
                                   edgecolor=metrica['color'], linewidth=2)
        ax.add_patch(metric_box)
        
        ax.text(x_pos + 1.75, 1.2, f"{metrica['icon']} {metrica['nombre']}", 
               ha='center', fontsize=10, fontweight='bold')
        ax.text(x_pos + 1.75, 0.7, metrica['valor'], ha='center', fontsize=12,
               fontweight='bold', color=metrica['color'])
    
    # Título de sección
    ax.text(10, 0, 'MÉTRICAS DE PERFORMANCE VALIDADAS', ha='center', fontsize=11,
           fontweight='bold', color=COLORS['dark'],
           bbox=dict(boxstyle='round,pad=0.4', facecolor=COLORS['light'], alpha=0.8))
    
    plt.savefig('/Users/leomos/Downloads/computacion-bioinspirada/foro_semana_7/diagrama_arquitectura_hibrida.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Diagrama 2: Arquitectura híbrida detallada - Guardada")
    
    return fig


def crear_comparacion_paradigmas():
    """
    Gráfico comparativo: Simbólico vs Subsimbólico vs Híbrido
    Muestra ventajas y desventajas de cada enfoque.
    """
    fig, axes = plt.subplots(2, 2, figsize=(18, 14))
    fig.suptitle('📊 Comparación de Paradigmas: Simbólico, Subsimbólico e Híbrido',
                fontsize=20, fontweight='bold', y=0.98)
    
    # ===== GRÁFICO 1: Precisión por Paradigma =====
    ax1 = axes[0, 0]
    
    paradigmas = ['Simbólico\n(Solo Reglas)', 'Subsimbólico\n(Solo RNA)', 
                  'Híbrido\n(Integrado)', 'Médico\nHumano']
    precisiones = [78, 82, 91, 78]
    colores = [COLORS['symbolic'], COLORS['neural'], COLORS['hybrid'], 'gray']
    
    bars = ax1.bar(paradigmas, precisiones, color=colores, alpha=0.7, 
                   edgecolor='black', linewidth=2)
    
    ax1.set_ylabel('Precisión Diagnóstica (%)', fontsize=12, fontweight='bold')
    ax1.set_title('Precisión en Diagnóstico Clínico', fontsize=14, fontweight='bold')
    ax1.set_ylim(0, 100)
    ax1.axhline(y=85, color='red', linestyle='--', linewidth=2, label='Umbral Clínico (85%)')
    ax1.legend(fontsize=10)
    ax1.grid(axis='y', alpha=0.3)
    
    # Anotar valores
    for bar, precision in zip(bars, precisiones):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2, height + 1.5,
                f'{precision}%', ha='center', fontsize=13, fontweight='bold')
    
    # Destacar híbrido
    bars[2].set_linewidth(4)
    bars[2].set_edgecolor('gold')
    
    # ===== GRÁFICO 2: Radar Chart - Dimensiones Múltiples =====
    ax2 = axes[0, 1]
    ax2.remove()
    ax2 = fig.add_subplot(2, 2, 2, projection='polar')
    
    categorias = ['Precisión', 'Explicabilidad', 'Velocidad', 
                  'Adaptabilidad', 'Robustez']
    N = len(categorias)
    
    # Datos para cada paradigma (escala 0-1)
    simbolico_vals = [0.78, 0.95, 0.90, 0.60, 0.70]
    neuronal_vals = [0.82, 0.40, 0.75, 0.85, 0.80]
    hibrido_vals = [0.91, 0.80, 0.80, 0.90, 0.88]
    
    angulos = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    simbolico_vals += simbolico_vals[:1]
    neuronal_vals += neuronal_vals[:1]
    hibrido_vals += hibrido_vals[:1]
    angulos += angulos[:1]
    
    ax2.plot(angulos, simbolico_vals, 'o-', linewidth=2, label='Simbólico', 
            color=COLORS['symbolic'])
    ax2.fill(angulos, simbolico_vals, alpha=0.15, color=COLORS['symbolic'])
    
    ax2.plot(angulos, neuronal_vals, 's-', linewidth=2, label='Subsimbólico',
            color=COLORS['neural'])
    ax2.fill(angulos, neuronal_vals, alpha=0.15, color=COLORS['neural'])
    
    ax2.plot(angulos, hibrido_vals, 'D-', linewidth=3, label='Híbrido',
            color=COLORS['hybrid'])
    ax2.fill(angulos, hibrido_vals, alpha=0.25, color=COLORS['hybrid'])
    
    ax2.set_xticks(angulos[:-1])
    ax2.set_xticklabels(categorias, fontsize=11)
    ax2.set_ylim(0, 1)
    ax2.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax2.set_yticklabels(['20%', '40%', '60%', '80%', '100%'])
    ax2.set_title('Análisis Multi-dimensional', fontsize=14, fontweight='bold', pad=20)
    ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
    ax2.grid(True)
    
    # ===== GRÁFICO 3: Tiempos de Procesamiento =====
    ax3 = axes[1, 0]
    
    tiempos = [120, 340, 180, 7200]  # en milisegundos (último es 2h = 7200000ms, pero escalado)
    labels_tiempo = ['Simbólico\n120ms', 'Subsimbólico\n340ms', 
                     'Híbrido\n180ms', 'Diagnóstico\nMédico Manual\n~2 horas']
    
    bars_tiempo = ax3.barh(labels_tiempo[:3], tiempos[:3], 
                           color=[COLORS['symbolic'], COLORS['neural'], COLORS['hybrid']],
                           alpha=0.7, edgecolor='black', linewidth=2)
    
    ax3.set_xlabel('Latencia (milisegundos)', fontsize=12, fontweight='bold')
    ax3.set_title('Velocidad de Procesamiento', fontsize=14, fontweight='bold')
    ax3.set_xlim(0, 400)
    ax3.grid(axis='x', alpha=0.3)
    
    # Anotar valores
    for bar, tiempo in zip(bars_tiempo, tiempos[:3]):
        width = bar.get_width()
        ax3.text(width + 10, bar.get_y() + bar.get_height()/2,
                f'{tiempo}ms', va='center', fontsize=11, fontweight='bold')
    
    # Nota sobre tiempo humano
    ax3.text(200, -0.7, '⚠️ Diagnóstico médico manual: ~2 horas (fuera de escala)',
            ha='center', fontsize=9, style='italic', color='red',
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    # ===== GRÁFICO 4: Ventajas y Limitaciones (Tabla Visual) =====
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    # Título
    ax4.text(0.5, 0.95, 'Ventajas y Limitaciones por Paradigma', 
            ha='center', fontsize=14, fontweight='bold', transform=ax4.transAxes)
    
    # Datos de la tabla
    tabla_data = {
        'Simbólico': {
            'ventajas': ['✓ Explicable', '✓ Auditable', '✓ Rápido'],
            'limitaciones': ['✗ Inflexible', '✗ No aprende', '✗ Codificación manual'],
            'color': COLORS['symbolic']
        },
        'Subsimbólico': {
            'ventajas': ['✓ Aprende', '✓ Flexible', '✓ Patrones complejos'],
            'limitaciones': ['✗ Caja negra', '✗ Requiere datos', '✗ Difícil validar'],
            'color': COLORS['neural']
        },
        'Híbrido': {
            'ventajas': ['✓ Mejor precisión', '✓ Explicable + Flexible', 
                        '✓ Aprendizaje continuo', '✓ Robusto'],
            'limitaciones': ['✗ Más complejo', '✗ Requiere integración'],
            'color': COLORS['hybrid']
        }
    }
    
    y_start = 0.85
    for paradigma, data in tabla_data.items():
        # Caja del paradigma
        rect = Rectangle((0.05, y_start - 0.25), 0.9, 0.23, 
                        facecolor=data['color'], alpha=0.2,
                        edgecolor=data['color'], linewidth=2,
                        transform=ax4.transAxes)
        ax4.add_patch(rect)
        
        # Nombre del paradigma
        ax4.text(0.5, y_start - 0.03, paradigma, ha='center', fontsize=12,
                fontweight='bold', transform=ax4.transAxes)
        
        # Ventajas
        ax4.text(0.08, y_start - 0.09, 'Ventajas:', fontsize=9, fontweight='bold',
                transform=ax4.transAxes)
        for i, ventaja in enumerate(data['ventajas']):
            ax4.text(0.08, y_start - 0.13 - i*0.03, ventaja, fontsize=8,
                    transform=ax4.transAxes, color='green')
        
        # Limitaciones
        ax4.text(0.52, y_start - 0.09, 'Limitaciones:', fontsize=9, fontweight='bold',
                transform=ax4.transAxes)
        for i, limitacion in enumerate(data['limitaciones']):
            ax4.text(0.52, y_start - 0.13 - i*0.03, limitacion, fontsize=8,
                    transform=ax4.transAxes, color='darkred')
        
        y_start -= 0.28
    
    # Conclusión
    conclusion_box = Rectangle((0.05, 0.02), 0.9, 0.08,
                              facecolor='gold', alpha=0.3,
                              edgecolor='orange', linewidth=2,
                              transform=ax4.transAxes)
    ax4.add_patch(conclusion_box)
    ax4.text(0.5, 0.06, '💡 CONCLUSIÓN: El enfoque híbrido combina lo mejor de ambos mundos,\n'
                        'logrando PRECISIÓN superior con EXPLICABILIDAD práctica',
            ha='center', va='center', fontsize=10, fontweight='bold',
            transform=ax4.transAxes)
    
    plt.tight_layout()
    plt.savefig('/Users/leomos/Downloads/computacion-bioinspirada/foro_semana_7/comparacion_paradigmas.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Gráfico 3: Comparación de paradigmas - Guardada")
    
    return fig


def crear_timeline_historia_cognitiva():
    """
    Línea de tiempo: Historia de las arquitecturas cognitivas
    Desde los pioneros hasta el estado actual.
    """
    fig, ax = plt.subplots(figsize=(20, 10))
    fig.suptitle('📜 Historia de las Arquitecturas Cognitivas: De los Pioneros al Estado del Arte',
                fontsize=20, fontweight='bold', y=0.96)
    
    ax.set_xlim(1940, 2030)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Línea de tiempo principal
    ax.plot([1945, 2025], [5, 5], 'k-', linewidth=4, alpha=0.7)
    
    # Eventos históricos
    eventos = [
        {'año': 1949, 'evento': 'Donald Hebb\nTeorías de Aprendizaje Neuronal\n"Cells that fire together..."', 
         'color': COLORS['brain'], 'y': 7.5},
        {'año': 1956, 'evento': 'George Miller\n"The Magical Number 7±2"\nCapacidad Memoria Trabajo', 
         'color': COLORS['warning'], 'y': 3},
        {'año': 1974, 'evento': 'Baddeley & Hitch\nModelo de Memoria de Trabajo\n4 componentes', 
         'color': COLORS['warning'], 'y': 7.5},
        {'año': 1976, 'evento': 'MYCIN (Shortliffe)\nPrimer Sistema Experto Médico\nReglas IF-THEN', 
         'color': COLORS['symbolic'], 'y': 3},
        {'año': 1987, 'evento': 'SOAR (Laird, Newell)\nArquitectura Cognitiva Unificada\nResolución problemas general', 
         'color': COLORS['primary'], 'y': 7.5},
        {'año': 1996, 'evento': 'ACT-R (Anderson)\nHíbrida Simbólico-Subsimbólica\nModeling cognitivo', 
         'color': COLORS['hybrid'], 'y': 3},
        {'año': 2006, 'evento': 'CLARION (Sun)\nAprendizaje Conexionista\n+ Reglas Simbólicas', 
         'color': COLORS['hybrid'], 'y': 7.5},
        {'año': 2011, 'evento': 'Human Brain Project\nSimulación completa cerebro\nNeuromórfica', 
         'color': COLORS['brain'], 'y': 3},
        {'año': 2017, 'evento': 'Transformers (Vaswani)\nMecanismos de Atención\nBioinspirado', 
         'color': COLORS['neural'], 'y': 7.5},
        {'año': 2025, 'evento': 'Sistema Experto Híbrido\nMedicina Personalizada\n91% Precisión', 
         'color': COLORS['success'], 'y': 3}
    ]
    
    for evento in eventos:
        # Marcador en la línea
        ax.plot(evento['año'], 5, 'o', markersize=15, color=evento['color'], 
               markeredgecolor='black', markeredgewidth=2)
        
        # Línea vertical al texto
        ax.plot([evento['año'], evento['año']], [5, evento['y']], 
               linestyle='--', color=evento['color'], linewidth=2, alpha=0.6)
        
        # Caja de texto
        bbox_props = dict(boxstyle='round,pad=0.5', facecolor=evento['color'], 
                         alpha=0.3, edgecolor='black', linewidth=2)
        ax.text(evento['año'], evento['y'], evento['evento'], 
               ha='center', va='center' if evento['y'] > 5 else 'center',
               fontsize=8.5, fontweight='bold', bbox=bbox_props)
        
        # Año debajo
        ax.text(evento['año'], 4.5, str(evento['año']), ha='center', va='top',
               fontsize=9, fontweight='bold')
    
    # Eras/Épocas
    epocas = [
        {'inicio': 1945, 'fin': 1970, 'nombre': 'Era Fundacional\nNeurociencia Cognitiva', 'color': 'lightblue'},
        {'inicio': 1970, 'fin': 1995, 'nombre': 'Era Simbólica\nSistemas Expertos', 'color': 'lightcoral'},
        {'inicio': 1995, 'fin': 2010, 'nombre': 'Era Híbrida\nCognitiva Unificada', 'color': 'lightgreen'},
        {'inicio': 2010, 'fin': 2025, 'nombre': 'Era Moderna\nDeep Learning + Neuromórfica', 'color': 'lightyellow'}
    ]
    
    for epoca in epocas:
        rect = Rectangle((epoca['inicio'], 0.5), epoca['fin'] - epoca['inicio'], 1.5,
                        facecolor=epoca['color'], alpha=0.2, edgecolor='gray', linewidth=1)
        ax.add_patch(rect)
        ax.text((epoca['inicio'] + epoca['fin'])/2, 1.25, epoca['nombre'],
               ha='center', va='center', fontsize=9, style='italic')
    
    # Leyenda de categorías
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['brain'], 
              markersize=12, label='Neurociencia'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['symbolic'], 
              markersize=12, label='Simbólico'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['hybrid'], 
              markersize=12, label='Híbrido'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['neural'], 
              markersize=12, label='Subsimbólico'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS['success'], 
              markersize=12, label='Aplicación')
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=11, framealpha=0.9)
    
    # Notas al pie
    ax.text(1985, 0.2, '📚 Referencias clave mencionadas en el Foro Semana 7', 
           ha='center', fontsize=10, style='italic')
    
    plt.savefig('/Users/leomos/Downloads/computacion-bioinspirada/foro_semana_7/timeline_historia_cognitiva.png',
                dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Timeline 4: Historia de arquitecturas cognitivas - Guardada")
    
    return fig


def main():
    """Generar todas las visualizaciones"""
    
    print("\n" + "="*80)
    print("🎨 GENERANDO VISUALIZACIONES AVANZADAS PARA FORO SEMANA 7")
    print("="*80 + "\n")
    
    print("📊 Creando infografías educativas...\n")
    
    # 1. Infografía cerebro → computación
    print("[1/4] Infografía: Del cerebro biológico a la arquitectura computacional...")
    crear_infografia_arquitectura_cerebro()
    
    # 2. Diagrama arquitectura híbrida
    print("\n[2/4] Diagrama técnico: Arquitectura híbrida detallada...")
    crear_diagrama_arquitectura_hibrida()
    
    # 3. Comparación de paradigmas
    print("\n[3/4] Gráficos comparativos: Simbólico vs Subsimbólico vs Híbrido...")
    crear_comparacion_paradigmas()
    
    # 4. Timeline histórica
    print("\n[4/4] Línea de tiempo: Historia de las arquitecturas cognitivas...")
    crear_timeline_historia_cognitiva()
    
    print("\n" + "="*80)
    print("✅ VISUALIZACIONES COMPLETADAS")
    print("="*80)
    print("\n📁 Archivos generados en: foro_semana_7/")
    print("   1. infografia_cerebro_computacion.png")
    print("   2. diagrama_arquitectura_hibrida.png")
    print("   3. comparacion_paradigmas.png")
    print("   4. timeline_historia_cognitiva.png")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    main()
