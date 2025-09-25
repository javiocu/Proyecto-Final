# Automate Catalog Updates System (Frutería)

Sistema de automatización para una tienda de frutas online que procesa catálogos de productos enviados por proveedores. El sistema convierte imágenes grandes TIFF a formato JPEG optimizado, genera páginas HTML con descripciones de productos y actualiza el sitio web mediante Django.

Lo estoy completando poco a poco antes de realizar el qwiklab, de esta forma puedo pararme a probar todo. La idea es generar pruebas unitarias para cada apartado y poder probarlos uno a uno.

## Funcionalidades Principales

### Procesamiento de Imágenes  
- [x] Identificar los nombres de las imágenes que se tienen en la carpeta origen
- [x] Convertir archivos .TIF de alta resolución a imágenes JPEG optimizadas  
- [x] Redimensionar automáticamente las imágenes para web (3000x2000 → 600x400 píxeles)
- [x] Mantener calidad visual mientras reduce el tamaño de archivo
- [x] Convertir formato RGBA a RGB antes del procesamiento
- [x] Generar test para comprobar que todo funciona correctamente

### Generación de Contenido
- [ ] Procesar archivos .txt con descripciones de productos del directorio `supplier-data/descriptions`
- [ ] Extraer información de peso y nombre de frutas desde archivos de texto
- [ ] Convertir peso de formato "500 lbs" a entero 500
- [ ] Crear estructura JSON con campos: name, weight, description, image_name
- [ ] Procesar todos los archivos de descripción automáticamente

### Integración con Django
- [ ] Subir imágenes JPEG procesadas al servidor web fruit catalog
- [ ] Enviar datos de productos mediante Python requests a `/fruits` endpoint
- [ ] Actualizar el catálogo online automáticamente usando POST requests
- [ ] Crear script `supplier_image_upload.py` para cargar imágenes
- [ ] Crear script `run.py` para cargar descripciones como JSON

### Sistema de Notificaciones  
- [ ] Generar reportes PDF con nombres y pesos totales de frutas usando ReportLab
- [ ] Crear script `reports.py` con método generate_report  
- [ ] Procesar datos de descripción en formato: "name: Apple\nweight: 500 lbs"
- [ ] Enviar emails automáticos a proveedores con resumen de carga
- [ ] Incluir PDF adjunto con estadísticas detalladas (`processed.pdf`)
- [ ] Crear script `report_email.py` para automatizar envío

### Monitoreo del Sistema
- [ ] Crear script `health_check.py` para verificaciones cada 60 segundos
- [ ] Detectar CPU usage > 80% automáticamente  
- [ ] Detectar espacio en disco < 20% disponible
- [ ] Detectar memoria disponible < 100MB
- [ ] Verificar resolución de hostname "localhost" a "127.0.0.1"
- [ ] Enviar alertas por email en caso de errores con subjects específicos

## Pruebas Unitarias

### Tests por Módulo
- [x] Test para procesamiento de imágenes TIFF (con mocks)
- [x] Test para conversión a JPEG (casos de éxito y error)
- [x] Test para manejo de FileNotFoundError
- [ ] Test para extracción de datos de archivos .txt
- [ ] Test para generación de JSON válido  
- [ ] Test para integración con Django API (/fruits endpoint)
- [ ] Test para generación de PDFs con ReportLab
- [ ] Test para envío de emails con attachments
- [ ] Test para monitoreo del sistema (CPU, memoria, disco)
- [ ] Test para health check notifications

## Scripts del Proyecto

### Scripts Principales
- [x] `changeImage.py` - Procesamiento y conversión de imágenes
- [ ] `supplier_image_upload.py` - Subida de imágenes al servidor web
- [ ] `run.py` - Procesamiento y subida de descripciones como JSON  
- [ ] `reports.py` - Generación de reportes PDF
- [ ] `report_email.py` - Envío automático de reportes por email
- [ ] `emails.py` - Métodos generate_email() y send_email()
- [ ] `health_check.py` - Monitoreo continuo del sistema

### Configuración y Permisos
- [x] Shebang line: `#!/usr/bin/env python3` en todos los scripts
- [ ] Permisos ejecutables: `chmod +x` para todos los scripts
- [ ] Importación de librerías necesarias (PIL, requests, ReportLab, psutil, shutil)
- [ ] Configuración de URLs del servidor web externo
