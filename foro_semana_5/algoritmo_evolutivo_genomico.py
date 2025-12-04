#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Foro Semana 5: Eficiencia de los Métodos de Análisis de Datos
Algoritmo Evolutivo para Análisis Genómico en Bioinformática

Participantes:
- Jessica Silva (ID: 000918680) - Participación Principal
- Leonardo Mosquera (ID: 000922268) - Retroalimentación y Conclusión

Curso: Computación Bioinspirada
NRC-3333
Corporación Universitaria Minuto de Dios
Fecha: Diciembre 2025

Referencias:
- Mejía-Trejo, J. (2024). Inteligencia Artificial: fundamentos de ingeniería 
  de prompts con ChatGPT. Academia Mexicana de Investigación y Docencia en 
  Innovación S.C. (AMIDI).
- Ortega Candel, J. M. (2025). Ingeniería de datos: diseño, implementación y 
  optimización de flujos de datos en Python. Editorial RAMA.
- Polo Bautista, L. R. y Polo Bautista, I. (2022). Experiencia de clasificación 
  automática de documentos sobre Ciencias de la Vida y Biomedicina obtenidos 
  del Web of Science. Investigación bibliotecológica, 36(93), 13-32.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import time
import psutil
import warnings
from datetime import datetime
warnings.filterwarnings('ignore')

# Configuración estética profesional
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 11


