#!/usr/bin/env python3

import os
from PyPDF2 import PdfMerger
from pathlib import Path
import argparse

def concatenate_pdfs(folder_path: str, output_name: str = "merged.pdf") -> None:
    """
    Concatenate all PDFs in the specified folder.
    
    Args:
        folder_path (str): Path to the folder containing PDFs
        output_name (str): Name of the output PDF file (default: merged.pdf)
    """
    # Convert to Path object for better path handling
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist")
        return
    
    # Get all PDF files in the folder
    pdf_files = sorted([f for f in folder.glob("*.pdf")])
    
    if not pdf_files:
        print(f"No PDF files found in '{folder_path}'")
        return
    
    merger = PdfMerger()
    
    # Merge all PDFs
    for pdf in pdf_files:
        try:
            merger.append(str(pdf))
            print(f"Added: {pdf.name}")
        except Exception as e:
            print(f"Error processing {pdf.name}: {str(e)}")
            continue
    
    # Save the merged PDF
    output_path = folder / output_name
    try:
        merger.write(str(output_path))
        merger.close()
        print(f"\nSuccessfully created merged PDF: {output_path}")
    except Exception as e:
        print(f"Error saving merged PDF: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Concatenate PDF files in a folder")
    parser.add_argument("folder", help="Path to folder containing PDF files")
    parser.add_argument("-o", "--output", default="merged.pdf", help="Output filename (default: merged.pdf)")
    
    args = parser.parse_args()
    concatenate_pdfs(args.folder, args.output)

if __name__ == "__main__":
    main()
