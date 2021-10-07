#!/usr/bin/env python
# coding: utf-8


# h 타이핑하면 주피터 노트북 사용법  / a b 는 추가 dd는 삭제 / 셀 실행은 커맨드 엔터


from bs4 import BeautifulSoup
import requests
a = [1, 2, 3, 4, 5]
for index, num in enumerate(a):
    print(index, num)
# 기본적으로 for 에 리스트를 순회할 경우 값만 추출하는데
# enumerate 메소드를 사용시 전부가능


def mean(nums):
    return sum(nums) / len(nums)


# 소수판별
def is_prime(num):
    a = 0
    for i in range(2, num+1):
        if num % i == 0:
            a += 1
    return a


print(is_prime(7))
print(is_prime(5))
print(is_prime(17))
print(is_prime(3))


#  #### **Class Inheritance (상속)**
#   - 기존에 정의해둔 클래스의 기능을 그대로 물려받을 수 있다.
#   - 기존 클래스에 기능 일부를 추가하거나, 변경하여 새로운 클래스를 정의한다.
#   - 코드를 재사용할 수 있게된다.
#   - 상속 받고자 하는 대상인 기존 클래스는 (Parent, Super, Base class 라고 부른다.)
#   - 상속 받는 새로운 클래스는(Child, Sub, Derived class 라고 부른다.)
#   - 의미적으로 is-a관계를 갖는다

# #### **method override**
#  - 부모 클래스의 method를 재정의(override)
#  - 하위 클래스(자식 클래스) 의 인스턴스로 호출시, 재정의된 메소드가 호출됨


# #### super
#  - 하위클래스(자식 클래스)에서 부모클래스의 method를 호출할 때 사용


# #### **self**
#  - 파이썬의 method는 항상 첫번째 인자로 self를 전달
#  - self는 현재 해당 메쏘드가 호출되는 객체 자신을 가리킴
#  - C++/C#, Java의 this에 해당
#  - 역시, 이름이 self일 필요는 없으나, 위치는 항상 맨 처음의 parameter이며 관례적으로 self로 사용


# #### **method type**
#  - instance method - 객체로 호출
#    - 메쏘드는 객체 레벨로 호출 되기 때문에, 해당 메쏘드를 호출한 객체에만 영향을 미침
#  - class method    - class로 호출
#        - 클래스 메쏘드의 경우, 클래스 레벨로 호출되기 때문에, 클래스 멤버 변수만 변경 가능
#


# #### **special method**
#  - __로 시작 __로 끝나는 특수 함수
#  - 해당 메쏘드들을 구현하면, 커스텀 객체에 여러가지 파이썬 내장 함수나 연산자를 적용 가능
#  - 오버라이딩 가능한 함수 목록은 아래 링크에서 참조
#    - https://docs.python.org/3/reference/datamodel.html


# #### 연습문제)
#  - 복소수 클래스를 정의 해봅시다.
#  - 덧셈, 뺄셈, 곱셈 연산자 지원
#  - 길이 (복소수의 크기) 지원
#  - 복소수 출력 '1 + 4j'와 같이 표현
#  - 비교 연산 ==, != 지원
#  - >=, <= , <, > 연산 지원
#  - 절대값 지원
#

#!/usr/bin/env python
# coding: utf-8


# * 정규표현식
#  - regular expression
#  - 특정한 패턴과 일치하는 문자열를 '검색', '치환', '제거' 하는 기능을 지원
#  - 정규표현식의 도움없이 패턴을 찾는 작업(Rule 기반)은 불완전 하거나, 작업의 cost가 높음
#  - e.g) 이메일 형식 판별, 전화번호 형식 판별, 숫자로만 이루어진 문자열 등

# * **raw string**
#  - 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 변환

# #### **기본 패턴**
#  - a, X, 9 등등 문자 하나하나의 character들은 정확히 해당 문자와 일치
#    - e.g) 패턴 test는 test 문자열과 일치
#    - 대소문자의 경우 기본적으로 구별하나, 구별하지 않도록 설정 가능
#  - 몇몇 문자들에 대해서는 예외가 존재하는데, 이들은 틀별한 의미로 사용 됨
#    - . ^ $ * + ? { } [ ] \ | ( )
#
#  - . (마침표) - 어떤 한개의 character와 일치 (newline(엔터) 제외)
#
#  - \w - 문자 character와 일치 [a-zA-Z0-9_]
#  - \s - 공백문자와 일치
#  - \t, \n, \r - tab, newline, return
#  - \d - 숫자 character와 일치 [0-9]
#  - ^ = 시작, $ = 끝 각각 문자열의 시작과 끝을 의미
#  - \가 붙으면 스페셜한 의미가 없어짐. 예를들어 \\.는 .자체를 의미 \\\는 \를 의미
#  - 자세한 내용은 링크 참조 https://docs.python.org/3/library/re.html

# #### **search method**
#  - 첫번째로 패턴을 찾으면 match 객체를 반환
#  - 패턴을 찾지 못하면 None 반환

# #### **metacharacters (메타 캐릭터)**