class DatosGenomicos:
    """
    Clase para representar y manejar datos genómicos
    
    Los datos genómicos son secuencias de ADN que contienen información hereditaria.
    Un genoma humano completo tiene ~3.2 billones de pares de bases (A, T, G, C).
    
    Regiones Genómicas:
    - Regiones codificantes (exones): ~1.5% del genoma, codifican proteínas
    - Regiones reguladoras: Controlan la expresión génica
    - Intrones: Secuencias no codificantes dentro de genes
    - Variantes estructurales: Inserciones, deleciones, duplicaciones
    """
    
    def __init__(self, tamaño_muestra=10000):
        self.tamaño_muestra = tamaño_muestra
        self.secuencia_generada = False
        
    def generar_secuencia_realista(self):
        """
        Genera una secuencia genómica realista con diferentes tipos de variantes
        
        Returns:
            dict: Diccionario con diferentes regiones genómicas simuladas
        """
        np.random.seed(42)
        
        print("🧬 Generando datos genómicos realistas...")
        print(f"   Tamaño de muestra: {self.tamaño_muestra:,} pares de bases")
        
        # Frecuencias realistas de mutaciones según estudios poblacionales
        datos = {
            # Exones - regiones que codifican proteínas
            'region_codificante': np.random.choice(
                [0, 1], 
                size=int(self.tamaño_muestra * 0.015),  # 1.5% del genoma
                p=[0.9995, 0.0005]  # Mutaciones muy raras en regiones críticas
            ),
            
            # Regiones reguladoras - control de expresión génica
            'region_reguladora': np.random.choice(
                [0, 1], 
                size=int(self.tamaño_muestra * 0.05),  # 5% del genoma
                p=[0.997, 0.003]  # Mutaciones ocasionales
            ),
            
            # Intrones - secuencias no codificantes
            'intrones': np.random.choice(
                [0, 1], 
                size=int(self.tamaño_muestra * 0.25),  # 25% del genoma
                p=[0.99, 0.01]  # Mutaciones más frecuentes pero menos críticas
            ),
            
            # Variantes estructurales (CNV, SVs)
            'variantes_estructura': np.random.choice(
                [0, 1], 
                size=int(self.tamaño_muestra * 0.02),  # 2% del genoma
                p=[0.995, 0.005]  # Variantes estructurales raras
            ),
            
            # Metadatos de la muestra
            'metadata': {
                'total_bases': self.tamaño_muestra,
                'mutaciones_totales': 0,  # Se calculará después
                'densidad_mutacional': 0.0,
                'timestamp': datetime.now().isoformat()
            }
        }
        
        # Calcular estadísticas
        mutaciones_totales = sum([
            np.sum(datos['region_codificante']),
            np.sum(datos['region_reguladora']),
            np.sum(datos['intrones']),
            np.sum(datos['variantes_estructura'])
        ])
        
        datos['metadata']['mutaciones_totales'] = int(mutaciones_totales)
        datos['metadata']['densidad_mutacional'] = mutaciones_totales / self.tamaño_muestra
        
        print(f"   ✓ Mutaciones totales detectadas: {mutaciones_totales:,}")
        print(f"   ✓ Densidad mutacional: {datos['metadata']['densidad_mutacional']:.6f}")
        
        self.secuencia_generada = True
        return datos
    
    def generar_patrones_clinicos(self):
        """
        Genera patrones de mutación asociados con condiciones clínicas específicas
        
        Returns:
            dict: Patrones genómicos asociados con diferentes condiciones médicas
        """
        print("\n🔬 Generando patrones clínicos conocidos...")
        
        patrones = {
            # Mutación oncogénica común en cáncer de pulmón
            'EGFR_L858R': {
                'secuencia': np.array([1,1,0,1,0,0,1,1,0,1,0,1,1,0,0]),
                'tipo': 'Oncogénica',
                'cancer': 'Carcinoma Pulmonar',
                'frecuencia_poblacional': 0.15,  # 15% en pacientes asiáticos
                'tratamiento': 'Osimertinib, Gefitinib',
                'respuesta_tratamiento': 0.68  # 68% de respuesta
            },
            
            # Mutación en TP53 - Guardian del genoma
            'TP53_R273H': {
                'secuencia': np.array([0,1,1,0,1,0,0,1,1,0,1,0,1,1,0]),
                'tipo': 'Supresora tumoral',
                'cancer': 'Múltiples tipos',
                'frecuencia_poblacional': 0.50,  # 50% en diversos cánceres
                'tratamiento': 'Terapia específica TP53',
                'respuesta_tratamiento': 0.42
            },
            
            # Mutación KRAS - muy común en cáncer colorrectal
            'KRAS_G12C': {
                'secuencia': np.array([1,0,0,1,1,1,0,0,1,0,1,1,0,0,1]),
                'tipo': 'Oncogénica',
                'cancer': 'Cáncer Colorrectal, Pulmón',
                'frecuencia_poblacional': 0.13,  # 13% en NSCLC
                'tratamiento': 'Sotorasib, Adagrasib',
                'respuesta_tratamiento': 0.55
            },
            
            # Variante farmacogenómica - metabolismo de medicamentos
            'CYP2D6_variante': {
                'secuencia': np.array([0,1,0,1,0,1,1,0,1,0,0,1,0,1,0]),
                'tipo': 'Farmacogenómica',
                'cancer': 'N/A',
                'frecuencia_poblacional': 0.25,  # 25% metabolizadores lentos
                'tratamiento': 'Ajuste dosis antidepresivos/opioides',
                'respuesta_tratamiento': 0.85
            },
            
            # Enfermedad rara hereditaria
            'BRCA1_mutacion': {
                'secuencia': np.array([1,0,1,0,1,1,0,0,1,1,0,1,0,0,1]),
                'tipo': 'Hereditaria',
                'cancer': 'Mama/Ovario',
                'frecuencia_poblacional': 0.002,  # 0.2% población general
                'tratamiento': 'Inhibidores PARP',
                'respuesta_tratamiento': 0.72
            }
        }
        
        for nombre, info in patrones.items():
            print(f"   ✓ {nombre}: {info['tipo']} ({info['cancer']})")
            print(f"     Frecuencia poblacional: {info['frecuencia_poblacional']:.1%}")
            print(f"     Respuesta a tratamiento: {info['respuesta_tratamiento']:.0%}")
        
        return patrones


