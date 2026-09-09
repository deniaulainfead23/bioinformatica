# Gabarito comentado — Aula 05

1. A base possui 24 linhas e 10 colunas originais; confirme com `tabela.shape`.
2. Cada linha representa uma amostra didática.
3. `id_amostra` identifica e permite rastrear cada registro.
4. Os grupos são Controle, Tratamento_A e Tratamento_B.
5. `dia_coleta`, `qualidade_media`, `temperatura_c` e `resposta_percentual`.
6. A padronização reduz diferenças artificiais de maiúsculas, minúsculas e espaços.
7. O tamanho é o número de caracteres; quantidade GC é G + C; GC% é `(G+C)/tamanho*100`.
8. Há ausência em `qualidade_media` para C05 e em `resposta_percentual` para C07.
9. Use `tabela[tabela['grupo'] == 'Tratamento_A']`.
10. Use `tabela[tabela['resposta_percentual'] >= 40]`; valores ausentes não atendem à comparação.
11. Use `tabela.loc[tabela['tamanho'].idxmax()]`.
12. Use `tabela.groupby('laboratorio')['temperatura_c'].mean()`.
13. Use `groupby('grupo')` com contagem e médias.
14. Barras são adequadas para comparar categorias.
15. Linhas são adequadas para uma sequência temporal.
16. O histograma mostra a distribuição da qualidade.
17. A dispersão mostra relação entre variáveis, mas não prova causalidade.
18. Não. A resposta média é apenas um indicador da base sintética.
19. Preencher sem justificativa pode inventar informação e alterar as conclusões.
20. Não. GC% é um indicador descritivo; não é diagnóstico nem identificação definitiva.

A interpretação real exigiria contexto experimental, origem da amostra, método de coleta, qualidade do sequenciamento, referência biológica, controles e método estatístico. Os dados deste material são sintéticos e servem apenas para aprendizagem.