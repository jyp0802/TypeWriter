# TypeWriter
TypeWriter is project for converting text to hand-writing PNG file.

## 1. Introduction
TypeWriter는 손글씨를 사랑하는 사람들을 위해 만들었습니다. 자신의 손글씨를 포함하는 PNG 파일을 읽어서 각 글자 데이터로 받아옵니다. 그 다음, 임의의 텍스트 파일을 읽어, 자신의 손글씨를 담은 PNG 파일을 생성하여 자신이 직접 쓴 것 처럼 모방합니다.

## 2. Library
* Python 3.6
    - Numpy
    - PIL
    - scipy


## 3. Code
### 3.1 image_parser.py
image_parser.py는 같은 경로에 있는 original.png 파일을 읽어 a-z, A-Z를 읽어 오는 스크립트입니다.
- a-z 순으로 한 줄, A-Z 순으로 한 줄이 적혀있는 PNG 파일을 입력하면 각 글자 별 파일이 현재 경로에 (알파벳)(0또는 c).PNG 파일로 저장 됩니다. (0의 경우 소문자, c의 경우 대문자)

### 3.2 imagetopdf.py
imagetopdf.py는 같은 경로에 있는 data.txt 파일을 읽어, 손글씨 데이터가 입력된 result.png를 출력하는 스크립트입니다.
### 3.3 dynamic_search.py

### 3.4 thinning_function_class.py
### 3.5 thinning_function.py


## 4. Application

### 4.1 GhostWriter
![Alt GhostWriter Step.1](https://i.imgur.com/2xsl41k.png)
![Alt GhostWriter Step.2](https://i.imgur.com/mui60fy.png)
![Alt GhostWriter Step.3](https://i.imgur.com/PwmJDZ5.png)