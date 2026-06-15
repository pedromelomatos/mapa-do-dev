const resumeInput = document.querySelector('#resumeFile');
const fileFeedback = document.querySelector('#fileFeedback');
const analyzeButton = document.querySelector('#analyzeButton');

resumeInput?.addEventListener('change', () => {
  const file = resumeInput.files[0];

  if (!file) {
    fileFeedback.textContent = 'Nenhum arquivo selecionado.';
    return;
  }

  if (file.type !== 'application/pdf') {
    fileFeedback.textContent = 'Por favor, selecione um arquivo PDF.';
    resumeInput.value = '';
    return;
  }

  fileFeedback.textContent = `Arquivo selecionado: ${file.name}`;
});

analyzeButton?.addEventListener('click', () => {
  const file = resumeInput.files[0];

  if (!file) {
    fileFeedback.textContent = 'Selecione um currículo em PDF antes de continuar.';
    return;
  }

  analyzeButton.textContent = 'Analisando...';
  analyzeButton.disabled = true;

  setTimeout(() => {
    window.location.href = analyzeButton.dataset.dashboardUrl || '/dashboard';
  }, 900);
});
