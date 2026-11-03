#!/usr/bin/env python3
"""Convert the Kardex workbook's three tabs into the single data.json used by the dashboard."""
import argparse
import json
from datetime import datetime
from pathlib import Path
import openpyxl

parser = argparse.ArgumentParser(description='Convert the Kardex Excel workbook to data.json')
parser.add_argument('workbook', nargs='?', help='Path to the source workbook (optional; defaults to OneDrive\\Avance\\data.xlsx)')
parser.add_argument('-o', '--output', help='Optional output JSON path (default: data.json beside the source workbook)')
args = parser.parse_args()
default_dir = Path(r'C:\Users\diego.velazquez.OPDIB\OneDrive - IMSS-BIENESTAR\Documentos\IMSS-B\35 Medicamentos tablero\Avance')
default_sources = [default_dir / 'data.xlsx', default_dir / 'data.xlsm']
if args.workbook:
    source = Path(args.workbook.strip().strip('\"').strip("'"))
else:
    source = next((candidate for candidate in default_sources if candidate.is_file()), default_sources[0])
output = Path(args.output) if args.output else default_dir / 'data.json'
if not source.is_file():
    raise SystemExit(f'Workbook not found: {source}')
wb = openpyxl.load_workbook(source, read_only=True, data_only=True)
required_sheets = ['Tabla_resumen', 'Dx_arch_clues', 'Acciones_sugeridas']
missing = [name for name in required_sheets if name not in wb.sheetnames]
if missing:
    raise SystemExit('Missing workbook sheets: ' + ', '.join(missing))

summary = []
for row in wb['Tabla_resumen'].iter_rows(min_row=2, values_only=True):
    if row[0] and isinstance(row[1], (int, float)):
        summary.append({'entidad': str(row[0]), 'invalido': int(row[1] or 0), 'valido': int(row[2] or 0), 'sinArchivo': int(row[3] or 0), 'total': int(row[4] or 0)})
fields = ['clues', 'entidad', 'tipologia', 'unidad', 'jurisdiccion', 'municipio', 'estado', 'motivo']
records = []
for row in wb['Dx_arch_clues'].iter_rows(min_row=2, values_only=True):
    if row and row[0]:
        records.append(dict(zip(fields, ['' if value is None else str(value) for value in row[:len(fields)]])))
actions = []
for row in wb['Acciones_sugeridas'].iter_rows(min_row=3, values_only=True):
    if row and row[0] and row[1]:
        actions.append({'motivo': str(row[0]), 'accion': str(row[1])})
payload = {'summary': summary, 'records': records, 'actions': actions, 'meta': {'source': source.name, 'generated': datetime.now().astimezone().isoformat(timespec='minutes')}}
output.write_text(json.dumps(payload, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
print(f'Created {output} ({len(summary)} summary rows, {len(records)} CLUES rows, {len(actions)} actions)')
