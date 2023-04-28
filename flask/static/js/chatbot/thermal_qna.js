import { BOT_UI } from "./chatbot.js";



function getQuestions() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const QUESTIONS = JSON.parse(REQUEST.responseText);
  });

  REQUEST.open('POST', '/thermal-qna/questions');
  REQUEST.send();
};

function startThermalQnA() {
  getQuestions();
};



export {
  startThermalQnA
};