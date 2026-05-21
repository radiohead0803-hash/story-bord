# Output Templates

## Normal selection report

```markdown
# 상호명·캐릭터 선정 결과

## 1. 결론
- 추천 조합:
- Evidence level:
- 공개판매 가능 여부:

## 2. 브랜드 전략
| 항목 | 내용 |

## 3. 상호명 후보 점수표
| 순위 | 상호명 | Lane | 점수 | 강점 | 리스크 | 판정 |

## 4. 캐릭터 후보 점수표
| 순위 | 캐릭터 | 실루엣/아이템 | 점수 | 상품화 방향 | 리스크 | 판정 |

## 5. 최종 조합 추천
| 추천 | 조합 | 첫 상품 | 확장 상품 | Proof status |

## 6. Claude Design 프롬프트
[copy-paste prompt]

## 7. 검증 게이트
| Gate | 확인사항 | 통과 기준 | 현재 상태 |

## 8. 다음 행동
- KIPRIS search:
- Platform search:
- Visual proof:
- Print proof:
- Operator approval:
```

## Proof gate wording

Use direct labels:
- `needs_research`: 판매 전 검증 필요
- `recommend`: 현재 후보 중 우선 검토
- `conditional_pass`: 디자인/샘플 제작 가능, 공개판매 전 추가 승인 필요
- `blocked`: 사용 금지 또는 변경 필요
