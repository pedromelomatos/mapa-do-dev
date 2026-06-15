const checkboxes = document.querySelectorAll('.exercise-list input[type="checkbox"]');
const habitText = document.querySelector('.habit-card p');

function updateHabitText() {
  const completed = [...checkboxes].filter((checkbox) => checkbox.checked).length;
  habitText.textContent = `${completed} tarefas concluídas hoje. Continue mantendo constância.`;
}

checkboxes.forEach((checkbox) => {
  checkbox.addEventListener('change', updateHabitText);
});

updateHabitText();