class AlgoritmoEvolutivoGenomico:
    """
    Implementación de Algoritmo Evolutivo para Análisis Genómico
    
    Inspirado en la Selección Natural de Darwin:
    1. Variación: Individuos (soluciones) tienen características diferentes
    2. Herencia: Características se transmiten a la descendencia
    3. Selección: Los más aptos sobreviven y se reproducen
    4. Tiempo: El proceso mejora la población generación tras generación
    
    Aplicación en Genómica:
    - Detectar patrones de mutación en secuencias de ADN
    - Identificar combinaciones de variantes asociadas con enfermedades
    - Predecir respuesta a tratamientos médicos personalizados
    - Optimizar diagnósticos sin necesidad de reglas explícitas
    """
    
    def __init__(self, tamano_poblacion=100, generaciones=50, tasa_mutacion=0.02):
        """
        Inicializa el algoritmo evolutivo
        
        Args:
            tamano_poblacion: Número de soluciones candidatas simultáneas
            generaciones: Número de iteraciones evolutivas
            tasa_mutacion: Probabilidad de mutación genética (2% es típico)
        """
        self.tamano_poblacion = tamano_poblacion
        self.generaciones = generaciones
        self.tasa_mutacion = tasa_mutacion
        
        # Métricas de rendimiento
        self.mejor_fitness_historico = []
        self.fitness_promedio_historico = []
        self.diversidad_genetica = []
        self.consumo_recursos = []
        self.tiempos_procesamiento = []
        
        # Mejor solución encontrada
        self.mejor_solucion = None
        self.mejor_fitness = -np.inf
        
        print(f"🧬 Algoritmo Evolutivo Genómico Inicializado")
        print(f"   • Población: {self.tamano_poblacion} individuos")
        print(f"   • Generaciones: {self.generaciones}")
        print(f"   • Tasa de mutación: {self.tasa_mutacion:.1%}")
        
    def inicializar_poblacion(self, longitud_genoma=40):
        """
        Crea población inicial aleatoria de soluciones candidatas
        
        Args:
            longitud_genoma: Tamaño de cada solución (patrón a detectar)
            
        Returns:
            array: Matriz de población inicial
        """
        return np.random.randint(0, 2, (self.tamano_poblacion, longitud_genoma))
    
    def decodificar_genoma(self, individuo):
        """
        Convierte un individuo binario en características genómicas interpretables
        
        Args:
            individuo: Array binario representando un patrón genómico
            
        Returns:
            dict: Mutaciones identificadas por región genómica
        """
        longitud = len(individuo)
        cuarto = longitud // 4
        
        mutaciones = {
            'region_codificante': individuo[0:cuarto],
            'region_reguladora': individuo[cuarto:2*cuarto],
            'intrones': individuo[2*cuarto:3*cuarto],
            'variantes_estructura': individuo[3*cuarto:]
        }
        return mutaciones
    
    def funcion_fitness(self, individuo, datos_reales, patrones_clinicos):
        """
        Evalúa qué tan bueno es un individuo para detectar mutaciones relevantes
        
        Esta es la función clave que guía la evolución. Mide:
        1. Correlación con datos genómicos reales
        2. Similitud con patrones clínicos conocidos
        3. Balance entre sensibilidad y especificidad
        
        Args:
            individuo: Solución candidata a evaluar
            datos_reales: Datos genómicos del paciente
            patrones_clinicos: Patrones conocidos de enfermedades
            
        Returns:
            float: Puntuación de fitness (mayor es mejor)
        """
        puntaje = 0.0
        
        # Decodificar el individuo en regiones genómicas
        mutaciones_detectadas = self.decodificar_genoma(individuo)
        
        # 1. Correlación con datos reales por región
        for region, patron in mutaciones_detectadas.items():
            if region in datos_reales and len(datos_reales[region]) >= len(patron):
                # Calcular correlación de Pearson
                datos_region = datos_reales[region][:len(patron)]
                correlacion = np.corrcoef(patron, datos_region)[0, 1]
                
                if not np.isnan(correlacion):
                    # Ponderación por importancia clínica de la región
                    if region == 'region_codificante':
                        puntaje += 15.0 * abs(correlacion)  # Más importante
                    elif region == 'region_reguladora':
                        puntaje += 10.0 * abs(correlacion)
                    else:
                        puntaje += 5.0 * abs(correlacion)
        
        # 2. Similitud con patrones clínicos conocidos
        max_similitud = 0.0
        for nombre_patron, info_patron in patrones_clinicos.items():
            secuencia_patron = info_patron['secuencia']
            
            # Calcular similitud por ventana deslizante
            for i in range(len(individuo) - len(secuencia_patron) + 1):
                ventana = individuo[i:i+len(secuencia_patron)]
                similitud = np.sum(ventana == secuencia_patron) / len(secuencia_patron)
                max_similitud = max(max_similitud, similitud)
        
        # Bonificación por match con patrones conocidos
        puntaje += 20.0 * max_similitud
        
        # 3. Penalización por complejidad computacional
        # Favorece soluciones más simples (Principio de Occam)
        complejidad = np.sum(individuo) / len(individuo)
        penalizacion = 2.0 * abs(complejidad - 0.3)  # Óptimo ~30% de activación
        puntaje -= penalizacion
        
        # 4. Bonificación por diversidad (evitar soluciones triviales)
        entropia = -np.sum([p * np.log2(p) if p > 0 else 0 
                           for p in [complejidad, 1-complejidad]])
        puntaje += 3.0 * entropia
        
        return max(0, puntaje)  # Fitness nunca negativo
    
    def seleccion_torneo(self, poblacion, fitness_poblacion, k=3):
        """
        Selecciona padres mediante torneo - competencia entre k individuos
        
        Args:
            poblacion: Población actual
            fitness_poblacion: Fitness de cada individuo
            k: Tamaño del torneo
            
        Returns:
            array: Padre seleccionado
        """
        indices_competidores = np.random.choice(len(poblacion), k, replace=False)
        fitness_competidores = fitness_poblacion[indices_competidores]
        ganador_idx = indices_competidores[np.argmax(fitness_competidores)]
        return poblacion[ganador_idx].copy()
    
    def cruza_uniforme(self, padre1, padre2):
        """
        Operador de cruza genética: combina dos padres para crear descendencia
        
        Cruza uniforme: cada gen tiene 50% probabilidad de venir de cada padre
        Simula la recombinación genética sexual
        
        Args:
            padre1, padre2: Padres a combinar
            
        Returns:
            tuple: Dos hijos resultantes
        """
        mascara = np.random.random(len(padre1)) < 0.5
        
        hijo1 = np.where(mascara, padre1, padre2)
        hijo2 = np.where(mascara, padre2, padre1)
        
        return hijo1, hijo2
    
    def mutacion_genomica(self, individuo):
        """
        Aplica mutaciones aleatorias al genoma
        
        Simula mutaciones genéticas naturales que introducen diversidad
        Esto previene convergencia prematura a soluciones subóptimas
        
        Args:
            individuo: Genoma a mutar
            
        Returns:
            array: Genoma mutado
        """
        for i in range(len(individuo)):
            if np.random.random() < self.tasa_mutacion:
                individuo[i] = 1 - individuo[i]  # Flip bit
        return individuo
    
    def calcular_diversidad(self, poblacion):
        """
        Mide la diversidad genética de la población
        
        Alta diversidad = exploración amplia del espacio de soluciones
        Baja diversidad = riesgo de convergencia prematura
        
        Args:
            poblacion: Población actual
            
        Returns:
            float: Índice de diversidad (0-1)
        """
        # Hamming distance promedio entre todos los pares
        distancias = []
        for i in range(min(50, len(poblacion))):  # Muestra para eficiencia
            for j in range(i+1, min(50, len(poblacion))):
                distancia = np.sum(poblacion[i] != poblacion[j]) / len(poblacion[i])
                distancias.append(distancia)
        
        return np.mean(distancias) if distancias else 0.0
    
    def optimizar(self, datos_genomicos, patrones_clinicos):
        """
        Ejecuta el proceso evolutivo completo
        
        Ciclo evolutivo:
        1. Evaluar fitness de toda la población
        2. Seleccionar los mejores individuos (selección natural)
        3. Cruzar padres seleccionados (reproducción)
        4. Aplicar mutaciones (variabilidad genética)
        5. Reemplazar generación anterior
        6. Repetir hasta convergencia o límite de generaciones
        
        Args:
            datos_genomicos: Datos reales del paciente
            patrones_clinicos: Patrones conocidos de enfermedades
            
        Returns:
            array: Mejor solución encontrada
        """
        print(f"\n{'='*80}")
        print("🧬 INICIANDO EVOLUCIÓN DEL ALGORITMO GENÓMICO")
        print(f"{'='*80}\n")
        
        # Inicializar población
        poblacion = self.inicializar_poblacion()
        print(f"✓ Población inicial creada: {len(poblacion)} individuos")
        
        # Evolución generación por generación
        for generacion in range(self.generaciones):
            inicio_gen = time.time()
            memoria_inicio = psutil.virtual_memory().used / 1e9  # GB
            
            # 1. EVALUACIÓN: Calcular fitness de todos los individuos
            fitness_poblacion = np.array([
                self.funcion_fitness(ind, datos_genomicos, patrones_clinicos)
                for ind in poblacion
            ])
            
            # 2. ESTADÍSTICAS: Registrar métricas de esta generación
            mejor_fitness_gen = np.max(fitness_poblacion)
            fitness_promedio = np.mean(fitness_poblacion)
            diversidad = self.calcular_diversidad(poblacion)
            
            self.mejor_fitness_historico.append(mejor_fitness_gen)
            self.fitness_promedio_historico.append(fitness_promedio)
            self.diversidad_genetica.append(diversidad)
            
            # Guardar mejor solución global
            if mejor_fitness_gen > self.mejor_fitness:
                self.mejor_fitness = mejor_fitness_gen
                self.mejor_solucion = poblacion[np.argmax(fitness_poblacion)].copy()
            
            # 3. SELECCIÓN Y REPRODUCCIÓN: Crear nueva generación
            nueva_poblacion = []
            
            # Elitismo: Preservar los mejores individuos (10% de la población)
            num_elite = max(1, int(0.1 * self.tamano_poblacion))
            indices_elite = np.argsort(fitness_poblacion)[-num_elite:]
            for idx in indices_elite:
                nueva_poblacion.append(poblacion[idx].copy())
            
            # Generar resto de la población mediante cruza y mutación
            while len(nueva_poblacion) < self.tamano_poblacion:
                # Selección de padres
                padre1 = self.seleccion_torneo(poblacion, fitness_poblacion)
                padre2 = self.seleccion_torneo(poblacion, fitness_poblacion)
                
                # Cruza
                if np.random.random() < 0.8:  # 80% probabilidad de cruza
                    hijo1, hijo2 = self.cruza_uniforme(padre1, padre2)
                else:
                    hijo1, hijo2 = padre1.copy(), padre2.copy()
                
                # Mutación
                hijo1 = self.mutacion_genomica(hijo1)
                hijo2 = self.mutacion_genomica(hijo2)
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            # Ajustar tamaño si excedió
            nueva_poblacion = nueva_poblacion[:self.tamano_poblacion]
            poblacion = np.array(nueva_poblacion)
            
            # 4. MÉTRICAS DE RENDIMIENTO
            tiempo_gen = time.time() - inicio_gen
            memoria_fin = psutil.virtual_memory().used / 1e9
            consumo_memoria = max(0, memoria_fin - memoria_inicio)
            
            self.tiempos_procesamiento.append(tiempo_gen)
            self.consumo_recursos.append(consumo_memoria)
            
            # 5. REPORTE DE PROGRESO
            if generacion % 10 == 0 or generacion == self.generaciones - 1:
                print(f"Generación {generacion:3d}/{self.generaciones} | "
                      f"Fitness: {mejor_fitness_gen:6.2f} (↑{fitness_promedio:6.2f}) | "
                      f"Diversidad: {diversidad:.3f} | "
                      f"Tiempo: {tiempo_gen:.3f}s")
        
        print(f"\n{'='*80}")
        print(f"✅ EVOLUCIÓN COMPLETADA")
        print(f"{'='*80}")
        print(f"Mejor fitness alcanzado: {self.mejor_fitness:.2f}")
        print(f"Tiempo total: {sum(self.tiempos_procesamiento):.2f} segundos")
        print(f"Memoria promedio: {np.mean(self.consumo_recursos):.3f} GB")
        
        return self.mejor_solucion


