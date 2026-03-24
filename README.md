# Athena-OS

GitHub에서 찾은 `AI tutor`, `study guide`, `prompt engineering`, `humanize`, `style guide` 자료를 한 레포로 재구성한 한국어 중심 학습/문체 조합 킷입니다.

이 레포의 목적은 두 가지입니다.

1. 아무것도 보지 않은 학습자도 문서를 `처음부터 끝까지 배우게` 만들기
2. 기계적인 설명을 `사람이 쓴 듯 자연스럽고 이해 쉬운 문체`로 바꾸기

원본 저장소를 통째로 벤더링하지는 않았습니다. 대신 라이선스와 실사용성을 고려해 핵심 아이디어를 추출해 다음 네 가지 형태로 재조합했습니다.

- 한국어 프롬프트 팩
- 실전 워크플로 레시피
- 출처 registry와 체리피킹 근거
- 프롬프트를 조립해주는 로컬 CLI

## What Is Inside

```text
Athena-OS/
├── prompts/
│   ├── core/
│   └── tasks/
├── packs/
├── recipes/
├── examples/
├── scripts/
├── sources/
└── dist/
```

## Included Packs

- `mastery-ko`
  문서를 처음 보는 한국어 사용자에게 전체 커리큘럼과 학습 루프를 만들어 줍니다.
- `lesson-ko`
  자료를 작은 덩어리로 가르치고 바로 확인 질문까지 붙입니다.
- `quiz-ko`
  이해 점검, active recall, 오답 교정용입니다.
- `humanize-ko`
  어색한 AI 문체를 자연스럽고 설명력 있는 한국어 문체로 바꿉니다.

## Quick Start

### 1. 사용 가능한 팩 보기

```bash
python3 scripts/promptforge.py list
```

### 2. 마스터 학습 프롬프트 생성

`.md`와 `.ipynb` 파일 모두 `--source`로 넣을 수 있습니다.
`--embed`를 붙이면 파일 내용이 프롬프트에 직접 포함됩니다.

```bash
python3 scripts/promptforge.py build mastery-ko \
  --goal "이 문서들을 처음부터 끝까지 완전히 이해하고 기억하기" \
  --level "완전 초보" \
  --session-length "60분" \
  --source "/path/to/doc1.md" \
  --source "/path/to/notebook.ipynb" \
  --embed \
  --output dist/mastery-ko.md
```

### 3. Humanize 프롬프트 생성

```bash
python3 scripts/promptforge.py build humanize-ko \
  --goal "딱딱한 설명문을 자연스러운 한국어 학습 설명으로 바꾸기" \
  --level "일반 독자" \
  --session-length "N/A" \
  --output dist/humanize-ko.md
```

## Recommended Workflow

1. `mastery-ko`로 전체 지도와 학습 계획을 만듭니다.
2. `lesson-ko`로 섹션별 설명을 받습니다.
3. `quiz-ko`로 기억을 강제합니다.
4. `humanize-ko`로 결과 문체를 다듬습니다.

## Design Principles

- 한국어 우선
- 초보자 기준 설명
- 문서를 이미 읽었다고 가정하지 않음
- 설명 후 확인 질문
- 요약보다 학습 설계 우선
- detector 회피보다 가독성과 자연스러움 우선

## Why This Repo Exists

대부분의 AI 요약은 이미 내용을 아는 사람 기준으로 압축합니다. 이 레포는 반대로 설계했습니다.

- 처음 보는 사람도 따라올 수 있어야 합니다.
- 용어는 설명 없이 던지지 않습니다.
- 문서는 `요약`이 아니라 `수업`으로 변환되어야 합니다.
- 톤 보정은 `AI 냄새 제거`가 아니라 `사람이 읽기 쉬운 설명`이 목표입니다.

## Key Source Families

- 튜터링: Mr. Ranedeer, ai-tutor, Tutor-GPT, OATutor, SocraticMath
- 교육 프롬프트: Microsoft prompts-for-edu
- 프롬프트 엔지니어링: Prompt Engineering Guide, Learn Prompting, Promptify
- 스타일/톤: GitHub Docs Style Guide
- 문체 humanize: humanicer, text-rewriter, AI text humanizer 계열

자세한 목록은 [sources/REGISTRY.md](/Users/gongysd/Desktop/달피디/Athena-OS/sources/REGISTRY.md)와 [sources/CHERRY_PICKS.md](/Users/gongysd/Desktop/달피디/Athena-OS/sources/CHERRY_PICKS.md)에 정리했습니다.

## Suggested Starting Files

- [prompts/core/01_master_tutor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/01_master_tutor_ko.md)
- [prompts/core/03_humanize_editor_ko.md](/Users/gongysd/Desktop/달피디/Athena-OS/prompts/core/03_humanize_editor_ko.md)
- [recipes/01_zero_to_mastery.md](/Users/gongysd/Desktop/달피디/Athena-OS/recipes/01_zero_to_mastery.md)
- [examples/anthropic_prompt_engineering.md](/Users/gongysd/Desktop/달피디/Athena-OS/examples/anthropic_prompt_engineering.md)

## License

이 레포의 큐레이션과 새로 작성된 문서는 MIT 라이선스로 배포합니다. 원본 저장소의 라이선스와 권리는 각 저장소에 남아 있습니다. 원본 코드를 통째로 복제하지 않았으며, 아이디어와 사용 패턴을 요약해 재구성했습니다.
