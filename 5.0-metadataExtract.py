""" Python2 code to extract information(metadata) about the pdf file """

#Python2 module 
import pyPdf

def main():
	#location of the pdf file
	filename = "term.pdf" 

	#opening and extracting the information from the file
	pdfFile = pyPdf.PdfFileReader(file(filename,'rb'))
	data = pdfFile.getDocumentInfo()

	print("----- Metadata of the file -----")

	#printing the metadata information
	for metadata in data:
		print metadata+ " " +data[metadata]


if __name__ == '__main__':
	main()