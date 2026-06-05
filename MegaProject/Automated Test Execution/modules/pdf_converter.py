from docx2pdf import convert


class PDFConverter:

    @staticmethod
    def convert_to_pdf(docx_file, pdf_file):

        try:

            convert(docx_file, pdf_file)

            print("PDF Generated Successfully")

        except Exception as e:

            print(f"PDF Generation Failed: {e}")