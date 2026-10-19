"""Validate notebook JSON and compile every Python code cell without executing models."""
from pathlib import Path
import sys
import nbformat

ROOT = Path(__file__).resolve().parents[1]
notebooks = sorted(ROOT.glob("*/*.ipynb"))
if not notebooks:
    raise SystemExit("No notebooks found under the expected numbered folders.")

errors = []
code_cells = 0
for path in notebooks:
    try:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid notebook: {exc}")
        continue
    for index, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type != "code":
            continue
        code_cells += 1
        try:
            compile(cell.source, f"{path.name}:cell{index}", "exec")
        except SyntaxError as exc:
            errors.append(f"{path.relative_to(ROOT)}: cell {index}: {exc}")
    embedded_errors = [
        (index, output)
        for index, cell in enumerate(notebook.cells, start=1)
        if cell.cell_type == "code"
        for output in cell.get("outputs", [])
        if output.output_type == "error"
    ]
    for index, output in embedded_errors:
        errors.append(f"{path.relative_to(ROOT)}: stored error output in cell {index}: {output.get('ename', 'Error')}")

print(f"Checked {len(notebooks)} notebooks and {code_cells} code cells.")
if errors:
    print("Validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print("All notebook files are valid and all code cells compile.")
