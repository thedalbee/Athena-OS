# Cherry Picks

이 문서는 어떤 소스를 왜 채택했고, 어디에 반영했는지 설명합니다.

## Tutor Layer

### Mr.-Ranedeer-AI-Tutor

채택:
- 학습자 상태와 선호도에 맞춘 튜터 역할 설계
- 개인화된 수업 운영 관점

반영:
- [prompts/core/01_master_tutor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/01_master_tutor_ko.md)

### ai-tutor

채택:
- 코스, 모듈, 평가까지 이어지는 구조

반영:
- [prompts/tasks/01_doc_to_course_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/tasks/01_doc_to_course_ko.md)
- [recipes/01_zero_to_mastery.md](/Users/gongysd/Desktop/달피디/Athena-OS/recipes/01_zero_to_mastery.md)

### prompts-for-edu

채택:
- 교육 맥락에 맞는 역할 지시
- 학습자 중심 프롬프트 감각

반영:
- 전체 한국어 교육형 톤 설계

### Tutor-GPT / OATutor

채택:
- 학습자 반응에 따라 다음 질문 난이도를 바꾸는 적응형 관점

반영:
- [prompts/core/02_socratic_tutor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/02_socratic_tutor_ko.md)

### SocraticMath

채택:
- 질문 -> 힌트 -> 교정 -> 요약 흐름

반영:
- [prompts/core/02_socratic_tutor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/02_socratic_tutor_ko.md)

## Document To Study Artifact Layer

### PageLM / NotebookLM-style repos

채택:
- 문서에서 코스, 퀴즈, 카드, 질답을 뽑는 발상

반영:
- [prompts/tasks/01_doc_to_course_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/tasks/01_doc_to_course_ko.md)
- [prompts/tasks/03_doc_to_quiz_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/tasks/03_doc_to_quiz_ko.md)

### QuizFlow / flashcard repos

채택:
- active recall 중심 반복 학습

반영:
- [prompts/tasks/04_recall_drill_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/tasks/04_recall_drill_ko.md)

## Prompt Engineering Layer

### Prompt Engineering Guide / Learn Prompting / Promptify

채택:
- 역할 분리
- 모듈식 프롬프트
- 실행 지시와 출력 형식 분리

반영:
- `packs/*.json`
- [scripts/promptforge.py](/Users/gongysd/Desktop/달피디/Athena-OS/scripts/promptforge.py)

### awesome-prompting / awesome-prompts / awesome-claude-prompts

채택:
- 프롬프트를 역할과 목적별로 분리하는 방식

반영:
- `core`와 `tasks` 분리

## Humanize Layer

### GitHub Docs Style Guide

채택:
- clear, simple, approachable, active voice, audience-aware

반영:
- [prompts/core/03_humanize_editor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/03_humanize_editor_ko.md)
- [recipes/03_humanize_technical_text.md](/Users/gongysd/Desktop/달피디/Athena-OS/recipes/03_humanize_technical_text.md)

### humanicer / text-rewriter / AI Text Humanizer 계열

채택:
- 군더더기 제거
- 더 자연스러운 리듬
- 반복 표현 줄이기

반영:
- [prompts/core/03_humanize_editor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/03_humanize_editor_ko.md)
- [prompts/tasks/05_humanize_rewrite_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/tasks/05_humanize_rewrite_ko.md)

## Intentional Exclusions

- detector bypass 문구
- "AI 탐지 우회" 같은 공격적 목표
- 과도하게 광고성인 문구
- 라이선스와 출처가 불분명한 대량 복제
