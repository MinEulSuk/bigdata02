#넘파이(numpy)
#써드파티 라이브러리 (별도의 설치가 필요, 단 colab에는 기본 설치가 되어 있음
#파이썬에서 수치 계산을 위한 핵심 라이브러리, 다차원 배열 객체와 이를 다루기 위한 다양한 함수를 제공
#

import numpy as np

arr = np.array([1,2,3,4,5])
# indexing
print(arr[2])
print(arr[4],arr[-1],arr[len(arr)-1])

#slicing
print(arr[1:3])
print(arr[::3])