from pdf2docx import Converter
pdf_file = 'ch2annex.pdf'
docx_file = 'informejr.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()