print("hola mundo")
print(f"Hola, {{ usuario }}!")

devengo = pd.DataFrame()
for f in glob.glob('/Users/hector/Downloads/80 BIS.xlsx'): # "../mejorninez/input_excel/pagoManual/*",
	df = pd.read_excel(f, converters={ 'folio': str, 'Nº CDP': str, 'Monto Total': int } )
	print('Procesando  : ', f)
	devengo = pd.concat([devengo, df], ignore_index=True)
print(devengo)
