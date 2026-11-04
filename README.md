# Visualizador Kardex para GitHub Pages

## Contenido del repositorio

Sube estos archivos a la raiz del nuevo repositorio: `index.html` y `data.json`. Conserva tambien `convertir_excel_a_json.py` y este README como apoyo.

`data.json` concentra las tres hojas del Excel en una sola fuente: `Tabla_resumen` como `summary`, `Dx_arch_clues` como `records` y `Acciones_sugeridas` como `actions`. El conversor también cruza cada CLUES con la hoja `DATOS` del archivo `RO_NACIONAL_2025_YUCATANact.xlsx` y agrega `REGIÓN OPERATIVA` desde `NOM_REG` o `NOM_REGION_2025`. El mapa y la interfaz permanecen en `index.html`.

## Publicacion inicial

1. Crea un repositorio publico en GitHub y sube los archivos a la raiz.
2. En **Settings → Pages**, publica desde la rama `main`, carpeta `/ (root)`.
3. Comparte la URL publicada (normalmente `https://USUARIO.github.io/REPOSITORIO/`) con la persona que administra WordPress.
4. Esa persona inserta una vez un bloque HTML como este, con la URL real:

```html
<iframe src="https://USUARIO.github.io/REPOSITORIO/" title="Avance Kardex por estado" loading="lazy" style="display:block;width:100%;height:1100px;border:0"></iframe>
```

## Actualizaciones futuras

1. Guarda el nuevo Excel con las mismas hojas y columnas.
2. Guarda `data.xlsx` y `RO_NACIONAL_2025_YUCATANact.xlsx` en `C:\Users\diego.velazquez.OPDIB\OneDrive - IMSS-BIENESTAR\Documentos\IMSS-B\35 Medicamentos tablero\Avance`. Ejecuta el conversor con Python y `openpyxl` instalado. La ruta de ambos libros está configurada como predeterminada; genera `data.json` en esa misma carpeta de OneDrive, junto al Excel. También acepta una ruta para el Excel principal como argumento y `--regions` para el archivo de regiones si cambia la ubicación.
3. Reemplaza solo `data.json` en GitHub y confirma el cambio. La pagina lee el JSON al abrirse; no se actualiza mientras permanece abierta. El visitante puede recargarla para leer la version nueva. El conversor agrega la hora local de generacion en `meta.generated`; el visualizador la muestra como fecha de generacion. Si falta, usa la fecha de modificacion del servidor y, como ultimo recurso, la hora de consulta.

El repositorio y la pagina de GitHub Pages seran publicos. Publica ahi unicamente datos autorizados para consulta publica.
