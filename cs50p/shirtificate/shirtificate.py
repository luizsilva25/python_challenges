from fpdf import FPDF

name = input('Name: ')
phrase = f'{name} took CS50'

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 40)
pdf.text(55, 25, text='CS50 Shirtificate')
pdf.image('shirtificate.png', 35, 50, w=140 )
pdf.set_font("helvetica", "B", 18)
pdf.set_text_color(255,255,255)
pdf.text(70, 100, text=phrase)
pdf.output('shirtificate.pdf')
