# Automate Catalog Updates System (Frutería)

Sistema de automatización para una tienda de frutas online que procesa catálogos de productos enviados por proveedores. El sistema convierte imágenes grandes TIFF a formato JPEG optimizado, genera páginas HTML con descripciones de productos y actualiza el sitio web mediante Django.

Lo estoy completando poco a poco antes de realizar el qwiklab, de esta forma puedo pararme a probar todo. La idea es generar pruebas unitarias para cada apartado y poder probarlos uno a uno.

## Funcionalidades Principales

### Procesamiento de Imágenes
- [x] Identificar los nombres de las imágenes que se tienen en la carpeta origen
- [ ] Convertir archivos .TIF de alta resolución a imágenes JPEG optimizadas
- [ ] Redimensionar automáticamente las imágenes para web
- [ ] Mantener calidad visual mientras reduce el tamaño de archivo

### Generación de Contenido
- [ ] Procesar archivos .txt con descripciones de productos
- [ ] Crear páginas HTML que combinan imágenes y descripciones
- [ ] Extraer información de peso y nombre de frutas

### Integración con Django
- [ ] Subir contenido HTML generado al servidor Django
- [ ] Enviar datos de productos mediante Python requests
- [ ] Actualizar el catálogo online automáticamente

### Sistema de Notificaciones
- [ ] Generar reportes PDF con nombres y pesos totales de frutas
- [ ] Enviar emails automáticos a proveedores con resumen de carga
- [ ] Incluir PDF adjunto con estadísticas detalladas

### Monitoreo del Sistema
- [ ] Ejecutar verificaciones de salud en paralelo
- [ ] Detectar problemas del sistema automáticamente
- [ ] Enviar alertas por email en caso de errores

## Pruebas Unitarias

### Tests por Módulo
- [ ] Test para procesamiento de imágenes TIFF
- [ ] Test para conversión a JPEG
- [ ] Test para extracción de datos de archivos .txt
- [ ] Test para generación de HTML
- [ ] Test para integración con Django API
- [ ] Test para generación de PDFs
- [ ] Test para envío de emails
- [ ] Test para monitoreo del sistema
