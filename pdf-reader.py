from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def read_pdf(pdf_file):
    resource_manager = PDFResourceManager()
    resource_str = StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, resource_str, laparams=laparams)

    process_pdf(resource_manager, device, pdf_file)
    device.close()

    content = resource_str.getvalue()
    resource_str.close()
    return content


pdf_file = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
output_string = read_pdf(pdf_file)
print(output_string)
pdf_file.close()