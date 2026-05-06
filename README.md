
# PDF Merger

Simple Python project to merge PDF files.

## Installation

```bash
pip install PyPDF2
```

## Run

```bash
python main.py
```

## Example

```python
from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("file1.pdf")
merger.append("file2.pdf")

merger.write("merged.pdf")
merger.close()
```

## Author

Sughosh Bhat
![image alt](pdf.png)
