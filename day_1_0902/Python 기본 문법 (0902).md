# Day 1: Python 기본 문법

# Python version 확인 방법
먼저 터미널에 
```bash
python --version
```
을 입력해 version을 확인해준다.

**주의**
여기서 주의해야 할 점은 본인이 `Python` 웹사이트에서 다운 받은 `version`과 터미널에서 확인할때 나오는 `version`이 같은지 확인해야한다.

**원인**
본인이 여러개의 `Python`을 설치해서 `version`이 다르게 나올 수도 있다. 따라서 `Python version`이 몇개 있는지 확인해야 한다.

# 가상환경 생성
```bash
python -m venv .firstvenv
```
를 입력해 가상환경을 만든다.

**만드는 이유**

프로젝트마다 필요한 패키지 버전이 다를 수 있는데,
가상환경 없이 작업하면 서로 충돌이 날 수 있다.
가상환경을 만드는 것은 독립된 공간을 만들어
분리하여 충돌을 막아주는 것이다.

# 가상환경 활성화 비활성화
가상환경에서 작업하기 원한다면 먼저 가상환경을 활성화 해야한다.

**방법**
왼쪽 목록에서 `Scripts`를 클릭 -
`activate.bat`을 우클릭 - 상대경로 복사 -
터미널에 우클릭으로 붙여넣기 

작업이 끝난 후 **비활성화** 해야한다.

**WHY?**

비활성화 하지 않은 상태에서 작업을 하면
어떤 환경에서 작업 중인지 헷갈릴 수 있다.

**방법**

활성화하는 방법과 동일하게 왼쪽 목록에서
`Scripts`를 클릭 -
`deactivate.bat`을 우클릭 -
상대경로 복사 - 터미널에 우클릭으로 붙여넣기

# 작업
위에 Code Editor에 명령어를 적은 후
터미널에 예를 들어 `python test.py`를 입력 후
`Enter` 버튼을 누르면 출력이 된다.

**주의**:
`Code Editor`에서 코드를 변경 후
`ctrl+s`를 눌러 저장을 해야만 변경사항이 적용된다.

# 변수 (Python Variables) 
데이터 값을 저장하는 컨테이너

## 변수 생성 (Creating Variables)
파이썬에는 변수를 선언하는 명령어가 없기 때문에
해당 변수에 처음으로 값을 할당해야 한다.

**EXAMPLE**
```python
x = 5
y = "John"
print(x)
print(y)
```

**결과**
```
5
John
```

# 데이터 유형 (Data Types)
- Text Type: str (문자열/string)
- Numeric Types: int (정수/Integer)
                float (부동소수점수/Floating Point Number)
                complex (복소수/Complex Number)
- Sequence Types: list (리스트/List)
                  tuple (튜플/Tuple)
                  range (레인지/Range)
- Mapping Type: dict (딕셔너리/Dictionary)
- Boolean Type: bool (불리언/Boolean)

# 데이터 유형 갖고오기 (Getting the Data Type)
Python에서 데이터의 유형을 가져올 수 있다.

**EXAMPLE**
```python
x = 5
print(type(x))
```

**결과**
```
<class 'int'>
```

# Day 1 연습
## 변수를 이용한 연습
**EXAMPLE**
```python
title = "AI 서비스 백엔드 프로그래밍 실무"
line = "=========="
time = 8
a = "파이썬 기본 문법, 시간"
b = "클래스"
c = "데코레이터"
d = "예외 처리"
e = "로깅"
print(title)
print(line)
print(a, time, sep=", 시간:")
print(b, time, sep=", 시간:")
print(c, time, sep=", 시간:")
print(d, time, sep=", 시간:")
print(e, time, sep=", 시간:")
```

**결과**
```
AI 서비스 백엔드 프로그래밍 실무
==========
파이썬 기본 문법, 시간, 시간:8
클래스, 시간:8
데코레이터, 시간:8
예외 처리, 시간:8
로깅, 시간:8
```

## 리스트를 이용한 연습

**EXAMPLE**
```python
title = "AI 서비스 백엔드 프로그래밍 실무"
line = "=========="
time = 8
myList = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]
print(title)
print(line)
print(myList[0], time)
print(myList[1], time)
print(myList[2], time)
print(myList[3], time)
print(myList[4], time)
```

**결과**
```
AI 서비스 백엔드 프로그래밍 실무
==========
파이썬 기본 문법 8
클래스 8
데코레이터 8
예외 처리 8
로깅 8
```

## For문을 이용한 연습
**EXAMPLE**
```python
title = "AI 서비스 백엔드 프로그래밍 실무"
line = "=========="
time = 8
myList = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"]
print(title)
print(line)

for x in myList:
    print(x, time, sep=", 시간:")
```

**결과**
```
AI 서비스 백엔드 프로그래밍 실무
==========
파이썬 기본 문법, 시간:8
클래스, 시간:8
데코레이터, 시간:8
예외 처리, 시간:8
로깅, 시간:8
```
