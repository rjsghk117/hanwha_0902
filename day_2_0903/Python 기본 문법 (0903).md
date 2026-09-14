# Day 2: Python 문법

# Python 클래스(Class) & 객체(Object)

## 클래스란?
클래스(`class`)는 객체(`object`)를 만들기 위한 설계도이다.
간단한 비유로, 클래스를 **붕어빵 틀**로 비유할 수 있다.
빵틀 붕어빵이 아니라 붕어빵을 찍어내기 위한 틀일 뿐이다.

## 객체란?

객체는 설계도(붕어빵 틀)을 바탕으로 실제로 만들어진 결과물이다.
비유하자면, **붕어빵 틀로 찍어낸 붕어빵**이 객체에 해당하는 것이다.
같은 붕어빵 틀로 여러 개의 붕어빵을 만들 듯이 하나의 클래스로 여러 개의 객체를 만들 수 있는 것이다.

- 클래스: 실체가 없음
- 객체: 실체가 있음

**EXAMPLE**
```python
class fish():
    def __init__(self, flavor):
        self.flavor = flavor

fish1 = fish("팥")
fish2 = fish("슈크림")

print(fish1.flavor)
print(fish2.flavor)
```

**결과**
```
팥
슈크림
```
같은 클래스(`fish`)로 만들었지만, `fish1`과 `fish2`는 서로 다른 맛(`속성`)을 가진 객체이다.

**중요**
위의 예시 코드에 보이듯이 `def`와 `__init__` 매서드를 사용했다.

## def란?
`def`는 **함수(메서드)를 만들때 쓰는 키워드**이다.
이제부터 이런 동작을 하는 함수를 **정의**(`define`)하겠다는 뜻이다.

- `def 함수이름(매개변수):` 형태로 작성
- 함수 안에 들어갈 실행 코드는 한 칸 들여쓰기(indent)해서 작성
- 클래스 안에 정의된 함수는 특별히 `메서드(method)`라고 부름

**EXAMPLE**
```python
def greet(name):
    print(name + "님 안녕하세요")

greet("철수")
```

**결과**
```
철수님 안녕하세요
```
즉, `def greet(name):`은 `greet`라는 이름의, `name`이라는 값을 받는 함수를 만들겠다"는 뜻이고, 그 아래 들여쓰기된 `print(...)`가 실제로 이 함수가 실행할 내용이다.

**비유**

`def greet(name):` - "greet라는 이름의 레시피를 만들건데, 'name'이라는 재료가 필요해"

`들여쓰기된 print(...)` - "이 재료(name)를 가지고 실제로 할 행동"

`greet("철수")` - "greet 레시피에 '철수'라는 재료를 넣고 실행해"

**따라서** `greet("철수")`라고 실행하면 `name` 자리에 `철수`가 쏙 들어가서 `print("철수" + "님 안녕하세요")`가 실행 되는 것이다.

## `__init__`(initialize)이란?

위의 붕어빵 틀 예시로 돌아가, 붕어빵 틀에 반죽을 부으면 따로 모양을 만들지 않아도 틀에 맞게 
**자동**으로 붕어 모양으로 나온다. 

이것이 바로 `__init__`이다. 객체(`object`)를 만드는 순간 `(fish("팥")을 호출하는 순간)`, 파이썬이 **자동**으로 `__init__`을 실행해서 그 객체에 필요한 값을 채워 넣어준다.

**예시 코드**

```python
class fish():
    def __init__(self, flavor):
        self.flavor = flavor

fish1 = fish("팥")

print(fish1.flavor)
```

**결과**

```
팥
```

**비유**

`fish("팥")` - "fish 틀에 '팥' 반죽을 부어라"

`(자동실행) __init__(self, flavor)` - 반죽을 붓자마자 자동으로 실행되는 과정. "flavor"라는 재료로 "팥"이 전달

`self.flavor` = flavor - "지금 만들어지는 이 붕어빵(self)한테, 방금 받은 팥이라는 맛(flavor)을 부여

`결과` - fish1은 이제 flavor = "팥"을 가진 붕어빵(객체)이 됨

## 파이썬 문자열 (string)

**문자열 슬라이싱 (slicing)**

슬라이싱 구문을 사용하면 문자 범위를 반환할 수 있다.
문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스를 콜론(:)으로 구분하여 지정이 가능하다.

**EXAMPLE**

```python
b = "Hello, World!"
print(b[2:5])
```

**결과**

```
llo
```

**주의**

파이썬은 숫자를 셀때 0부터 시작한다.

**EXAMPLE**

파이썬 식 숫자 세기: `0, 1, 2, 3, 4, ...`

일반 숫자 세기: `1, 2, 3, 4, 5, ...`

**처음부터 자르기**

```python
b = "Hello, World!"
print(b[:5])
```

**결과**

```
Hello
```

**끝까지 자르기**

```python
b = "Hello, World!"
print(b[2:])
```

**결과**

```
llo, World!
```

**음수 인덱싱**

**EXAMPLE**

```python
b = "Hello, World!"
pirnt(b[-5:-2])
```

**결과**

```
orl
```

## 문자열 수정 (Modify Strings)

**대문자**

```python
a = "Hello, World!"
print(a.upper())
```

**결과**

```
HELLO, WORLD!
```

**소문자**

```python
a = "Hello, World!"
print(a.lower())
```

**결과**

```
hello, world!
```

**공백 제거 (strip)**

```python
a = " Hello, World "
print(a.strip())
```

**결과**

```
Hello, World!
```

## 문자열 바꾸기 (Replace String)

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

**결과**

```
Jello, World!
```

## 문자열 분할 (Split String)

```python
a = "Hello, World!"
b = a.split(",")
print(b)
```

**결과**

```
['Hello', 'World!']
```

## Streamlit 연습
