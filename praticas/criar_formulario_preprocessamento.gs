/**
 * Cria um Google Forms e uma planilha de respostas para a prática
 * de pré-processamento de dados laboratoriais.
 *
 * Os dados são fictícios. Não solicitar dados de pacientes.
 */
function criarFormularioPreProcessamento() {
  const titulo = 'Oficina de Pré-processamento de Dados - Biomedicina e Farmácia';

  const formulario = FormApp.create(titulo)
    .setDescription(
      'Atividade didática com amostras laboratoriais fictícias.\n\n' +
      'Não informe nome de paciente, CPF, diagnóstico, prontuário ou qualquer dado real.\n\n' +
      'Digite as informações conforme aparecem no roteiro da atividade. ' +
      'Algumas diferenças de escrita serão analisadas posteriormente no Google Colab.'
    )
    .setConfirmationMessage(
      'Resposta registrada! Na próxima etapa, sua turma irá analisar a qualidade dos dados no Google Colab.'
    )
    .setProgressBar(true)
    .setCollectEmail(false)
    .setLimitOneResponsePerUser(false)
    .setAcceptingResponses(true);

  formulario.addSectionHeaderItem()
    .setTitle('Parte 1 - Identificação didática')
    .setHelpText('Use apenas uma identificação da atividade. Não informe dados pessoais de pacientes.');

  formulario.addTextItem()
    .setTitle('Nome do grupo ou código da equipe')
    .setHelpText('Exemplo: Grupo 1, Equipe Azul ou BIO-01.')
    .setRequired(true);

  formulario.addTextItem()
    .setTitle('Código da amostra')
    .setHelpText('Use um código fictício, por exemplo: A01, A02 ou A03. Alguns códigos poderão ser repetidos para simular duplicidade.')
    .setRequired(true);

  formulario.addSectionHeaderItem()
    .setTitle('Parte 2 - Características da amostra')
    .setHelpText('Digite as informações como se estivesse preenchendo uma ficha de laboratório.');

  formulario.addTextItem()
    .setTitle('Qual é o material da amostra?')
    .setHelpText('Digite apenas o material. Exemplos: sangue, urina, plasma ou saliva. Para a simulação, diferenças como Sangue, SANGUE ou sangue serão analisadas.')
    .setRequired(true);

  formulario.addTextItem()
    .setTitle('Qual é a concentração da amostra?')
    .setHelpText('Digite um valor fictício. Você pode usar, por exemplo, 2.5, 2,5 ou 2,5 mg/mL. Não deixe o campo vazio sem orientação da professora.')
    .setRequired(false);

  formulario.addTextItem()
    .setTitle('Qual é o pH observado?')
    .setHelpText('Digite um valor numérico fictício, como 6,8 ou 7.2. Não use dados de exames reais.')
    .setRequired(false);

  formulario.addTextItem()
    .setTitle('Qual é a temperatura da amostra?')
    .setHelpText('Digite um valor fictício em graus Celsius, como 36,8 ou 37.1.')
    .setRequired(false);

  formulario.addTextItem()
    .setTitle('Qual é a cidade de origem da amostra didática?')
    .setHelpText('Use uma cidade fictícia ou uma das opções do roteiro. Exemplos: Nova Iguaçu, Rio de Janeiro ou Niterói.')
    .setRequired(true);

  formulario.addTextItem()
    .setTitle('Qual foi o resultado didático da análise?')
    .setHelpText('Digite: adequado, inadequado ou não informado. A padronização será feita posteriormente no Python.')
    .setRequired(false);

  formulario.addParagraphTextItem()
    .setTitle('Que problema de qualidade você imagina que pode aparecer nessa base?')
    .setHelpText('Resposta opcional. Pense em ausência, duplicidade, grafia diferente, unidade ou valor fora do esperado.');

  const planilha = SpreadsheetApp.create(
    'Respostas - Pré-processamento Biomedicina e Farmácia'
  );

  formulario.setDestination(
    FormApp.DestinationType.SPREADSHEET,
    planilha.getId()
  );

  const abaOrientacoes = planilha.insertSheet('ORIENTAÇÕES');
  abaOrientacoes.getRange('A1:B8').setValues([
    ['PRÁTICA', 'Pré-processamento de dados laboratoriais'],
    ['PÚBLICO', 'Biomedicina e Farmácia'],
    ['OBJETIVO', 'Gerar uma base fictícia para limpeza, validação, transformação e visualização'],
    ['ATENÇÃO', 'Não utilizar dados reais de pacientes'],
    ['ETAPA 1', 'Coletar as respostas neste formulário'],
    ['ETAPA 2', 'Abrir a aba de respostas e exportar como CSV'],
    ['ETAPA 3', 'Executar o notebook do Google Colab'],
    ['ETAPA 4', 'Interpretar os problemas encontrados'],
  ]);
  abaOrientacoes.getRange('A1:B1').setFontWeight('bold');
  abaOrientacoes.autoResizeColumns(1, 2);

  Logger.log('FORMULARIO_PUBLICO: ' + formulario.getPublishedUrl());
  Logger.log('FORMULARIO_EDICAO: ' + formulario.getEditUrl());
  Logger.log('PLANILHA_RESPOSTAS: ' + planilha.getUrl());
}

