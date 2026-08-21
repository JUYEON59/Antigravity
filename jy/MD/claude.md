# 박주연 프로젝트 컨텍스트

이 폴더의 Skill들은 **리서치 → 분류 → 트렌드 분석 → 심층 분석** 순으로 이어지는 다단계 워크플로우의 일부입니다. 개별 Skill 실행 시 아래 공통 규칙을 기본 전제로 삼습니다.

---

## 🗂️ 워크플로우 단계 및 폴더 구조

| 단계 | 결과 파일 | 담당 Skill |
|---|---|---|
| 01. 리서치 수집 | `output/01_research/research-report.md`, `references_raw.txt` | (본 폴더 외부) |
| 02. 분류 | `output/02_classification/classification-report.md` | `classification_skill.md` |
| 03. 트렌드 분석 | `output/03_trend-analysis/trend-analysis.md` *(원본 skill 파일에 명시된 경로 기준 추정)* | (본 폴더 외부) |
| 04. 심층 분석 | `output/04_analysis/analysis-report.md` | `analysis_skill.md` |

- 전체 단계 상태(`approved` / `draft` / `stale`)는 `output/workflow-status.md`에서 추적한다.
- 각 단계는 `references/*.md`(판별·분석 기준 설정 파일), `templates/*.md`(출력 구조 템플릿)가 존재하면 최우선 적용한다.

## ✅ 공통 실행 원칙

1. **승인 게이트:** 모든 Skill은 시작 전 `${CLAUDE_PROJECT_DIR}/CLAUDE.md`와 `output/workflow-status.md`를 읽고, 이전 단계 상태가 `approved`인지, 대상 입력 파일이 실제로 존재하는지 확인한다. 조건 미충족 시 무엇이 필요한지 알리고 즉시 중단한다.
2. **저장/아카이브:** 기존 결과 파일이 있으면 덮어쓰기 전 해당 단계 폴더의 `archive/` 하위에 타임스탬프를 붙여 보존한다. 기존 파일을 삭제하지 않는다.
3. **상태 갱신:** 결과 저장 후 `output/workflow-status.md`에서 해당 단계를 `draft`로 변경하고, 그 결과에 의존하는 하위 단계들은 `stale`로 변경한다 (파일 삭제 금지).
4. **근거 기반 원칙:** 모든 판정·결론은 객관적 데이터 근거에 연결한다. 임의로 부풀리거나 창작하지 않는다. 불확실한 항목은 `추가 검토 필요` / `TBD` / `확인 필요` 등으로 명시한다.
5. **자기 승인 금지:** Skill은 결과를 스스로 "승인" 처리하지 않는다. 승인은 사용자의 몫이다.

## 🔗 관련 Skill

- `classification_skill.md` — 수집 데이터를 분류 기준(제외 조건 + 3개 카테고리)에 따라 판별·맵핑하고 리포트 작성 (`/classification`)
- `analysis_skill.md` — 승인된 자료를 사실/해석/가정으로 구조화해 심층 분석·검증하고 리포트 작성 (`/analysis`)