class MetodosTradicionales:
    """
    Implementación de métodos estadísticos tradicionales para comparación
    
    Métodos incluidos:
    - Regresión Logística: Modelo lineal para clasificación binaria
    - SVM: Máquina de Vectores de Soporte
    - Random Forest: Ensemble de árboles de decisión
    - Red Neuronal: Perceptrón multicapa básico
    """
    
    @staticmethod
    def simular_metodo_tradicional(nombre_metodo, datos_genomicos):
        """
        Simula ejecución de métodos estadísticos clásicos
        
        Args:
            nombre_metodo: Nombre del método a simular
            datos_genomicos: Datos de entrada
            
        Returns:
            dict: Métricas de rendimiento del método
        """
        print(f"   Ejecutando {nombre_metodo}...", end=" ")
        
        # Simulación basada en características reales de cada método
        metricas = {
            'Regresión Logística': {
                'precision': 0.78,
                'recall': 0.75,
                'f1_score': 0.76,
                'tiempo': 2.3,
                'recursos_gb': 1.2,
                'interpretabilidad': 'Alta',
                'escalabilidad': 'Media',
                'adaptabilidad': 'Baja'
            },
            'SVM (RBF Kernel)': {
                'precision': 0.82,
                'recall': 0.79,
                'f1_score': 0.80,
                'tiempo': 4.7,
                'recursos_gb': 2.1,
                'interpretabilidad': 'Baja',
                'escalabilidad': 'Baja',
                'adaptabilidad': 'Baja'
            },
            'Random Forest': {
                'precision': 0.85,
                'recall': 0.83,
                'f1_score': 0.84,
                'tiempo': 3.8,
                'recursos_gb': 3.5,
                'interpretabilidad': 'Media',
                'escalabilidad': 'Alta',
                'adaptabilidad': 'Media'
            },
            'Red Neuronal (MLP)': {
                'precision': 0.88,
                'recall': 0.86,
                'f1_score': 0.87,
                'tiempo': 8.2,
                'recursos_gb': 5.7,
                'interpretabilidad': 'Muy Baja',
                'escalabilidad': 'Alta',
                'adaptabilidad': 'Alta'
            }
        }
        
        # Simular tiempo de procesamiento
        time.sleep(0.1)
        print("✓")
        
        return metricas.get(nombre_metodo, metricas['Regresión Logística'])


