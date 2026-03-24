# Example: Anthropic Prompt Engineering Tutorial

이 예시는 Anthropic이 공개한 프롬프트 엔지니어링 강의를
Athena-OS로 처음부터 끝까지 학습하는 흐름입니다.

원본 레포: https://github.com/anthropics/courses

## 준비

```bash
git clone https://github.com/anthropics/courses.git
cd courses/prompt_engineering_interactive_tutorial
```

클론하면 아래 구조의 `.ipynb` 파일들이 생깁니다.

```
prompt_engineering_interactive_tutorial/Anthropic 1P/
├── 00_Tutorial_How-To.ipynb
├── 01_Basic_Prompt_Structure.ipynb
├── 02_Being_Clear_and_Direct.ipynb
├── 03_Assigning_Roles_Role_Prompting.ipynb
├── 04_Separating_Data_and_Instructions.ipynb
├── 05_Formatting_Output_and_Speaking_for_Claude.ipynb
├── 06_Precognition_Thinking_Step_by_Step.ipynb
├── 07_Using_Examples_Few-Shot_Prompting.ipynb
├── 08_Avoiding_Hallucinations.ipynb
├── 09_Complex_Prompts_for_Real_World_Use_Cases_and_Conclusion.ipynb
├── 10_Appendix_Tool_Use.ipynb
├── 11_Appendix_Chaining_Prompts.ipynb
└── 12_Appendix_Search_and_Retrieval.ipynb
```

## 목표

- 프롬프트 엔지니어링을 처음 접하는 한국어 사용자 기준으로 처음부터 학습
- 9개 챕터를 하나의 체계적인 커리큘럼으로 재구성
- 각 단계마다 확인 질문과 회상 과제 포함

## 추천 실행

### 1. 전체 코스 프롬프트 생성 (mastery-ko)

```bash
python3 scripts/promptforge.py build mastery-ko \
  --goal "프롬프트 엔지니어링 핵심 개념을 처음부터 완전히 이해하기" \
  --level "완전 초보" \
  --session-length "90분" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/01_Basic_Prompt_Structure.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/02_Being_Clear_and_Direct.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/03_Assigning_Roles_Role_Prompting.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/04_Separating_Data_and_Instructions.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/05_Formatting_Output_and_Speaking_for_Claude.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/06_Precognition_Thinking_Step_by_Step.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/07_Using_Examples_Few-Shot_Prompting.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/08_Avoiding_Hallucinations.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/09_Complex_Prompts_for_Real_World_Use_Cases_and_Conclusion.ipynb" \
  --embed \
  --output dist/anthropic-mastery-ko.md
```

> `--embed` 플래그를 붙이면 `.ipynb` 파일 내부의 마크다운 셀과
> 코드 셀이 프롬프트에 직접 포함됩니다.
> 그대로 LLM에 붙여넣으면 바로 수업이 시작됩니다.

### 2. 섹션별 레슨 (lesson-ko)

챕터 하나씩 깊게 파고 싶을 때:

```bash
python3 scripts/promptforge.py build lesson-ko \
  --goal "Few-Shot Prompting 개념 완전히 이해하기" \
  --level "기초 개념은 아는 상태" \
  --session-length "30분" \
  --source "courses/prompt_engineering_interactive_tutorial/07_using_examples.ipynb" \
  --embed \
  --output dist/lesson-few-shot.md
```

### 3. 퀴즈 & 회상 (quiz-ko)

수업 직후 기억 고정:

```bash
python3 scripts/promptforge.py build quiz-ko \
  --goal "챕터 1~4 핵심 개념 회상 훈련" \
  --level "완전 초보" \
  --session-length "20분" \
  --source "courses/prompt_engineering_interactive_tutorial/01_basic_prompt_structure.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/02_being_clear_and_direct.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/03_assigning_roles.ipynb" \
  --source "courses/prompt_engineering_interactive_tutorial/Anthropic 1P/04_Separating_Data_and_Instructions.ipynb" \
  --embed \
  --output dist/quiz-ch1-4.md
```

## 산출물 기대치

- 전체 9챕터 학습 로드맵
- 챕터별 핵심 개념 정의 + 확인 질문
- 챕터 간 연결 지도 ("이 개념이 저 챕터에서 왜 중요한가")
- 누적 퀴즈 (챕터 3개 단위)
- 최종 백지복원: 프롬프트 엔지니어링 9원칙을 노트 없이 설명
