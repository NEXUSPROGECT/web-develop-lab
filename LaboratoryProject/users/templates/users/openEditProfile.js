const toggleButton = document.getElementById('toggleFormButton');
    const editForm = document.getElementById('editForm');

    toggleButton.addEventListener('click', () => {
      if (editForm.classList.contains('hidden')) {
        editForm.classList.remove('hidden');
        // Используем setTimeout для плавного перехода после удаления 'hidden'
        setTimeout(() => {
          editForm.classList.remove('opacity-0', 'scale-95');
          editForm.classList.add('opacity-100', 'scale-100');
        }, 10);
      } else {
        editForm.classList.add('opacity-0', 'scale-95');
        editForm.classList.remove('opacity-100', 'scale-100');
        // Добавляем 'hidden' после завершения анимации
        setTimeout(() => {
          editForm.classList.add('hidden');
        }, 500); // Должно совпадать с duration-500
      }
    });