# #### **[]** 문자들의 범위를 나타내기 위해 사용
#    - [] 내부의 메타 캐릭터는 캐릭터 자체를 나타냄
#    - e.g)
#    - [abck] : a or b or c or k
#    - [abc.^] : a or b or c or . or ^
#    - [a-d]  : -와 함께 사용되면 해당 문자 사이의 범위에 속하는 문자 중 하나
#    - [0-9]  : 모든 숫자
#    - [a-z]  : 모든 소문자
#    - [A-Z]  : 모든 대문자
#    - [a-zA-Z0-9] : 모든 알파벳 문자 및 숫자
#    - [^0-9] : ^가 맨 앞에 사용 되는 경우 해당 문자 패턴이 아닌 것과 매칭

# #### **\**
#  1. 다른 문자와 함께 사용되어 특수한 의미를 지님
#    - \d : 숫자를          [0-9]와 동일
#    - \D : 숫자가 아닌 문자  [^0-9]와 동일
#    - \s : 공백 문자(띄어쓰기, 탭, 엔터 등)
#    - \S : 공백이 아닌 문자
#    - \w : 알파벳대소문자, 숫자 [0-9a-zA-Z]와 동일
#    - \W : non alpha-numeric 문자 [^0-9a-zA-Z]와 동일
#  2. 메타 캐릭터가 캐릭터 자체를 표현하도록 할 경우 사용
#    - \\. , \\\
#

# #### **.**
#  - 모든 문자를 의미

# #### **반복패턴**
#  - 패턴 뒤에 위치하는 *, +, ?는 해당 패턴이 반복적으로 존재하는지 검사
#    - '+' -> 1번 이상의 패턴이 발생
#    - '*' -> 0번 이상의 패턴이 발생
#    - '?' -> 0 혹은 1번의 패턴이 발생
#  - 반복을 패턴의 경우 greedy하게 검색 함, 즉 가능한 많은 부분이 매칭되도록 함
#   - e.g) a[bcd]*b  패턴을 abcbdccb에서 검색하는 경우
#     - ab, abcb, abcbdccb 전부 가능 하지만 최대한 많은 부분이 매칭된 abcbdccb가 검색된 패턴


# #### **^**, **$**
#  - ^  문자열의 맨 앞부터 일치하는 경우 검색
#  - \$  문자열의 맨 뒤부터 일치하는 경우 검색


#  #### **grouping**
#   - ()을 사용하여 그루핑
#   - 매칭 결과를 각 그룹별로 분리 가능
#   - 패턴 명시 할 때, 각 그룹을 괄호() 안에 넣어 분리하여 사용


#  #### **{}**
#   - *, +, ?을 사용하여 반복적인 패턴을 찾는 것이 가능하나, 반복의 횟수 제한은 불가
#   - 패턴뒤에 위치하는 중괄호{}에 숫자를 명시하면 해당 숫자 만큼의 반복인 경우에만 매칭
#   - {4} - 4번 반복
#   - {3,4} - 3 ~ 4번 반복


# #### **미니멈 매칭(non-greedy way)**
#  - 기본적으로 *, +, ?를 사용하면 greedy(맥시멈 매칭)하게 동작함
#  - *?, +?을 이용하여 해당 기능을 구현


# #### **{}?**
#  - {m,n}의 경우 m번 에서 n번 반복하나 greedy하게 동작
#  - {m,n}?로 사용하면 non-greedy하게 동작. 즉, 최소 m번만 매칭하면 만족


# #### **match**
#  - search와 유사하나, 주어진 문자열의 시작부터 비교하여 패턴이 있는지 확인
#  - 시작부터 해당 패턴이 존재하지 않다면 None 반환


# #### **findall**
#  - search가 최초로 매칭되는 패턴만 반환한다면, findall은 매칭되는 전체의 패턴을 반환
#  - 매칭되는 모든 결과를 리스트 형태로 반환


# #### **sub**
#  - 주어진 문자열에서 일치하는 모든 패턴을 replace
#  - 그 결과를 문자열로 다시 반환함
#  - 두번째 인자는 특정 문자열이 될 수도 있고, 함수가 될 수 도 있음
#  - count가 0인 경우는 전체를, 1이상이면 해당 숫자만큼 치환 됨


# #### **compile**
#  - 동일한 정규표현식을 매번 다시 쓰기 번거로움을 해결
#  - compile로 해당표현식을 re.RegexObject 객체로 저장하여 사용가능


# ### 연습문제
#   - 아래 뉴스에서 이메일 주소를 추출해 보세요
#   - 다음중 올바른 (http, https) 웹페이지만 찾으시오


# 위의 두 모듈이 없는 경우에는 pip install requests bs4 실행


def get_news_content(url):
    response = requests.get(url)
    content = response.text

    soup = BeautifulSoup(content, 'html5lib')

    div = soup.find('div', attrs={'id': 'harmonyContainer'})

    content = ''
    for paragraph in div.find_all('p'):
        content += paragraph.get_text()

    return content


news1 = get_news_content('https://news.v.daum.net/v/20190617073049838')
print(news1)


webs = ['http://www.test.co.kr',
        'https://www.test1.com',
        'http://www.test.com',
        'ftp://www.test.com',
        'http:://www.test.com',
        'htp://www.test.com',
        'http://www.google.com',
        'https://www.homepage.com.']
##
