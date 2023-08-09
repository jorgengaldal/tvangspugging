const questionTag = document.getElementById("question")
const resourceWrapper = document.getElementById("resource-wrapper")

// Global object for current question
let questionObj;

function cleanResource() {
    resourceWrapper.innerHTML = ""
}

// Function for populating question page
eel.expose(populate)
function populate(questionObject) {
    console.log(questionObject)
    questionTag.innerText = questionObject.question
    questionObj = questionObject
    cleanResource()

    for (let resource of questionObj.resources) {
        if (resource.type == "image") {
            resourceWrapper.style.display = "flex"
            let image = document.createElement("img")
            image.src = resource.path
            image.style.maxHeight = "100%"
            image.style.maxWidth = "100%"
            resourceWrapper.appendChild(image)
        }
    }
}

// Starts populating from python with question from python-part.
window.addEventListener("DOMContentLoaded", eel.startPopulating)

