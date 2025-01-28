// Функция для удаления студента
function deleteStudent(id) {
    const row = document.querySelector(`#studentsTable tr[data-id="${id}"]`);
    if (row) {
        row.remove();
    }
}

// Функция для поиска студентов
function searchStudent() {
    const searchQuery = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.querySelectorAll('#studentsTable tbody tr');
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        let match = false;
        cells.forEach(cell => {
            if (cell.textContent.toLowerCase().includes(searchQuery)) {
                match = true;
            }
        });
        if (match) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Функция для добавления студента
document.getElementById('addStudentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('studentName').value;
    const email = document.getElementById('studentEmail').value;
    const age = document.getElementById('studentAge').value;

    const table = document.getElementById('studentsTable').getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();

    newRow.innerHTML = `
        <td></td>
        <td>${name}</td>
        <td>${email}</td>
        <td>${age}</td>
        <td><button class="delete-button" onclick="deleteStudent()">Удалить</button></td>
    `;
});
