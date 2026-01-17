# 🛡️ System Log & Security Analyzer

Este proyecto es una herramienta de **Backend** desarrollada en Python para la auditoría y monitoreo de seguridad. Su función principal es el análisis automatizado de archivos de registro (logs) del sistema para identificar patrones sospechosos, intentos de intrusión o errores críticos que comprometan la integridad del equipo.

> [!IMPORTANT]
> **ENFOQUE DE SEGURIDAD:** Esta herramienta actúa como un sistema de detección temprana, ayudando a los administradores a visualizar amenazas ocultas en miles de líneas de texto de los logs del sistema.

---

## ✨ Características
- **Escaneo de Patrones:** Busca indicadores de compromiso (IoC) como múltiples intentos fallidos de login o ejecución de comandos sospechosos.
- **Detección de Errores Críticos:** Identifica fallos de hardware o software antes de que causen una caída del sistema.
- **Reportes de Integridad:** Genera un resumen limpio y legible con los hallazgos más importantes.
- **Análisis de Texto Eficiente:** Capacidad para procesar archivos de gran tamaño de forma rápida.

---

## 🛠️ Tecnologías y Conceptos Básicos

Para entender cómo funciona este software, debemos conocer estos términos de ciberseguridad:

* **Logs del Sistema:** Son archivos donde el sistema operativo anota TODO lo que pasa (quién entró, qué programa falló, a qué hora se apagó).
* **Expresiones Regulares (Regex):** Es una técnica de búsqueda avanzada que permite encontrar palabras o códigos complejos dentro de un archivo.
* **Integridad de Datos:** Se refiere a asegurar que la información del sistema no haya sido alterada por un atacante.



### **Instalación y Requisitos**
Este script utiliza librerías estándar de Python, por lo que es muy ligero. Se recomienda usar un **entorno virtual (venv)**:

```bash
# Crear entorno
python -m venv venv
# Activar (Windows)
.\venv\Scripts\activate
