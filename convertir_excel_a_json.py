#!/usr/bin/env python3
"""Convert the Kardex workbook's three tabs into the single data.json used by the dashboard."""
import argparse
import json
import unicodedata
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

def header_key(value):
    text = unicodedata.normalize('NFKD', str(value or '')).encode('ascii', 'ignore').decode('ascii').lower()
    return ''.join(char for char in text if char.isalnum())

summary_sheet = wb['Tabla_resumen'].iter_rows(values_only=True)
summary_headers = [header_key(value) for value in next(summary_sheet)]
summary_columns = {'entidad': 'entidad', 'sinarchivo': 'sinarchivojson', 'valido': 'jsonvalido', 'invalido': 'jsoninvalido', 'total': 'total'}
summary_index = {key: summary_headers.index(header) for key, header in summary_columns.items() if header in summary_headers}
missing_summary = set(summary_columns) - set(summary_index)
if missing_summary:
    raise SystemExit('Missing summary columns: ' + ', '.join(sorted(missing_summary)))
summary = []
for row in summary_sheet:
    entity = row[summary_index['entidad']] if summary_index['entidad'] < len(row) else None
    if entity:
        summary.append({'entidad': str(entity), 'invalido': int(row[summary_index['invalido']] or 0), 'valido': int(row[summary_index['valido']] or 0), 'sinArchivo': int(row[summary_index['sinarchivo']] or 0), 'total': int(row[summary_index['total']] or 0)})
fields = ['clues', 'entidad', 'tipologia', 'unidad', 'jurisdiccion', 'municipio', 'estado', 'motivo']
records = []
for row in wb['Dx_arch_clues'].iter_rows(min_row=2, values_only=True):
    if row and row[0]:
        records.append(dict(zip(fields, ['' if value is None else str(value) for value in row[:len(fields)]])))
record_entities = {header_key(row['entidad']) for row in records if row['entidad']}
summary = [row for row in summary if header_key(row['entidad']) in record_entities]
actions = []
for row in wb['Acciones_sugeridas'].iter_rows(min_row=3, values_only=True):
    if row and row[0] and row[1]:
        actions.append({'motivo': str(row[0]), 'accion': str(row[1])})
payload = {'summary': summary, 'records': records, 'actions': actions, 'meta': {'source': source.name, 'generated': datetime.now().astimezone().isoformat(timespec='minutes')}}
output.write_text(json.dumps(payload, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
print(f'Created {output} ({len(summary)} summary rows, {len(records)} CLUES rows, {len(actions)} actions)')
sonora = next((row for row in summary if header_key(row['entidad']) == 'sonora'), None)
if sonora:
    print('SONORA counts: missing={sinArchivo}, valid={valido}, invalid={invalido}, total={total}'.format(**sonora))
