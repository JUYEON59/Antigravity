# [작업 파이프라인 2] 핀터레스트 레퍼런스 분석 및 Flow 프롬프트 생성 지침서 (`pin분석.md`)

본 문서는 `로고/output/` 폴더에 수집된 핀터레스트 레퍼런스 이미지를 정밀 분석하여 AI 이미지 생성 도구(Flow/Midjourney/SD/DALL-E)에 활용할 수 있는 프롬프트로 변환·문서화하기 위한 2단계 파이프라인 표준 지침서입니다.

---

## 1. 파이프라인 개요 및 목적

- **목적**: 수집된 흑백 레퍼런스 로고 이미지의 시각적·구조적 요소를 분해 분석하고, AI 이미지 생성엔진에서 고품질 결과를 재현할 수 있는 디테일한 프롬프트 합성
- **대상 파일 경로**: `로고/output/` 내 수집된 로고 이미지 (`similar_logo_1.jpg`, `similar_logo_2.jpg` 등)

---

## 2. 레퍼런스 이미지 정밀 분석 항목 (Analysis Framework)

1. **타이포그래피 서체 (Typography)**: Serif(thin/bold contrast) vs. Sans-serif(geometric/clean)
2. **모노그램 및 심볼 구조 (Composition)**: 글자 간 결합 방식(Interlocking, Monogram, Lettermark, Line Symbol)
3. **획 두께 및 명암 대비 (Line Weight & Contrast)**: 획의 선 두께, 대비감, 2D Flat 처리 여부
4. **여백 및 대칭성 (Negative Space & Alignment)**: 순수 흰색 여백의 비중, 밸런스
5. **브랜드 무드 (Brand Identity Mood)**: 하이브리드 뷰티 브랜드에 부합하는 미니멀리즘, 럭셔리, 클린 감성

---

## 3. Flow 영문 프롬프트 합성 스펙 (Flow Prompt Engineering)

### 3.1 작성 언어 원칙
- 모든 이미지 생성 프롬프트는 AI 생성 엔진 최적화를 위해 **100% 영문(English)**으로 작성합니다.

### 3.2 프롬프트 구문 작성 구조
```text
[Subject/Core Monogram] + [Typography & Style] + [Color & Background Specs] + [Quality & Aesthetic Modifiers] + [Negative Constraint Terms]
```

### 3.3 프롬프트 구성 키워드 가이드
- **Subject**: `Minimalist luxury monogram logo design combining letters 'N' and 'D'`
- **Typography & Style**: `elegant interlocking serif typography style, solid flat black line art`
- **Color & Background**: `pure white background (#FFFFFF)`
- **Aesthetic Modifiers**: `ultra-clean vector graphics, high contrast, balanced stroke weight, elegant curves, 2D flat design`
- **Negative Constraints**: `no gradients, no drop shadows, no 3D effects, no mockups`

---

## 4. 이미지 재실행 방지 제어 규칙 (Non-Re-Execution Control)

1. **단발성 처리 원칙**: 한번 분석되어 `output/flow.md`에 기록이 완료된 레퍼런스 이미지는 시스템이 자동으로 재생성하거나 재작성하지 않습니다.
2. **재실행 트리거 조건**: 사용자가 터미널 또는 명령어로 명시적인 **"재실행"** 또는 **"다시 실행해"**를 입력한 경우에만 기존 분석 결과를 갱신합니다.

---

## 5. `output/flow.md` 문서화 규격

- **저장 위치**: `로고/output/flow.md`
- **문서 포맷 조건**:
  - 각 레퍼런스 이미지 파일명을 **대제목(`# 파일명.jpg`)**으로 작성
  - 대제목 아래 1줄 공백 후 분석하여 작성된 영문 Flow 프롬프트를 기술

### 출력 예시
```markdown
# similar_logo_1.jpg

Minimalist luxury monogram logo design combining uppercase letters 'N' and 'D' in an elegant interlocking serif typography style, solid flat black line art on a pure white background (#FFFFFF), ultra-clean vector graphics, high contrast, balanced stroke weight, elegant curves, 2D flat design, no gradients, no drop shadows, no 3D effects, aesthetic beauty brand identity logo.
```
