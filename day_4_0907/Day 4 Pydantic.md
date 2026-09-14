# Pydantic

## Pydantic이란?

* 데이터 형식을 검증하고 관리해주는 Python Library
* **비유**: 데이터가 들어오기 전에 거르는 `거름망`

## 왜 필요한가?

* `Python`은 타입을 강제하지 않음 → 잘못된 값이 들어와도 `error` 없이 통과
* `Pydantic`은 이것을 미리 차단해서 `초기`에 문제를 발견

### BaseModel이란?

* `Pydantic Library` 안에 들어있는, **데이터 검증 기능을 가진 기본 class**
* 이걸 상속해서 나만의 `class`를 만들면, 그 클래스는 자동으로 `데이터가 맞는지 검사하는 능력`을 갖게 된다.

### 한 줄 정의

일반 `Python class`에 **타입 검증 + 자동 변환 + 데이터 변환 기능**을 자동으로 붙여주는 부모 클래스

**EXAMPLE**

```python
class JobApplication(BaseModel):
    company_name: str
    position: str
```

위의 예시에서 볼 수 있듯이, `company_name: str`은 그냥 주석이 아니라, Pydantic이 "이 필드는 문자열(str)이여야 한다"는 **규칙**으로 인식한다. 일반 `Python class`라면 이 타입 힌트는 그냥 참고용이라 무시되지만, `BaseModel`은 이걸 진짜 검증에 사용한다.

### 상속이란?

* 다른 클래스가 이미 만들어준 기능을 그대로 받아 쓰는 것
* 비유: 붕어빵 틀 - 이미 만들어진 틀`(BaseModel)`을 가져다가 내 모양`(JobApplication)`으로 커스텀하는 것

위의 예시 코드에서 `(BaseModel)` 부분이 상속어다. "`JobApplication`은 `BaseModel`의 기능을 물려받는다"는 뜻

### 상속하면 자동으로 딸려오는 것

* 타입 검증 (틀에 안 맞으면 에러)
* 자동 변환 ("20" → 20)
* `model_dump(), model_dump_json()` 같은 변환 기능

### 상속 안 하면?

* 타입 힌트를 적어도 그냥 참고용, 검증 안 됨
* 숫자 자리에 문자열 넣어도 에러 없이 통과됨

### 기본값 지정

* `Pydantic`은 필드에 기본값을 주느냐 안 주느냐로 "이 값이 꼭 있어야 하는지"를 판단
* 필드명: 타입 = 기본값
* 값을 안 넣으면 기본값 자동 적용

**EXAMPLE**
```python
class JobApplication(BaseModel):
    company_name: str
    position: str
    is_submitted: bool = False   # 값을 안 넣으면 자동으로 False

app = JobApplication(company_name="ABC상사", position="해외영업")
print(app.is_submitted)   # False (기본값 적용)
```
**결과**
```
False
```

### Field()로 조건 걸기

* `Field(min_length=1, max_length=50)` - 글자 길이 제한
* `Field(gt=0)` - 숫자 범위 제한 (0보다 커야 함)

**EXAMPLE**
```python
from pydantic import BaseModel, Field

class JobApplication(BaseModel):
    company_name: str = Field(min_length=1, max_length=50)
    salary: int = Field(gt=0)

app = JobApplication(company_name="ABC상사", salary=-100)
# 에러! salary가 0 이하라서 조건 위반
```
**결과**
```
ValidationError: 1 validation error for JobApplication
salary
Input should be greater than 0 [type=greater_than, input_value=-100, input_type=int]
```
### 중첩 모델

* 모델 안에 다른 모델을 필드로 넣기
* 딕셔너리를 넣어도 자동으로 객체 변환됨

**EXAMPLE**
```python
class Company(BaseModel):
    name: str
    industry: str

class JobApplication(BaseModel):
    company: Company   # Company 모델을 필드로 사용
    position: str

app = JobApplication(
    company={"name": "ABC상사", "industry": "무역"},   # 딕셔너리로 넣어도 자동 변환됨
    position="해외영업"
)
print(app.company.name)
```
**결과**
```
ABC상사
```
### field_validator로 커스텀 검증

* `Field()`로 표현 안 되는 복잡한 조건은 함수로 직접 검증

**EXAMPLE**
```python
from pydantic import BaseModel, field_validator

class JobApplication(BaseModel):
    company_name: str
    applied_date: str

    @field_validator("applied_date")
    def check_date_format(cls, value):
        if not value.startswith("2026"):
            raise ValueError("2026년도 지원 건만 입력 가능합니다")
        return value
app2 = JobApplication(company_name="XYZ무역", applied_date="2025-03-15")
```
**결과**
```
ValidationError: 1 validation error for JobApplication
applied_date
Value error, 2026년도 지원 건만 입력 가능합니다 [type=value_error, input_value='2025-03-15', input_type=str]
```
