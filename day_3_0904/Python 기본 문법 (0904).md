# Day 3: Python 문법

# Python 문자열 형실(String Format)

## F-String

`F-string`은 문자열 형식을 지정하는 데 권장하는 방법이다.

문자열을 `f-문자열`로 지정하려면 문자 리터럴 앞에 `f`를 붙이고 변수 및 기타 연산을 위한 자리 표시자로 `{}(중괄호)`를 추가하면 된다.

**EXAMPLE**

```python
age = 36
txt = f"My name is John, I am {age}."
print(txt)
```

**결과**

```
My name is John, I am 36.
```

## 자리 표시자와 수정자 (Placeholders & Modifiers)

자리 표시자는 변수, 연산, 함수 및 값 형식을 지정하는 수정자를 포함할 수 있다.

**EXAMPLE 1**

```python
price = 59
txt = f"The price is {price} dollars."
print(txt)
```

**결과**

```
The price is 59 dollars.
```

**EXAMPLE 2**

```python
price = 59
txt = f"The price is {price:.2f} dollars."
print(txt)
```

**결과**

```
The price is 59.00 dollars.
```

**알아야 할 점**

위의 예시 코드에서 `price` 뒤에 `:.2f`가 붙은걸 볼 수 있다.
`:.2f`의 역할은 소수점 이하 두 자리까지 표시되는 고정 소수점 숫자를 의미한다.

**EXAMPLE 3**

```python
txt = f"The price is {20*59} dollars."
print(txt)
```

**결과**

```
The price is 1180 dollars.
```

**알아야 할 점**

자리표시자`(Placeholder)`에는 수학 연산과 같은 파이썬 코드가 포함될 수 있다.

## 탈출 캐릭터 (Escape Character)

문자열 안에 큰 따옴표 (")나 줄바꿈처럼 원래는 코드 문법으로 쓰이는 문자를 **그냥 텍스트**로 넣고 싶을 때 사용한다.
백슬레시(\)를 앞에 붙여서 **이건 특별한 의미가 아니라 그냥 문자야**라고 알려주는 방식이다.

**EXAMPLE**

```python
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
```

**결과**

```
We are the so-called "Vikings" from the north.
```
## Python 문자열 capitalize() method

문장의 첫 글자를 대문자로, 나머지 글자는 소문자로 만들어주는 `method`이다.

**EXAMPLE 1**

```python
txt = "hello, welcome to my world"
x = txt.capitalize()
print(x)
```
**결과**

```
Hello, welcome to my world
```

**EXAMPLE 2**

```python
txt = "hello, WELCOME TO MY WORLD"
x = txt.capitalize()
print(x)
```
**결과**

```
Hello, welcome to my world
```

**주의**

숫자가 첫 글자인 경우 변화가 없다.

**EXAMPLE**

```python
txt = "36 is my age"
x = txt.capitalize()
print(x)
```

**결과**

```
36 is my age
```

## Python 문자열 center() method

단어를 지정한 너비 안에서 **가운데 정렬**하는 `method`이다.

**EXAMPLE**

```python
txt = "banana"
x = txt.center(20)
print(x)
```

**결과**
```
'       banana       '
```

## 좀 더 보기 쉽게 빈칸을 `'0'`으로 채워서 입력하는 방식

**EXAMPLE**

```python
txt = "banana"
x = txt.center(20, "0")
print(x)
```

**결과**

```
0000000banana0000000
```

## Python 문자열 find() method

이 문자열 `method`는 지정된 값의 첫 번째 발생 위치를 찾는다.

찾을 수 없는 경우 `-1`을 반환한다.

**EXAMPLE**

```python
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
```

**결과**
```
7
```

**찾을 수 없는 경우의 EXAMPLE**

```python
txt = "Hello, welcome to my world."
x = txt.find("wow")
print(x)
```

**결과**
```
-1
```

**찾는 값이 여러 개 있을 경우의 EXAMPLE**

```python
txt = "Hello, welcome to my world"
x = txt.find("e")
print(x)
```

**결과**

```
1
```

**주의**

결과가 `1`이 나오는 이유는 `"Hello, welcome to my world"`안에 `"e"`가 처음 나오는 자리가 `1`이기 때문에 `1`이라는 결과가 나온다.

**본문에서 찾는 범위를 지정해서 찾는 경우의 EXAMPLE**

```python
txt = "Hello, welcome to my world"
x = txt.find("e", 5, 10)
print(x)
```

**결과**

```
8
```

**주의**

이 명령어는 `"Hello, welcome to my world"`에서 5번째 위치부터 10번째 위치 사이에 `"e"`가 처음 나타나는 위치가 어디인지 알려준다.

## Python 문자열 upper() method

본문을 대문자로 바꿔준다.

**EXAMPLE**

```python
txt = "Hello, welcome to my world"
x = txt.upper()
print(x)
```

**결과**

```
HELLO, WELCOME TO MY WORLD
```

## Python 문자열 lower() method

본문을 소문자로 바꿔준다.

**EXAMPLE**

```python
txt = "HELLO, WELCOME TO MY WORLD"
x = txt.lower()
print(x)
```

**결과**

```
hello, welcome to my world
```

## Python 전역 변수 (Global Variable)

전역 변수는 함수 밖에서 선언되어, 코드 전체 어디서든 사용할 수 있는 변수이다.

**비유**

집에서 사용하는 냉장고를 생각해보면, 부엌에 냉장고를 두면, 안방에서도 거실에서도 집 어디서든 냉장고에 접근 할 수 있는 것을 생각하면 된다.

**EXAMPLE**

```python
x = "awesome"
def myfunc():
    print("Python is" + x)

myfunc()
```

**결과**

```
Python is awesome
```

**설명**

`x`는 함수 밖에서 만들어졌기 때문에, 함수 안에서도 밖에서도 자유롭게 접근할 수 있다.

## Python 지역 변수 (Local Variable)

함수 안에서 선언되어, 그 함수 안에서만 사용 가능한 변수이다.

**비유**

위의 비유에서 부엌에 냉장고를 두고 집 안 어디서든 접근 할 수 있었다면 (전역 변수), 지역 변수는 각자 방에 있는 미니 냉장고라고 생각하면 된다. 그 방 안에 있을 때만 저근 할 수 있고, 방 문을 닫고 나오면(함수가 끝나면) 더 이상 접근할 수 없다. 그리고 방 밖에서는 미니 냉장고가 있었다는 것을 알 수 없다.

**EXAMPLE**

```python
def make_juice():
    fruit = "strawberry"
    print(fruit)

make_juice()
print(fruit)
```

**결과**

```
NameError: name 'fruit' is not defined
```

**주의**

왜 에러가 뜨는가? `fruit`라는 변수는 `make_juice()` 함수 **안에서만** 만들어졌기 때문에, 함수가 실행을 끝내고 나면 사라진다. 함수 밖에서 `print(fruit)`를 하면 `"그 이름의 변수는 없다(NameError)"`라는 메세지가 출력된다.

**중요**

이 개념이 필요한 이유는 같은 이름의 변수를 여러 함수에서 각각 따로 써도 서로 충돌하지 않게 해주기 때문이다.

**EXAMPLE**

```python
def make_juice():
    fruit = "strawberry"
    print(fruit)

def make_smoothie():
    fruit = "banana"
    print(fruit)

make_juice()
make_smoothie()
```

**결과**

```
strawberry
banana
```
