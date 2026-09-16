# Guia para preparar o formulário da próxima semana

## 1. Criar o formulário

1. Abra o Google Apps Script.
2. Crie um projeto novo.
3. Cole o conteúdo do arquivo `criar_formulario_preprocessamento.gs`.
4. Salve o projeto.
5. Execute a função `criarFormularioPreProcessamento`.
6. Autorize o acesso solicitado pelo Google.
7. Abra o registro de execução para copiar os três links gerados:
   - formulário para participantes;
   - formulário para edição;
   - planilha de respostas.

## 2. Compartilhar com os participantes

Use o link identificado como `FORMULARIO_PUBLICO`. Antes de compartilhar:

- confirme que o formulário está aceitando respostas;
- deixe desativada a coleta de e-mails, caso a atividade não precise identificar estudantes;
- não solicite nomes de pacientes, CPF, prontuários, diagnósticos ou resultados reais;
- envie o link no grupo da turma ou no ambiente da disciplina.

## 3. Como será usado no Colab

Depois que a turma responder:

1. abra a planilha de respostas;
2. baixe a aba como CSV;
3. carregue o arquivo no notebook;
4. execute as etapas por grupo;
5. compare a base bruta com a base pré-processada.

## Mensagem sugerida para os participantes

Olá, pessoal!

Antes da nossa prática de Bioinformática, respondam ao formulário abaixo utilizando apenas dados fictícios de uma amostra laboratorial. Não preencham informações de pacientes ou exames reais.

Na aula, vamos analisar as respostas no Google Colab e aprender como identificar dados ausentes, duplicidades, grafias diferentes, valores suspeitos e outros problemas de qualidade.

Leiam cada orientação com atenção. A atividade será realizada em grupos de pelo menos quatro estudantes.

Até a nossa prática!

