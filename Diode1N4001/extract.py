import numpy as np
import math

a = np.load('D1N4001.npy') # a 是ndarray类型，a.shape 返回一个空turple
data = a[()]  # 转化为内置字典类型
# # 用len()得到它的长度
v_source = []
c_measure =[]
for j, k in data.items():
    v_source.append(j)
    c_measure.append(k)
# print(c_measure)
TNOM = 27
index1 = 20
index2 = 30
v1 = v_source[index1]
i1 = abs(c_measure[index1])
print('first value get %s' %i1)
v2 = v_source[index2]
i2 = abs(c_measure[index2])
print('second value get %s' %i2)

# while(v_source[index] > 0.4):
#     index = index+1
#     v1 = v_source[index]
#     i1 = c_measure[index]
#     print('first value get %s' %i1)
#     break
#
# while(v_source[index] > 0.5):
#     index = index + 1
#     v2 = v_source[index]
#     i2 = c_measure[index]
#     print('second value get %s' %i2)
#     break

try:
 vt = 8.62e-5 * (TNOM + 273.15)
 N = 1 / vt * (v2-v1) / (math.log10(i2 / i1))
 Is = math.sqrt(i1 * i2)/math.exp((v1+v2)/(2*N*vt))
except BaseException:
    print("error")
print ('IS = %s  N = %s' % (Is, N))
