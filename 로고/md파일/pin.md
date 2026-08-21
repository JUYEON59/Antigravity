# [작업 파이프라인 1] 핀터레스트 레퍼런스 자동 수집 지침서 (`pin.md`)

본 문서는 스킨케어와 메이크업의 경계를 허무는 '하이브리드 뷰티 브랜드'의 로고 레퍼런스를 핀터레스트(Pinterest)에서 자동 탐색, 검증 및 수집하기 위한 1단계 파이프라인 표준 지침서입니다.

---

## 1. 실행 트리거 및 파이프라인 전제조건

- **실행 명령**: `"래퍼런스 수집 시작해"`
- **입력 참조 데이터**: `로고/input/` 폴더 내 초안 이미지 (예: `로고 초안.jpeg`)
- **스타일 무드 기준**: `로고/래퍼런스/` 폴더 내 벤치마크 샘플 (Pure White 배경 + Flat 2D Black Vector)

---

## 2. 브랜드 컨셉 & 로고 핵심 규격

- **브랜드 컨셉**: 스킨케어와 메이크업의 경계를 허물어, 쉽고 간결한(Easy & Effortless) 뷰티 경험을 제안하는 브랜드
- **배경색**: 순수 흰색 (`#FFFFFF` Pure White)
- **로고색**: 단색 검정색 (`#000000` Solid Black)
- **표현 방식**: 2D 미니멀 타이포그래피, 모노그램(Monogram), 절제된 레터마크 및 라인 심볼

---

## 3. 핀터레스트 최적화 검색 키워드 체계

### 3.1 영문 메인 검색어 (Primary English Keywords)
1. `minimalist beauty logo design`
2. `clean skincare makeup hybrid logo`
3. `black and white serif logo design`
4. `minimal beauty monogram logo`
5. `aesthetic skincare typography logo`

### 3.2 영문 보조 조합 키워드 (Secondary Keywords)
- `effortless beauty logo flat`
- `minimalist cosmetic brand identity logo`
- `clean beauty lettermark logo`
- `simple ND logo design`

### 3.3 한글 보조 키워드
- `미니멀 뷰티 로고 디자인`
- `스킨케어 브랜드 로고 흑백`

---

## 4. 수집 필터링 규칙 (Inclusion vs. Exclusion)

### 4.1 필수 채택 기준 (Inclusion)
1. **단색 흑백**: 흰색 배경에 검정색 획으로만 구성된 디자인
2. **2D 평면 벡터**: 쉐이딩이나 질감이 없는 2D 평면 이미지 (`로고/래퍼런스/` 무드 기준)
3. **간결한 구조**: 글자 중심 또는 모노그램/라인 심볼 형태
4. **선명한 대비**: 가독성이 명확한 세리프 또는 산세리프 구조

### 4.2 엄격 금지 및 수집 제외 기준 (Exclusion)
1. **컬러 적용**: 검정색 외의 색상 또는 그라디언트 포함 로고
2. **목업(Mockup) 적용**: 용기, 상자, 튜브 패키지, 종이 압인, 명함, 3D 질감 목업
3. **배경 질감 및 어두운 배경**: 종이, 돌, 패브릭 질감 배경, 검은색/어두운 배경
4. **복잡한 일러스트**: 화려한 꽃, 나뭇잎, 3D 장식 요소
5. **대형 종합 쇼핑몰 스타일**: 세련되지 않은 아이콘 및 조잡한 폰트 조합

---

## 5. Playwright 자동화 수집 & 저장 스펙

1. **로딩 옵션**: `wait_until="domcontentloaded"` 설정 후 `img[src*="i.pinimg.com"]` 로딩 확인
2. **고해상도 전환**: 썸네일 URL 중 `/236x/` 또는 `/474x/`를 `/736x/` 또는 `/originals/`로 변경하여 다운로드
3. **저장 위치**: `로고/output/`
4. **저장 파일명**: `similar_logo_{index}.jpg` (JPEG 단색 포맷)
