# 2차시 — 기능별 Skill 등록과 호출

## 학습 목표

- 프로젝트 Skill의 폴더 구조를 설명한다.
- `SKILL.md`의 YAML frontmatter와 본문 역할을 구분한다.
- 핵심 Skill 4개와 선택 심화 Skill 1개를 확인하고 직접 호출한다.
- `$ARGUMENTS`가 명령 뒤의 입력을 전달하는 방식을 이해한다.

## Skill 구조

```text
.claude/skills/
├─ research/SKILL.md
├─ trend-analysis/SKILL.md
├─ proposal/SKILL.md
├─ presentation/SKILL.md
└─ workflow-council/SKILL.md
```

프로젝트 Skill의 명령 이름은 폴더 이름에서 결정됩니다. 예를 들어 `trend-analysis` 폴더는 `/trend-analysis`로 호출합니다.

## `SKILL.md`의 두 부분

```md
---
name: research
description: 이 Skill이 하는 일과 사용하는 상황
argument-hint: "[주제 또는 파일 경로]"
disable-model-invocation: true
---

# 실행 절차

여기에 입력, 검증, 작성, 저장, 완료 조건을 작성합니다.
```

- frontmatter: 목록과 호출 동작에 필요한 메타데이터
- 본문: Skill이 실행될 때 Claude가 따를 절차
- `disable-model-invocation: true`: 수업에서 학생이 단계별로 직접 호출하게 함
- `$ARGUMENTS`: `/research` 뒤에 입력한 전체 문장

## 실습 1 — Skill 확인

1. Claude Code에서 `/skills`를 입력합니다.
2. 핵심 Skill 4개와 `workflow-council` Skill의 Project 출처를 확인합니다.
3. 목록에 없으면 폴더명, 대문자 `SKILL.md`, YAML 구분선 `---`를 확인합니다.

## 실습 2 — 역할표 만들기

각 `SKILL.md`를 읽고 다음 표를 완성합니다.

| Skill | 입력 | 출력 | 시작 조건 | 멈추는 시점 |
|---|---|---|---|---|
| research |  |  |  |  |
| trend-analysis |  |  |  |  |
| proposal |  |  |  |  |
| presentation |  |  |  |  |
| workflow-council |  |  |  |  |

## 실습 3 — 인수 전달 이해

두 명령의 차이를 설명합니다.

```text
/research
/research input/topic.md를 기준으로 2024년 이후 자료를 우선 조사해줘
```

첫 번째는 Skill의 기본 입력 경로를 사용하고, 두 번째는 사용자의 추가 조건을 `$ARGUMENTS`로 전달합니다.

## 실습 4 — Skill과 `CLAUDE.md` 분류

다음 문장을 어느 파일에 둘지 분류합니다.

1. 모든 결과는 한국어로 작성한다.
2. 핵심 수치는 가능하면 독립 근거로 교차 확인한다.
3. 제안서 승인 전 PPT를 만들지 않는다.
4. 트렌드는 변화 규모와 지속 가능성을 1~5점으로 평가한다.

정답: 1·3은 `CLAUDE.md`, 2는 research Skill, 4는 trend-analysis Skill입니다.

## 완료 기준

- [ ] `/skills`에 핵심 Skill 4개와 선택 심화 Skill 1개가 표시된다.
- [ ] 폴더명과 명령 이름의 관계를 설명할 수 있다.
- [ ] frontmatter와 본문의 역할을 구분한다.
- [ ] Skill이 자동 실행되지 않고 직접 호출된다.
- [ ] 각 Skill의 입력·출력·게이트를 설명할 수 있다.
