let elAnswer = document.querySelector('.answer-user');
let elAnswerInner = document.querySelector('.answer-inner');

let elAnswerList = document.querySelector('.answer-list');
let elAnswerContent = document.querySelectorAll('.answer-content');
// console.log(elAnswerListelAnswerList);
// console.log(elAnswerContent);
// console.log(elAnswerContent);
// console.log(elAnswerList);

elAnswerList.addEventListener('click', (e) => {
    for (let i = 0; i < elAnswerContent.length; i++) {
        // console.log(e.target);
        // console.log(elAnswerContent.length);
        // console.log(elAnswerContent);
        if (e.target.contains('answer-content')) {
            console.log(65456);
            // elAnswerInner.classList.toggle('d-flex');
        }
    }
})


// elAnswerList.forEach(element => console.log(element));

// for (item of elAnswerList) {
//     console.log(elAnswerList);
// }

// elAnswerList.forEach(item => {
//     console.log(item);
// })

// elAnswerList.addEventListener('click', (e) => {
//     if(e.target.childNodes) {
//         if(e.target.textContent == 'Answer...') {
//             console.log(879798);
//             elAnswerInner.classList.toggle('d-flex');
//         }
//     }
// })



// console.log(elAnswerList );

// for (let i = 0; i < 5; i++) {
//     console.log(i);
// }

// elAnswer.addEventListener('click', (e) => {
//     console.log(e.target.parentNode.parentNode.parentNode);
//     if (e.target.parentNode.parentNode.parentNode == )
//     elAnswerInner.classList.toggle('d-flex');
// });


