#넘파이(numpy)
#써드파티 라이브러리 (별도의 설치가 필요, 단 colab에는 기본 설치가 되어 있음
#파이썬에서 수치 계산을 위한 핵심 라이브러리, 다차원 배열 객체와 이를 다루기 위한 다양한 함수를 제공
#

import numpy as np

#arr = np.array(["Korean","English","Mathmatics"])
#arr = np.array([[1,2,3],[4,5,6]])
arr = np.array(
    [
        [
            [1.0,2.0,3.0],
            [4.2,5.9,9.1],
        ],
        [
            [4.0, 6.8, 8.2],
            [8.2, 4.1, 6.5],
        ]
    ]
)
print(arr)
print(arr.shape,arr.dtype,arr.ndim,arr.size)
#위 3차원 배열에 4.1만 출력
print(arr[1,1,1])#arr[1][1][1] << 이것도 가능은 한데 파이썬은 보통 콤마로 함