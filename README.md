# gene_set_ora

Python 3.11 이상 표준 라이브러리만 사용하는 생물정보학 CLI입니다. AI 도움을 받아 작성했으며 예제는 합성 자료입니다.

## 실행

```console
python gene_set_ora.py examples/query.txt examples/universe.txt examples/sets.gmt
python -m unittest -v
```

결과는 표준 출력으로 내보냅니다. 파일로 저장하려면 `> results.txt`를 붙이세요. 잘못된 입력은 오류 메시지와 종료 코드 2로 반환합니다.

## 3. Gene-set ORA

query와 측정 가능한 배경(universe)은 줄당 유전자 하나이고, GMT는 `집합명 TAB 설명 TAB 유전자...` 형식입니다. query는 universe의 부분집합이어야 합니다. gene set은 universe와 교차한 뒤 hypergeometric 상측 꼬리확률 P(X≥k)를 구합니다. BH는 입력된 모든 집합에 대해 적용하며 겹침이 0인 집합도 포함합니다. gene ID 매핑, 발현량 기반 GSEA, 교란 보정은 하지 않습니다. 로그 조합 합산 방식이므로 극단적으로 작은 확률은 부동소수점 한계로 0이 될 수 있습니다.

[SciPy hypergeometric 정의](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html)

