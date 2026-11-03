# Visualizador Kardex para GitHub Pages

## Contenido del repositorio

Sube estos archivos a la raiz del nuevo repositorio: `index.html` y `data.json`. Conserva tambien `convertir_excel_a_json.py` y este README como apoyo.

`data.json` concentra las tres hojas del Excel en una sola fuente: `Tabla_resumen` como `summary`, `Dx_arch_clues` como `records` y `Acciones_sugeridas` como `actions`. El mapa y la interfaz permanecen en `index.html`.

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
2. Guarda el Excel actualizado como `data.xlsx` en `C:\Users\diego.velazquez.OPDIB\OneDrive - IMSS-BIENESTAR\Documentos\IMSS-B\35 Medicamentos tablero\Avance`. Ejecuta el conversor con Python y `openpyxl` instalado. La ruta ya está configurada como predeterminada, así que puedes correr el script sin argumentos; genera `data.json` en esa misma carpeta de OneDrive, junto al Excel. También acepta una ruta como argumento si algún día cambia la ubicación.
3. Reemplaza solo `data.json` en GitHub y confirma el cambio. La pagina lee el JSON al abrirse; no se actualiza mientras permanece abierta. El visitante puede recargarla para leer la version nueva. La fecha superior muestra la fecha de modificacion del servidor cuando esta disponible.

El repositorio y la pagina de GitHub Pages seran publicos. Publica ahi unicamente datos autorizados para consulta publica.