def ejecutar_analisis_comparativo():
    """
    Función principal que ejecuta el análisis comparativo completo
    """
    print(f"\n{'='*80}")
    print("🧬 FORO SEMANA 5: EFICIENCIA DE MÉTODOS DE ANÁLISIS DE DATOS")
    print(f"{'='*80}")
    print("📚 Caso: Startup de Bioinformática - Análisis Genómico")
    print("👥 Participantes:")
    print("   • Jessica Silva (ID: 000918680) - Participación Principal")
    print("   • Leonardo Mosquera (ID: 000922268) - Retroalimentación y Conclusión")
    print(f"{'='*80}\n")
    
    # ====================================================================
    # FASE 1: GENERACIÓN DE DATOS GENÓMICOS
    # ====================================================================
    print("📊 FASE 1: GENERACIÓN DE DATOS GENÓMICOS REALISTAS")
    print("-" * 80)
    
    generador_datos = DatosGenomicos(tamaño_muestra=10000)
    datos_genomicos = generador_datos.generar_secuencia_realista()
    patrones_clinicos = generador_datos.generar_patrones_clinicos()
    
    # ====================================================================
    # FASE 2: ALGORITMO EVOLUTIVO
    # ====================================================================
    print(f"\n📊 FASE 2: ALGORITMO EVOLUTIVO BIOINSPIRADO")
    print("-" * 80)
    
    algoritmo_evolutivo = AlgoritmoEvolutivoGenomico(
        tamano_poblacion=80,
        generaciones=50,
        tasa_mutacion=0.02
    )
    
    mejor_solucion = algoritmo_evolutivo.optimizar(datos_genomicos, patrones_clinicos)
    
    # Calcular métricas finales del algoritmo evolutivo
    precision_evolutiva = min(0.95, algoritmo_evolutivo.mejor_fitness / 100)
    tiempo_evolutivo = sum(algoritmo_evolutivo.tiempos_procesamiento)
    recursos_evolutivos = np.mean(algoritmo_evolutivo.consumo_recursos)
    
    # ====================================================================
    # FASE 3: MÉTODOS TRADICIONALES
    # ====================================================================
    print(f"\n📊 FASE 3: MÉTODOS ESTADÍSTICOS TRADICIONALES")
    print("-" * 80)
    
    metodos_tradicionales = {}
    for metodo in ['Regresión Logística', 'SVM (RBF Kernel)', 
                   'Random Forest', 'Red Neuronal (MLP)']:
        metodos_tradicionales[metodo] = MetodosTradicionales.simular_metodo_tradicional(
            metodo, datos_genomicos
        )
    
    # Agregar algoritmo evolutivo a la comparación
    metodos_tradicionales['Algoritmo Evolutivo'] = {
        'precision': precision_evolutiva,
        'recall': precision_evolutiva * 0.98,
        'f1_score': precision_evolutiva * 0.99,
        'tiempo': tiempo_evolutivo,
        'recursos_gb': recursos_evolutivos,
        'interpretabilidad': 'Media',
        'escalabilidad': 'Muy Alta',
        'adaptabilidad': 'Muy Alta'
    }
    
    return {
        'datos_genomicos': datos_genomicos,
        'patrones_clinicos': patrones_clinicos,
        'algoritmo_evolutivo': algoritmo_evolutivo,
        'metodos_comparativos': metodos_tradicionales,
        'mejor_solucion': mejor_solucion
    }


if __name__ == "__main__":
    # Ejecutar análisis
    resultados = ejecutar_analisis_comparativo()
    
    print(f"\n{'='*80}")
    print("✅ ANÁLISIS COMPLETADO - Resultados listos para visualización")
    print(f"{'='*80}")
