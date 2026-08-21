# 명령 빠른 참고표

## 구성 확인

| 명령 | 용도 |
|---|---|
| `/context` | 현재 컨텍스트에 로드된 지침, Skill, 도구 확인 |
| `/memory` | `CLAUDE.md`와 메모리 위치 확인·편집 |
| `/skills` | 사용 가능한 Skill과 출처 확인 |

## 단계별 실행

```text
/research input/topic.md를 기준으로 조사해줘
리서치 결과를 승인해. 상태표에 반영해줘.

/trend-analysis output/01_research/research-report.md를 분석해줘
트렌드 분석 결과를 승인해. 상태표에 반영해줘.

/proposal output/02_trend-analysis/trend-analysis.md를 바탕으로 제안서를 작성해줘
제안서를 승인해. 상태표에 반영해줘.

/presentation output/03_proposal/proposal.md를 15분 발표용으로 구성해줘
슬라이드 구성안을 승인해. 상태표에 반영하고 실제 PPT를 생성해줘.

실제 PPT를 열어 확인했어. 최종 승인으로 상태표에 기록해줘.

/workflow-council 전체 결과물의 근거 연결과 실행 가능성을 종합 심의해줘
통합 심의 결과를 승인해. 상태표에 반영해줘.
```

## 수정 요청 기본형

```text
[파일/절/슬라이드]의 [문제]를 [원하는 기준]에 맞게 수정해줘.
수정 전 파일을 archive에 보존하고, 변경된 부분부터 요약해줘.
영향받는 하위 단계는 stale로 표시해줘.
```

## 출처 검토 질문

```text
이 수치의 원문, 발행 기관, 기준 연도, 조사 범위를 보여줘.
1차 자료인지 2차 자료인지 구분해줘.
전체 시장으로 일반화할 수 없는 한계를 표시해줘.
```
