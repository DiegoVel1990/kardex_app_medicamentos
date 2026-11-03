# Visualizador Kardex: paquete para GitHub Pages

## Archivos

- `index.html`: visualizador.
- `data.csv`: fuente reemplazable, una fila por CLUES.

## Publicación inicial

1. Crea un repositorio público en GitHub y sube ambos archivos a la raíz.
2. En **Settings → Pages**, selecciona publicar desde la rama `main`, carpeta `/ (root)`.
3. Comparte la URL que GitHub Pages muestre, normalmente `https://USUARIO.github.io/REPOSITORIO/`, con la persona que administra WordPress.
4. Esa persona agrega una sola vez un bloque HTML con un `iframe` que apunte a esa URL.

```html
<iframe src="https://USUARIO.github.io/REPOSITORIO/" title="Avance Kardex por estado" loading="lazy" style="display:block;width:100%;height:1100px;border:0"></iframe>
```

## Actualizar los datos

1. En el Excel actualizado, exporta la hoja `Dx_arch_clues` como CSV UTF-8. Debe contener los campos de CLUES, entidad, tipología, unidad, jurisdicción, municipio, estado y motivo. El lector acepta encabezados con acentos y separador coma o punto y coma.
2. Reemplaza `data.csv` en la raíz del mismo repositorio conservando el nombre y confirma el cambio. No edites `index.html`.
3. GitHub Pages publicará de nuevo el sitio; al visitar o recargar la página, el visualizador vuelve a solicitar `data.csv` evitando la caché del navegador. La lectura ocurre al abrir o recargar la página; no hay consultas automáticas mientras permanece abierta. La fecha superior usa `Last-Modified` del servidor cuando está disponible; si no, indica la hora de consulta.

El lector reconoce los encabezados originales de la hoja (`CLUES`, `ENTIDAD`, `NOMBRE DE TIPOLOGIA`, `NOMBRE DE LA UNIDAD`, `JURISDICCION`, `MUNICIPIO`, `Estado`, `Motivo`) o sus nombres normalizados. El resumen por entidad se calcula automáticamente a partir de las filas del CSV. Las geometrías del mapa y el catálogo de acciones recomendadas permanecen en `index.html`; si cambian las recomendaciones, también habrá que editar el HTML. El repositorio y la página de GitHub Pages serán públicos: publica ahí únicamente datos autorizados para consulta pública.
