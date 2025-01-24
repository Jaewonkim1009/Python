import re

# 텍스트에서 코스 번호만 추출 해보자
text = '''101 COM PythonProgramming', '102 MAT LinearAIgebra', '103 ENG ComputerEnglish'''

i = re.findall('\d+',text)
print(i)