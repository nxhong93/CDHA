import numpy as np
from math import sqrt
import pandas as pd
import operator
from scipy.sparse.linalg import svds
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.model_selection import train_test_split


def load_data(file_name):
    name = open(file_name, 'r', encoding="utf-8")
    name = name.read().split('\n')
    return name

def matrix(file_matrix):
    maxt = np.loadtxt(file_matrix, dtype = float)
    return maxt

if __name__ == "__main__":

    list_benh = load_data('benh.txt')
    list_thuoc = load_data('thuoc.txt')
    matrix_benh_thuoc = matrix('matrix_bt.txt')
    matrix_donthuoc = matrix('matrix_donthuoc.txt')
    matrix_tt1 = 1 - pairwise_distances(matrix_benh_thuoc.T, metric='cosine')
    matrix_tt2 = 1 - pairwise_distances(matrix_donthuoc, metric='cosine')
    matrix_tt = matrix_tt1*matrix_tt2

    print ("Số bệnh = " + str(len(list_benh)) + " | Số thuốc = " + str(len(list_thuoc)))




    def ten_bt(matrix, ma_bt, list_bt, rand_bt): 
        index_bt = list(list_bt).index(ma_bt)
        matrix_bt = list(matrix[index_bt,:])
        z = {}
        for i in range(len(list_thuoc)):
            if matrix_bt[i] > 0:
                z[list_thuoc[i]] = matrix_bt[i]
        s = sorted(z.items(), key=operator.itemgetter(1),reverse=True)
        name_bt = []
        rate_bt = []
        kq = {}
        for v, k in s[:rand_bt]:
            name_bt.append(v)
            rate_bt.append(k)
            kq[v] = k
        return kq

    def tap_thuoc(ma_benh):
        if ma_benh == 'j00':
            return ten_bt(matrix_benh_thuoc, ma_benh,list_benh, 10)
        else:
            return ten_bt(matrix_benh_thuoc, ma_benh.upper(),list_benh, 10)

     

    while 0 == 0:
        name_input = input('Mã bệnh:\n')
        try:
            similarity_test = tap_thuoc(name_input)
            print('Thuốc:')
            for key, value in similarity_test.items():
                t_similarity = list(ten_bt(matrix_tt, key,list_thuoc, 4).keys())
                print (('%s: %.3f%%(tương ứng thuốc: %s)') %(key, 100*value, ','.join(t_similarity[1:])))
        except:
            print('Không tìm thấy kết quả!')