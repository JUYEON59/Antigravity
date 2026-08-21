# 워크플로 상태

상태 값: `not_started` · `draft` · `approved` · `revision_requested` · `stale`

| 단계 | 상태 | 현재 결과물 | 최종 변경 | 승인 근거 또는 메모 |
|---|---|---|---|---|
| 리서치 | not_started | `01_research/research-report.md` | - | - |
| 트렌드 분석 | not_started | `02_trend-analysis/trend-analysis.md` | - | 리서치 승인 필요 |
| 제안서 | not_started | `03_proposal/proposal.md` | - | 트렌드 분석 승인 필요 |
| 프레젠테이션 구성안 | not_started | `04_presentation/presentation-outline.md` | - | 제안서 승인 필요 |
| 실제 PPT | not_started | `04_presentation/presentation.pptx` | - | 구성안 승인 필요 |
| 통합 심의 | not_started | `05_council/council-decision.md` | - | 실제 PPT 최종 승인 필요 |

## 상태 기록 규칙

- 사용자가 명시적으로 승인한 경우에만 `approved`로 변경합니다.
- 승인된 상위 결과물이 바뀌면 하위 결과물을 삭제하지 않고 `stale`로 표시합니다.
- `최종 변경`에는 `YYYY-MM-DD HH:mm` 형식을 사용합니다.
- `승인 근거 또는 메모`에는 사용자의 승인 표현이나 수정 요청을 짧게 기록합니다.
