const url = window.location.href+'data';
const questionEle = document.getElementById('question')
const answerBtns = document.getElementById('answer-buttons')

//getting questions from json response
async function getData(index) {
    const response = await fetch(url);
    const data = await response.json()
    const question = data.data[index].question
    const answers = data.data[index].answers

    //add quiz's questions
    answers.forEach(answer => {
        const btn = document.createElement('li')
        btn.innerText = answer.text
        btn.classList.add('list-group-item')

        if (answer.correct) {
            btn.dataset.correct = answer.correct
        }else btn.dataset.correct = false

        answerBtns.appendChild(btn)
        btn.addEventListener('click', checkAnswer)
    })

    //add question
    questionEle.innerHTML = `<div class="card-header" style="text-align: center;" id="question-text">${question} </div>`

}

function resetQuestions(){
    while(answerBtns.firstChild)
        answerBtns.removeChild(answerBtns.firstChild)
        questionEle.innerHTML=""
}

var score = 0
function checkAnswer(e){
    for(const btn of answerBtns.children)
        btn.removeEventListener('click', checkAnswer)

    if(e.target.dataset.correct == 'true'){
        e.target.classList.add("list-group-item-success")
        score += 1
    }
    else{
        e.target.classList.add("list-group-item-danger")

        for (const child of answerBtns.children)
            if(child.dataset.correct == 'true')
                child.classList.add("list-group-item-success")
        
    }
    setTimeout(()=> {
        resetQuestions()
        showQuestion()
    },2300)
}

var index = 0
function showQuestion(){
    if(index < 10){
        getData(index)
        index += 1
    }else{
        questionEle.innerHTML = `<div class="card-header" style="text-align: center;"> Your Score: ${score}/10 </div>`
        answerBtns.innerHTML = `<a class='list-group-item' 
                                style='text-align: center;'
                                href="${document.referrer}">Play Again</a>`
    }
}

showQuestion()