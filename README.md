# PDF Concatenator

Simple Python script to merge multiple PDF files in a directory into a single PDF.

## Requirements

- Python 3.x
- PyPDF2

## Setup

1. Create a virtual environment:
```bash
python3 -m venv .venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install PyPDF2
```

## Usage

```bash
python concat-pdf.py <folder_path> -o output_name.pdf]
```

### Examples

Merge all PDFs in current directory:
```bash
python concat-pdf.py . -o merged.pdf
```

Merge PDFs from specific folder:
```bash
python concat-pdf.py ./my_pdfs -o final.pdf
```

### Arguments

- `folder`: Path to folder containing PDF files (required)
- `-o, --output`: Output filename (optional, defaults to "merged.pdf")

## Notes

- PDFs are merged in alphabetical order
- The script will skip any PDF files that cause errors during processing
- The merged PDF will be saved in the same folder as the input PDFs 