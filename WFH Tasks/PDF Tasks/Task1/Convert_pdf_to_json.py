import json
import coercion
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1

def pdf_to_json_data(file_name):
    parser = PDFParser(open(file_name, 'rb'))
    doc = PDFDocument(parser)
    data = resolve1(doc.catalog['AcroForm'], default=None)['Fields']
    
    # numbers of page counts
    nums_pages = resolve1(doc.catalog['Pages'], default=None)['Count']
    count = 0

    # for making document.pagecount field in dictionary dict1
    dict1 = {"document.pagecount":nums_pages}
    
    for x in data:
        perticular_field = resolve1(x)
        key, value = perticular_field.get('T'), perticular_field.get('V')
        dict1[key] = value
        count += 1

    # for making document.fieldcount field in dictionary dict1
    dict1["document.fieldcount"] =  count
    main_data = {"map":coercion.normalize_collection(dict1)}
    # for encoding dictionary data to JSON data
    json_data = json.dumps(main_data)
    return json_data

file_name = input("Enter pdf file name with extension .pdf: ")
print(pdf_to_json_data(file_name))
