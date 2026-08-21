# [TBD Hybrid Beauty] 핀터레스트 로고 레퍼런스 수집 및 분석 가이드

본 문서는 스킨케어와 메이크업의 경계를 허무는 '하이브리드 뷰티 브랜드'의 로고 레퍼런스를 핀터레스트(Pinterest)에서 안정적이고 정확하게 탐색·수집하기 위한 표준 지침서입니다.

---

## 1. 브랜드 및 로고 핵심 규격 (Logo Specifications)

- **브랜드 컨셉**: 스킨케어와 메이크업의 경계를 허물어, 쉽고 간결한(Easy & Effortless) 뷰티 경험을 제안하는 하이브리드 뷰티 브랜드
- **배경색**: 순수 흰색 (`#FFFFFF` Pure White)
- **로고색**: 단색 검정색 (`#000000` Solid Black)
- **표현 방식**: 2D 미니멀 타이포그래피, 모노그램(Monogram), 절제된 레터마크 및 라인 심볼

---

## 2. 핀터레스트 최적화 검색 키워드 (Search Keywords)

핀터레스트 알고리즘 특성상 영문 정밀 키워드 조합 시 고품질의 레퍼런스가 안정적으로 탐색됩니다.

### 2.1 메인 추천 검색어 (Primary Keywords)
1. `minimalist beauty logo design`
2. `clean skincare makeup hybrid logo`
3. `black and white serif logo design`
4. `minimal beauty monogram logo`
5. `aesthetic skincare typography logo`

### 2.2 스타일 보조 조합 키워드 (Secondary Keywords)
- `effortless beauty logo flat`
- `minimalist cosmetic brand identity logo`
- `clean beauty lettermark logo`
- `simple ND logo design` (모노그램 탐색 시)

### 2.3 한글 보조 키워드
- `미니멀 뷰티 로고 디자인`
- `스킨케어 브랜드 로고 흑백`

---

## 3. 로고 레퍼런스 채택 기준 (Inclusion Criteria)

아래 조건을 모두 만족하는 이미지 우선 채택:

1. **단색 흑백 (Monochrome)**: 흰색 배경에 검정색 획으로만 표현된 디자인
2. **평면 벡터 (Flat 2D)**: 입체감이나 입체 쉐이딩이 없는 정갈한 2D 평면 이미지 (`로고/래퍼런스/` 폴더 샘플 무드 기준)
3. **간결한 타이포그래피 & 심볼**: 스킨케어/메이크업 브랜드의 세련되고 간결한 이미지를 전달하는 글자 중심 또는 모노그램/라인 심볼 구조
4. **선명한 대비**: 가독성이 뛰어나고 명확한 세리프(Serif) 또는 산세리프(Sans-serif) 구조

---

## 4. 엄격 금지 및 수집 제외 조건 (Exclusion & Negative Rules)

핀터레스트 자동 스캔 및 수집 시 다음 조건에 해당하면 즉시 **제외(Drop)** 처리합니다.

1. **컬러 적용 로고 (Color & Gradient)**: 검정색 외의 컬러(핑크, 골드, 베이지 등) 또는 그라디언트가 들어간 로고
2. **목업(Mockup) 적용 로고**: 
   - 화장품 용기, 튜브, 상자 패키지 목업
   - 종이 압인, 명함, 명암 쉐이딩, 3D 질감 목업
3. **배경 질감 및 어두운 배경**: 텍스처(종이, 돌, 패브릭)가 있는 배경, 검은색/어두운 배경
4. **복잡한 일러스트/장식**: 과도하게 화려한 꽃, 나뭇잎 일러스트, 섬세한 3D 그래픽
5. **대형 종합 쇼핑몰 스타일**: 조잡한 폰트 조합이나 세련되지 않은 아이콘 형태

---

## 5. 자동화(Playwright) 수집 및 저장 실행 규칙

1. **페이지 로딩 방식**: `wait_until="domcontentloaded"` 설정 후 `img[src*="i.pinimg.com"]` 로딩 대기 (네트워크 아이들 타임아웃 방지)
2. **이미지 URL 고해상도 전환**:
   - 썸네일 URL 경로 중 `/236x/` 또는 `/474x/`를 `/736x/` 또는 `/originals/`로 변경하여 고화질 다운로드
3. **저장 포맷 및 경로**:
   - 저장 위치: `로고/output/`
   - 파일명 규격: `similar_logo_{index}.jpg` (JPEG 단색 이미지 저장)

---

## 6. 에이전트 자동 실행 명령 및 워크플로우 규칙 (Agent Execution Trigger & Rules)

사용자가 **"래퍼런스 수집 시작해"** 라고 명령할 때 에이전트가 자동 수행하는 작업 규칙(SOP)입니다.

### 6.1 실행 트리거 (Trigger Command)
- **명령어**: `"래퍼런스 수집 시작해"`

### 6.2 작업 실행 워크플로우 (Step-by-Step SOP)
1. **`로고/input/` 분석**: `로고/input/` 폴더 안의 이미지 파일(예: `로고 초안.jpeg`)을 분석하여 글자 형태, 획 스타일, 심볼 유무를 추출합니다.
2. **`로고/래퍼런스/` 무드 참조**: `로고/래퍼런스/` 폴더에 저장된 샘플 이미지(Pure White 배경 + Flat 2D Black Vector + 명확한 브랜드 타이포그래피)의 스타일 기준을 벤치마킹합니다.
3. **핀터레스트 탐색 및 필터링**: Playwright를 활용해 핀터레스트에서 유사 로고를 탐색하고, 본 가이드의 **채택 기준(3장)**과 **금지 조건(4장)**에 맞춰 정밀 스캔합니다.
4. **`로고/output/` 저장**: 조건에 부합하는 이미지를 캡처/다운로드하여 고해상도 `.jpg` 형태(`similar_logo_1.jpg`, `similar_logo_2.jpg` 등)로 `로고/output/` 폴더에 생성합니다.

---

## 7. Flow 이미지 생성 프롬프트 작성 및 재실행 방지 규칙 (Flow Prompt & Non-re-execution Rules)

1. **Output 레퍼런스 기반 Flow 프롬프트 변환**:
   - `로고/output/` 폴더에 수집된 이미지(예: `similar_logo_1.jpg`)의 시각적/구조적 특징을 정밀 분석하여 AI 이미지 생성 도구(Flow/Midjourney/SD 등)에서 활용할 수 있는 프롬프트로 작성합니다.
2. **영문 작성 원칙**:
   - AI 이미지 생성 엔진의 프롬프트 해석 정확도를 위해 모든 생성 프롬프트는 **영문(English)**으로 작성합니다.
3. **이미지 재실행 방지 (Non-re-execution Rule)**:
   - 한번 처리가 완료된 이미지는 명시적인 **"재실행"** 또는 **"다시 실행해"** 명령이 입력되기 전까지 기존 이미지를 다시 작성하거나 재생성하지 않습니다.
4. **`output/flow.md` 문서화 규격**:
   - 작성된 영문 프롬프트는 `로고/output/flow.md` 파일에 기록합니다.
   - 각 레퍼런스 이미지 파일명을 **대제목(`# 파일명.jpg`)**으로 작성하고, 그 아래쪽에 생성용 영문 프롬프트를 기술합니다.