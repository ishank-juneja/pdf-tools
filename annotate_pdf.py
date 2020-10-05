from pdf_annotate import PdfAnnotator, Location, Appearance
from pdf_annotate.config import constants
from pdf_annotate.graphics import ContentStream, Font
from PyPDF2 import PdfFileReader
import csv
import glob

# Parse the excel/csv file
with open('quiz1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        # Open the PDF file to be annotated        
        # print(row['Roll No.'], row['Q1'], row['Q3'])
        for pdf_file_name in glob.glob('exam01/{0}*'.format(row['Roll No.'])):
            # Get dimentions of page 0 of this PDF file
            pdf_obj = PdfFileReader(open(pdf_file_name, 'rb'))
            w = float(pdf_obj.getPage(0).mediaBox[2])
            h = float(pdf_obj.getPage(0).mediaBox[3])
            # Use w and h to place text boxes
            just_pdf_name = pdf_file_name.split('/')[1]
            a = PdfAnnotator(pdf_file_name)
            a.add_annotation(
                'text',
                # Through x1, x2, y1 and y2 we fix the corners of the text box but this has 
                # No bearing on the font size of the text itself
                Location(x1=0.6*w, y1=h - h/20, x2=0.6*w + w/10, y2=h - h/10 - h/20, page=0),
                Appearance(stroke_color=(1, 0, 0), stroke_width=10, 
                content="Q1: {0}\nQ3: {1}".format(row['Q1'], row['Q3']), 
                fill=[1, 0, 0], font_size=12*(w/600))
            )
            # a.add_annotation(
            #     'text',
            #     Location(x1=60, y1=50, x2=1000, y2=1000, page=0),
            #     Appearance(stroke_color=(1, 0, 0), stroke_width=8, content="Q3: {0}".format(row['Q3']), fill=(0.705, 0.094, 0.125, 1))
            # )
            a.write("exam01_out/{0}".format(just_pdf_name))
# a.write('annotated.pdf')  # or use overwrite=True if you feel             
    #     if line_count == 0:
    #         #print(f'Column names are {", ".join(row)}')
    #         #line_count += 1
    #         continue
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')

# a = PdfAnnotator('test.pdf')
# a.add_annotation(
#     'text',
#     Location(x1=50, y1=50, x2=100, y2=100, page=0),
#     Appearance(stroke_color=(1, 0, 0), stroke_width=5, content="hello world", fill=(0.705, 0.094, 0.125, 1))
# )
# a.write('annotated.pdf')  # or use overwrite=True if you feel 