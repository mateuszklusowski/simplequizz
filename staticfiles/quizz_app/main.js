const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const modalTitle = document.getElementById('staticBackdropLabel')
const startBtn = document.getElementById('start-button')
const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const title = modalBtn.getAttribute('data-category')
    const number = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const id = modalBtn.getAttribute('data-id')

    modalBody.innerHTML = `
    <ul class="text-muted">
        <li>Difficulty: <b>${difficulty}</b></li>
        <li>Number of questions: <b>${number}</b></li>
    </ul> 
    `    
    modalTitle.textContent = title

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + id
    })
}))