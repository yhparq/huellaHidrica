from django.shortcuts import render, redirect
from django.urls import reverse

questions = [
    # Preguntas del quiz
    {
        "question": "¿Cuál es la capital de Francia?",
        "options": ["París", "Londres", "Madrid", "Berlín"],
        "answer": "París"
    },
    {
        "question": "¿Cuál es el océano más grande?",
        "options": ["Atlántico", "Índico", "Ártico", "Pacífico"],
        "answer": "Pacífico"
    },
    {
        "question": "¿Quién escribió 'Cien años de soledad'?",
        "options": ["Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar", "Jorge Luis Borges"],
        "answer": "Gabriel García Márquez"
    }
]

def index(request):
    return render(request, 'quizapp/index.html')

def welcome(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            request.session['name'] = name
            request.session['question_index'] = 0  # Inicia en la primera pregunta
            request.session['score'] = 0  # Inicia el puntaje
            return redirect('quiz')  # Redirige a la vista 'quiz'
    return render(request, 'quizapp/welcome.html')

def quiz(request):
    question_index = request.session.get('question_index', 0)
    if question_index >= len(questions):
        return redirect('result')  # Redirige al resultado si no hay más preguntas

    question = questions[question_index]

    if request.method == 'POST':
        selected_option = request.POST.get('option')
        correct_answer = question['answer']
        if selected_option == correct_answer:
            request.session['score'] += 1

        # Avanza a la siguiente pregunta
        request.session['question_index'] += 1
        return redirect('quiz')  # Redirige a la vista 'quiz'

    return render(request, 'quizapp/quiz.html', {'question': question})

def result(request):
    score = request.session.get('score', 0)
    name = request.session.get('name')
    total = len(questions)
    return render(request, 'quizapp/result.html', {'score': score, 'total': total, 'name': name})
