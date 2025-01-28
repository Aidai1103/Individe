from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создаем приложение
app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель данных
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    IT = db.Column(db.Float, nullable=False)
    Korean = db.Column(db.Float, nullable=False)
    History = db.Column(db.Float, nullable=False, default=0.0)
    grade = db.Column(db.Float, nullable=False)

    # Функция для вычисления среднего балла
    def calculate_average_grade(self):
        grades = [self.IT, self.Korean, self.History]
        
        # Фильтруем None значения
        grades = [grade for grade in grades if grade is not None]
        
        if grades:  # Если есть хотя бы одно числовое значение
            return sum(grades) / len(grades)
        else:
            return 0

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Поиск студентов
@app.route('/search', methods=['GET'])
def search_student():
    query = request.args.get('query')
    students = Student.query.filter(
        (Student.name.ilike(f"%{query}%")) | (Student.email.ilike(f"%{query}%"))
    ).all()
    return render_template('index.html', students=students)

# Добавление студента
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        IT = request.form['IT']
        Korean = request.form['Korean']
        History = request.form['History']

        IT = float(IT) if IT else None
        Korean = float(Korean) if Korean else None
        History = float(History) if History else None
        
        # Создание нового студента
        new_student = Student(name=name, email=email, age=age, IT=IT, Korean=Korean, History=History)
        
        # Вычисление среднего балла
        new_student.grade = new_student.calculate_average_grade()
        
        # Сохранение студента в базе данных
        db.session.add(new_student)
        db.session.commit()

        return redirect('/')
    return render_template('add_student.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get(id)
    if not student:
        return "Студент не найден", 404  # Обработка ошибки, если студент не найден
    
    if request.method == 'POST':
        student.name = request.form['name']
        student.email = request.form['email']
        student.age = request.form['age']
        student.IT = request.form.get('IT', type=float)
        student.Korean = request.form.get('Korean', type=float)
        student.History = request.form.get('History', type=float)

        student.grade = student.calculate_average_grade()  # Обновление среднего балла

        db.session.commit()  # Сохраняем изменения в базе данных
        return redirect('/')  # Перенаправление на главную страницу после сохранения

    return render_template('edit_student.html', student=student)  # Отправка студента в шаблон


# Удаление студента
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

# Инициализация миграции
migrate = Migrate(app, db)

# app.py
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание базы данных
    app.run(debug=True)
