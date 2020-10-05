from PyPDF2 import PdfFileReader
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
import csv
import glob

# Parse the excel/csv file
with open('quiz1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        # Open the PDF file to be annotated        
        # print(row['Roll No.'], row['Q1'], row['Q3'])
        for pdf_file_name in glob.glob('exam01/{0}*'.format(row['Roll No.'])):
            canvas = Canvas("font-colors.pdf", pagesize=LETTER)
            # Set font to Times New Roman with 12-point size
            canvas.setFont("Times-Roman", 12)
            # Draw blue text one inch from the left and ten
            # inches from the bottom
            canvas.setFillColor(blue)
            canvas.drawString(1 * inch, 10 * inch, "Blue text")
            # Save the PDF file
            canvas.save()
            content="Q1: {0}\nQ3: {1}".format(row['Q1'], row['Q3'], font_size=1)