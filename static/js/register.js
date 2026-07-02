const registerForm = document.querySelector('#registerForm');
const resumeInput = document.querySelector('#resumeFile');
const fileFeedback = document.querySelector('#fileFeedback');

resumeInput?.addEventListener('change', () => {
  const file = resumeInput.files[0];

  if (!file) {
    fileFeedback.textContent = 'Somente PDF por enquanto';
    return;
  }

  if (file.type !== 'application/pdf') {
    fileFeedback.textContent = 'Selecione um arquivo PDF.';
    resumeInput.value = '';
    return;
  }

  fileFeedback.textContent = `Arquivo selecionado: ${file.name}`;
});

registerForm?.addEventListener('submit', (event) => {
  const file = resumeInput?.files[0];

  if (!file) {
    event.preventDefault();
    fileFeedback.textContent = 'Selecione seu currículo em PDF para criar a conta.';
  }
});
