# NumPy

## NumPy란?

* 숫자 배열(array)을 빠르고 효율적으로 계산해주는 Python Library
* 비유: 파이썬 리스트가 "한 줄씩 계산하는 계산기"라면, NumPy는 "전체를 한 번에 계산하는 계산기"

## 왜 필요한가?

* 파이썬 리스트로 숫자를 계산하려면 반복문(for)이 필요함 → 느림
* NumPy는 반복문 없이 배열 전체에 한 번에 연산 적용 가능 (벡터화, Vectorization) → 빠름

**EXAMPLE 1**
```python
# 파이썬 리스트 - 반복문 필요
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers]
print(result)
```
**결과**
```
[2, 4, 6, 8, 10]
```
**EXAMPLE 2**
```python
# NumPy 배열 - 반복문 없이 한 번에 계산
import numpy as np
numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2
print(result)
```
**결과**
```
[2 4 6 8 10]
```

## ndarray란?

* NumPy의 핵심 자료구조, N차원 배열(N-dimensional array)이라는 뜻
* 1차원(리스트 형태), 2차원(표/행렬 형태) 등 자유롭게 표현 가능

**EXAMPLE**
```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
print(arr2)
```
**결과**

```
[1 2 3]
[[1 2 3]
 [4 5 6]]
```
### 배열 정보 확인

* `.shape` - 몇 행 몇 열인지
* `.ndim` - 몇 차원인지
* `.dtype` - 데이터 타입이 뭔지

**EXAMPLE**
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)
print(arr.ndim)
print(arr.dtype)
```
**결과**
```
(2, 3)
2
int64
```
### 배열 생성 함수

* `np.zeros((2,3))` - 0으로 채운 배열
* `np.ones((2,3))` - 1로 채운 배열
* `np.arange(0,10,2)` - 0부터 10 전까지 2씩 증가
* `np.linspace(0,1,5)` - 0부터 1까지 5개 구간으로 균등 분할

**EXAMPLE**
```python
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
```
**결과**
```
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 1. 1.]
 [1. 1. 1.]]
[0 2 4 6 8]
[0.   0.25 0.5  0.75 1.  ]
```
### 사칙연산 (벡터화)

* 같은 위치끼리 자동으로 계산됨 (반복문 불필요)

**EXAMPLE**
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(a.sum())
print(a.mean())
```
**결과**
```
[5 7 9]
[4 10 18]
6
2.0
```
### 인덱싱과 슬라이싱

* 리스트와 비슷하지만, 다차원 배열도 콤마(,)로 한 번에 접근 가능

**EXAMPLE**
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[0])
print(arr[0, 1])
print(arr[:, 0])
```
**결과**
```
[1 2 3]
2
[1 4]
```
## 파이썬 리스트 vs NumPy 배열

| 구분 | 파이썬 리스트 | NumPy 배열 |
|---|---|---|
| 속도 | 느림 (반복문 필요) | 빠름 (벡터화 연산) |
| 데이터 타입 | 섞여도 됨 | 한 가지 타입으로 통일 |
| 다차원 처리 | 불편함 | 직관적 |

## 왜 AI 공부에서 나올까?

* `Pandas`가 내부적으로 `NumPy` 기반으로 동작
* AI 모델의 임베딩 벡터, 행렬 연산이 `NumPy` 배열 형태
* `RAG`에서 문서를 벡터로 변환해 검색하는 과정에도 `NumPy` 연산이 기반