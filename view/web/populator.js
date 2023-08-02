const questionTag = document.getElementById("question")


let questionObj;
let acceptedAnswers = []

eel.expose(populate)
function populate(questionObject) {
    console.log(questionObject)
    questionTag.innerText = questionObject.question
    acceptedAnswers = questionObject.acceptedAnswers
    questionObj = questionObject
}

window.addEventListener("DOMContentLoaded", eel.startPopulating)

const answerForm = document.getElementById("answer-form")
const answerField = document.getElementById("answer-field")
const feedbackField = document.getElementById("feedback")
const mainWrapper = document.getElementById("main-wrapper")

const feedbackBox = document.getElementById("feedback-popup")
const correctnessHeading = document.getElementById("correctness-heading")
const acceptedAnswersList = document.getElementById("acceptable-answers-list")
const youAnswered = document.getElementById("you-answered")

answerForm.addEventListener("submit", (event) => {
    event.preventDefault()
    feedbackBox.style.visibility = "visible"
    for (answer of questionObj.acceptedAnswers) {
        let li = document.createElement("li")
        li.textContent = answer
        acceptedAnswersList.appendChild(li)
    }
    youAnswered.innerText = answerField.value
    if (questionObj.acceptedAnswers.includes(answerField.value)) {
        feedbackBox.style.backgroundColor = "#476b59"
        correctnessHeading.innerText = "Det var riktig!"
        window.addEventListener("keypress", window.close)
    } 
    else {
        feedbackBox.style.backgroundColor = "#7d3636"
        correctnessHeading.innerText = "Det var feil!"
        window.addEventListener("keypress", (event) => {
            location.reload()
        })
    }
})