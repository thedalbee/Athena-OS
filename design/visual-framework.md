# 학습 문서 시각 디자인 프레임워크

> **참조 파일**: `dist/lesson-02-c2.html` (Cornell Notes), `dist/lesson-02-d2.html` (Tufte)

---

## 핵심 원칙

- 색상이 아닌 **타이포그래피 위계**로 정보 구조 표현
- 색상은 "진짜 중요한 곳"에만 — 규칙 없는 색상은 노이즈
- 한국어 학습 문서에 최적화된 간격과 자간

---

## 색상 시스템 (5색 제한)

| 변수 | 값 | 용도 |
|---|---|---|
| `--text` | `#1C1917` | 본문 텍스트 전체 |
| `--bg` | `#F5F0E8` | 페이지 배경 |
| `--surface` | `#FFFEFB` | 카드/블록 배경 |
| `--border` | `#D4CCC0` | 구분선, 테두리 |
| `--accent` | `#5B4FD6` | 강조 — 아래 규칙 참고 |

### 왜 5색인가

색이 많을수록 시각적 노이즈가 늘고 위계가 무너진다. 색채 이론의 핵심은 "대비 예산(contrast budget)": 모든 것을 강조하면 아무것도 강조되지 않는다.

- 1~2색: 구조만 전달 (텍스트 + 배경)
- 3~4색: 레이어와 경계 표현 (surface, border 추가)
- 5번째 색(accent): **예산**이다. 쓸 때마다 "이게 정말 clarity를 높이는가?" 물어볼 것

### Accent 사용 허용 목록 (exhaustive)

이 목록 이외의 사용은 모두 금지한다.

- 섹션 번호 / 섹션 레이블
- 키워드 underline (섹션당 최대 1~2개)
- TOC hover/active 상태
- 스크롤 진행 바 (progress bar)
- 퀴즈 토글 화살표 (`▶`)
- Cornell Notes cue column 텍스트
- Tufte sidenote 참조 번호

### Accent 사용 금지

- 일반 본문 텍스트
- 목록 불릿 (`•`, `-`)
- 테이블 헤더 배경
- 카드 배경 fill

---

## 레이아웃 프레임워크

### A. Cornell Notes 변형 (`lesson-02-c2`)

**Cornell Notes**는 키워드↔설명 쌍이 명확할 때, 능동적 회상(active recall)을 유도하는 구조다.

```css
.cornell-row {
  display: grid;
  grid-template-columns: 200px 1fr;
  gap: 0;
}
```

| 영역 | 역할 | 스타일 |
|---|---|---|
| 좌측 (cue column) | 키워드 / 질문 | accent 색상 텍스트, `--bg` 배경 |
| 우측 (notes column) | 전체 내용 | `--surface` 배경 |
| 하단 summary strip | 핵심 요약 | accent 레이블 "핵심 요약", neutral 배경 |

**언제 쓰는가**: 키워드와 설명이 1:1로 매핑되는 콘텐츠. 시험 전 복습, 개념 정리에 적합.

---

### B. Tufte 학술 문서 스타일 (`lesson-02-d2`)

**Tufte** 레이아웃은 정보 밀도가 높고 부가 설명이 많을 때 본문 흐름을 끊지 않기 위한 구조다.

```css
.tufte-layout {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 32px;
}
```

| 영역 | 역할 | 스타일 |
|---|---|---|
| 좌측 (main) | 본문 | 전체 너비 활용 |
| 우측 (sidenotes) | 보조 설명 | `font-size: 20px`, `border-left` neutral |

**섹션 레이블**: 섹션 제목 위에 ALL-CAPS 카테고리 레이블 배치 (accent 색상, 소형 텍스트)

```html
<span class="category-label">SECTION 01</span>
<h2>섹션 제목</h2>
```

**반응형 처리**: 모바일에서는 sidenote가 본문 위로 올라오며 `border-left` 인디케이터로 보조 콘텐츠임을 표시

```css
@media (max-width: 768px) {
  .tufte-layout {
    grid-template-columns: 1fr;
  }
  .sidenote {
    order: -1;
    border-left: 3px solid var(--border);
    padding-left: 12px;
  }
}
```

**언제 쓰는가**: 학술 교재 느낌, 정보 밀도가 높고 부가 컨텍스트가 본문만큼 많을 때.

---

## 타이포그래피 설정

```css
body {
  font-family: 'SUIT', 'Apple SD Gothic Neo', sans-serif;
  font-size: 24px;        /* 최소 — 절대 작게 하지 말 것 */
  letter-spacing: -0.04em;
  line-height: 1.7;
  word-break: keep-all;
  color: var(--text);
}
```

**CDN 로드**:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/suit@v1/packages/suit/dist/suit.min.css">
```

### 왜 SUIT인가

한국어 웹폰트 중 가변 weight(`font-weight: 100–900`)를 지원하며, 자간 `-0.04em`에서 가독성이 가장 높다. 타이포그래피 위계를 `font-weight`만으로 구성할 수 있어 색상 의존도를 낮춘다.

### 왜 24px 최소인가

학습 문서는 독자가 내용을 이해하는 데 인지 자원을 써야 한다. 작은 글씨는 읽기 자체에 인지 부하를 추가한다. 16~18px은 UI용이며, 학습 콘텐츠에는 적합하지 않다.

---

## 콘텐츠 블록 유형

### Section Header

```css
h2 {
  font-weight: 700;
  border-bottom: 2px solid var(--border);
  padding-bottom: 8px;
}
```

### Content Card

```css
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 12px 16px;
  min-width: 0; /* grid child overflow 방지 — 필수 */
}
```

### Critical Callout (섹션당 최대 1개)

```css
.callout-critical {
  border-left: 3px solid var(--accent);
  background: var(--surface);
  padding: 12px 16px;
}
```

### Neutral Callout

```css
.callout-neutral {
  border-left: 3px solid var(--border);
  background: var(--surface);
  padding: 12px 16px;
}
```

### Table

```css
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  border: 1px solid var(--border);
  padding: 8px 12px;
}
th {
  font-weight: 600;
  /* 배경 fill 없음 — 헤더도 --surface 또는 투명 */
}
```

### Quiz Toggle

```html
<details class="quiz-toggle">
  <summary>질문 텍스트</summary>
  <div class="quiz-answer">정답 내용</div>
</details>
```

```css
.quiz-toggle summary::before {
  content: '▶';
  color: var(--accent);
  margin-right: 8px;
  transition: transform 0.2s;
}
.quiz-toggle[open] summary::before {
  transform: rotate(90deg);
}
```

### Properties Block (페이지 상단)

페이지 최상단에 메타정보(난이도, 소요시간, 선수학습 등)를 가로 key-value 테이블로 표시.

```html
<table class="properties-block">
  <tr>
    <th>난이도</th>
    <td>중급</td>
    <th>소요시간</th>
    <td>40분</td>
  </tr>
</table>
```

---

## 적용 가이드

새 학습 문서를 만들기 전 이 체크리스트를 통과해야 한다.

- [ ] 색상이 5개 이하인가?
- [ ] accent는 페이지 전체에 10회 미만으로 쓰였는가?
- [ ] 모든 구분이 색 없이도 이해되는가? (색맹 테스트)
- [ ] 폰트 최소 24px 지켰는가?
- [ ] 회색 텍스트(`color: gray`, `opacity: 0.5` 등)가 없는가?
- [ ] 카드 overflow: 모든 그리드 자식에 `min-width: 0` 있는가?

---

*이 문서는 `lesson-02-c2.html`, `lesson-02-d2.html`에서 추출한 실제 구현 기준이다.*
