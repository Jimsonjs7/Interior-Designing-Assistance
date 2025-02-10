const quizQuestions = [
    {
        question: "What is your favorite type of flooring?",
        options: ["Hardwood", "Marble or tiles", "Natural stone or concrete", "Soft carpet or rugs"],
    },
    {
        question: "What kind of lighting do you prefer?",
        options: ["Sleek and recessed lighting", "Chandeliers and elegant sconces", "Warm and dim lighting with natural materials", "String lights or eclectic lamps"],
    },
    // Add more questions here...
];

let currentQuestionIndex = 0;

function renderQuestion() {
    const quizContainer = document.getElementById('quiz');
    quizContainer.innerHTML = '';

    const currentQuestion = quizQuestions[currentQuestionIndex];
    const questionElement = document.createElement('div');
    questionElement.classList.add('question');
    questionElement.textContent = currentQuestion.question;

    const optionsList = document.createElement('ul');
    optionsList.classList.add('options');

    currentQuestion.options.forEach(option => {
        const optionItem = document.createElement('li');
        optionItem.textContent = option;

        optionItem.addEventListener('click', () => {
            document.querySelectorAll('.options li').forEach(li => li.classList.remove('selected'));
            optionItem.classList.add('selected');
        });

        optionsList.appendChild(optionItem);
    });

    quizContainer.appendChild(questionElement);
    quizContainer.appendChild(optionsList);
}

document.getElementById('next-button').addEventListener('click', () => {
    if (currentQuestionIndex < quizQuestions.length - 1) {
        currentQuestionIndex++;
        renderQuestion();
    } else {
        alert('Quiz completed! Thank you.');
    }
});

renderQuestion();
