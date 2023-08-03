const questionTag = document.getElementById("question")

// Global object for current question
let questionObj;

// Function for populating question page
eel.expose(populate)
function populate(questionObject) {
    console.log(questionObject)
    questionTag.innerText = questionObject.question
    questionObj = questionObject
}

// Starts populating from python with question from python-part.
window.addEventListener("DOMContentLoaded", eel.startPopulating)

const answerForm = document.getElementById("answer-form")
const answerField = document.getElementById("answer-field")
const feedbackField = document.getElementById("feedback")
const mainWrapper = document.getElementById("main-wrapper")

const feedbackBox = document.getElementById("feedback-popup")
const correctnessHeading = document.getElementById("correctness-heading")
const acceptedAnswersList = document.getElementById("acceptable-answers-list")
const youAnswered = document.getElementById("you-answered")

// TODO: Separate this in a more appropriately named file
answerForm.addEventListener("submit", (event) => {

    // Common feedback page populating.
    event.preventDefault()
    feedbackBox.style.visibility = "visible"
    for (answer of questionObj.acceptedAnswers) {
        let li = document.createElement("li")
        li.textContent = answer
        acceptedAnswersList.appendChild(li)
    }
    youAnswered.innerText = answerField.value
    eel.log(questionObj, answerField.value)

    // TODO: Account for caseInsensitivity
    // Populating when correct answer
    if (questionObj.acceptedAnswers.includes(answerField.value)) {
        feedbackBox.style.backgroundColor = "#476b59"
        correctnessHeading.innerText = "Det var riktig!"
        window.addEventListener("keypress", window.close)
    } 

    // Populating when wrong answer
    else {
        feedbackBox.style.backgroundColor = "#7d3636"
        correctnessHeading.innerText = "Det var feil!"
        window.addEventListener("keypress", (event) => {
            location.reload()
        })
    }
})