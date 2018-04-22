# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-
import numpy as np 
import pandas as pd


df = pd.read_csv("DSBNNGTTHANG2BVEKETHUOC.csv", header = 0)




def bt(name):
	x = np.unique(df[name].dropna())
	return x

def save_file(file_name, bt):
	f = open(file_name, 'w', encoding="utf-8")
	f.write('\n'.join(str(n) for n in bt))
	f.close()

file = {'MABENH': 'benh.txt', 'TENTHUOC':'thuoc.txt', 'MALSVV': 'don_thuoc.txt'}
for key, value in file.items():
	save_file(value, bt(key))
	print(key + ':'  + str(len(bt(key))))




def matrix_benh_thuoc(df):
	matrix_bt = np.zeros((len(bt('MABENH')), len(bt('TENTHUOC'))), dtype = float)
	for benh in bt('MABENH'):
		id_benh = list(bt('MABENH')).index(benh)
		prescription = df.loc[df['MABENH'] == benh][['MALSVV', 'TENTHUOC']]
		count_donthuoc = len(prescription['MALSVV'].unique())
		for thuoc in prescription['TENTHUOC'].unique():
			id_thuoc = list(bt('TENTHUOC')).index(thuoc)
			count_thuoc = (prescription['TENTHUOC'] == thuoc).sum()
			matrix_bt[id_benh,id_thuoc] = float(count_thuoc/count_donthuoc)
			print(float(count_thuoc/count_donthuoc))
	return matrix_bt
			
np.savetxt('matrix_bt.txt', matrix_benh_thuoc(df), fmt = '%.5e')
print(matrix_benh_thuoc(df))	


# def matrix_thuoc_thuoc(df):
# 	matrix_tt = np.zeros((len(bt('TENTHUOC')), len(bt('TENTHUOC'))), dtype = int)
# 	list_donthuoc = bt('MALSVV')
# 	for prescription in list_donthuoc:
# 		list_thuoc = list(df.loc[df['MALSVV'] == prescription]['TENTHUOC'])
# 		while len(list_thuoc) > 0:
# 			index_t0 = list(bt('TENTHUOC')).index(list_thuoc[0])
# 			for index_t in list_thuoc:
# 				index_t1 = list(bt('TENTHUOC')).index(index_t)
# 				if index_t0 != index_t1:
# 					matrix_tt[index_t0, index_t1] += 1				
# 					matrix_tt[index_t1, index_t0] += 1
# 			list_thuoc.pop(0)
# 	return matrix_tt

# np.savetxt('matrix_tt.txt', matrix_thuoc_thuoc(df), fmt = '%.d')

def matrix_donthuoc(df):
	matrix_donthuoc = np.zeros((len(bt('TENTHUOC')), len(bt('MALSVV'))), dtype = int)
	for row in range(len(df['MALSVV'])):
		print(row)
		id_thuoc = list(bt('TENTHUOC')).index(df['TENTHUOC'][row])
		id_donthuoc = list(bt('MALSVV')).index(df['MALSVV'][row])
		matrix_donthuoc[id_thuoc, id_donthuoc] += 1
	return matrix_donthuoc
np.savetxt('matrix_donthuoc.txt', matrix_donthuoc(df), fmt = '%.d')
