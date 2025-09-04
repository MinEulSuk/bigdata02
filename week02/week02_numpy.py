#넘파이(numpy)
#써드파티 라이브러리 (별도의 설치가 필요, 단 colab에는 기본 설치가 되어 있음
#파이썬에서 수치 계산을 위한 핵심 라이브러리, 다차원 배열 객체와 이를 다루기 위한 다양한 함수를 제공
#

import numpy as np

#zeros = np.zeros((3,4))
# zeros = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]],dtype=float)
# print(zeros)
#
# ones = np.ones((3,5))
# ones = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],dtype=float)
# print(ones)

range_array = np.array(20)
print(range_array)

space_array = np.linspace(0,1,5) # 0부터 1까지 숫자 5개로 구간 설정
print(space_array)