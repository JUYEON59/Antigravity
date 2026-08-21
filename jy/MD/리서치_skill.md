---
name: hybrid-beauty-research
description: 스킨케어-메이크업 하이브리드 뷰티 브랜드 레퍼런스 수집 및 3단계 자동 분류 실행 스킬
---

# Hybrid Beauty Reference Research & Classification Skill

본 스킬은 CLI 에이전트(LLM, Web Search, Web Crawling 툴)가 **스킨케어-메이크업 하이브리드 뷰티 브랜드** 웹사이트 레퍼런스를 검색·추출·판별·분류하는 자동화 스킬 가이드입니다.

---

## 1. 실행 개요

- **프로젝트명**: TBD_Hybrid_Beauty
- **목적**: 하이브리드 뷰티 브랜드 웹사이트 기획 및 UI/UX 구조 설계를 위한 글로벌/국내 레퍼런스 자동 수집 및 분류
- **목표 수량**: 1차 Batch 20개 수집 -> 2차 Batch 누적 200개 확장
- **출력 포맷**: Plain Text (.txt)

---

## 2. Phase 1: 레퍼런스 탐색 및 데이터 추출 (Research)

### 2.1 검색 키워드 (Search Keywords)
에이전트는 아래 키워드 조합을 활용하여 웹 검색을 수행합니다.
- `"Hybrid Beauty" OR "Skin Tint" AND "Clean Beauty Ecommerce"`
- `"Minimal Skincare" AND "Effortless Beauty UI"`
- `"Skincare makeup hybrid" inurl:about`
- `"minimalist beauty web design" awwwards`

### 2.2 필수 수집 항목 (Data Extraction Schema)
각 사이트 탐색 시 아래 항목을 필수적으로 추출 및 분석합니다.

| 필드명 | 설명 | 추출/분석 기준 |
| :--- | :--- | :--- |
| `brand_name` | 브랜드명 | `<title>` 태그 또는 로고 텍스트 |
| `url` | 웹사이트 주소 | 공식 홈페이지 URL |
| `meta_description` | 브랜드 소개 | Meta Description 태그 내용 |
| `visual_mood` | 시각적 분위기 | 메인 컬러(Hex), 여백 활용도, 텍스처 중심 비주얼 여부 |
| `core_ui` | 핵심 UI/UX 요소 | Before/After 슬라이더, 1-Step/Multi-use 강조, 텍스처 초근접 컷 유무 |
| `copywriting_ratio` | 카피라이팅 비율 | 스킨케어 성분 강조 vs 메이크업 효과 강조 비율 |
| `core_insight` | 기획 적용 인사이트 | 웹사이트 기획에 도입할 핵심 포인트 (1~2줄) |

---

## 3. Phase 2: 카테고리 분류 및 폐기 조건 (Classification)

### 3.1 3대 분류 기준 (Classification Rules)

1. **Category 1: 디자인 무드 중심 (Effortless & Minimal Mood)**
   - **판별 조건**: 극도로 깔끔한 여백, 과도한 장식 배제, 절제된 타이포그래피 및 텍스처 중심 정갈한 비주얼.
   - **키워드**: 미니멀, 깔끔한 여백, 텍스처, 정갈함, 절제된 타이포그래피

2. **Category 2: 하이브리드 기능/UX 중심 (Hybrid UX & Interactive)**
   - **판별 조건**: 스킨케어 효과(성분/수분)와 메이크업 효과(발색/커버)를 동시에 전달하는 직관적 UI 확인.
   - **키워드**: Before/After, 텍스처 줌인, 투명한 사용 가이드, 1-Step

3. **Category 3: 최우수 롤모델 (Top Hybrid Model)**
   - **판별 조건**: Category 1(디자인 무드) + Category 2(기능/UX)를 동시에 충족하고, '간결함(Easy & Effortless)' 메시지와 빠른 결제 UI(Frictionless Checkout)가 결합된 사이트.

### 3.2 수집 제외 및 폐기 조건 (Drop Criteria)
다음 조건 중 하나라도 해당하면 즉각 제외합니다.
- [DROP] 수십 개의 카테고리와 복잡한 레이아웃이 나열된 대형 종합 뷰티 쇼핑몰 (예: 올리브영 스타일 UI)
- [DROP] 피부과/메디컬 느낌이 지나치게 강한 차갑고 투박한 클리닉/더마 코스메틱 사이트
- [DROP] 지나치게 화려한 그래픽이나 복잡한 팝업창으로 간결한 UX 방향성에 위배되는 사이트
- [DROP] 기존 수집 사이트와 중복되거나 접속이 불안정한 사이트

---

## 4. Phase 3: 출력 포맷 및 실행 루프 제어 (Output & Execution Rules)

### 4.1 결과물 출력 파일 양식 (Output Format)
추출 및 분류 결과는 아래 포맷으로 텍스트 파일(`hybrid_beauty_references_batch1.txt` / `hybrid_beauty_references_final.txt`)에 기록합니다.

```text
==================================================
[Brand 001] BRAND_NAME
- URL: https://example.com
- Category: Category 3 (Top Hybrid Model)
- Visual Mood: #F4F1EA / 여백 상 / 텍스처 제형 강조
- Core UI: Before/After 슬라이더 적용, 1-Step 멀티유즈 가이드
- Copywriting Ratio: Skincare 60% : Makeup 40%
- Core Insight: 텍스처 초근접 샷과 함께 성분/발색 효과를 탭으로 전환하여 보여주는 UI가 인상적임.
==================================================
```

### 4.2 실행 및 루프 제어 (Execution Cycle)

```mermaid
flowchart TD
    A[리서치 시작] --> B[Phase 1: 데이터 크롤링 및 수집]
    B --> C{Phase 2: 분류 및 Drop 조건 판별}
    C -- Drop 해당 -- Drop 및 새로 탐색
    C -- 통과 -- D[수집 데이터 누적]
    D --> E{누적 20개 도달?}
    E -- No -- B
    E -- Yes -- F[PAUSE: hybrid_beauty_references_batch1.txt 생성]
    F --> G[사용자 검토 대기 - Human in the Loop]
    G -- 사용자 승인 (y) -- H[Phase 1 & 2 루프 재개]
    G -- 사용자 중단 (n) -- K[작업 종료]
    H --> I{누적 200개 도달?}
    I -- No -- H
    I -- Yes -- J[STOP: hybrid_beauty_references_final.txt 생성]
    J --> K
```

1. **1차 실행 (Batch 1 - Initial QA)**
   - 수집 및 분류 누적 개수가 **20개**가 되면 작업을 일시 정지(PAUSE)합니다.
   - `hybrid_beauty_references_batch1.txt` 파일 생성.
2. **Human in the Loop (사용자 검토 대기)**
   - 아래 안내 메시지를 터미널에 출력하고 대기합니다.
   > *"20개의 1차 리서치 및 데이터 추출이 완료되었습니다. 텍스트 파일을 검토해 주세요. 분류와 추출된 인사이트가 적절하다면 나머지 전체(Total 200개) 리서치를 계속 진행할까요? (y/n)"*
3. **Full Scale 확장 (Batch 2)**
   - 사용자가 `y`를 입력하면 누적 **200개**에 도달할 때까지 연속 실행합니다.
   - 200개 도달 시 작업을 완료(STOP)하고 `hybrid_beauty_references_final.txt`를 저장합니다.
