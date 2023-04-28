import { BOT_UI } from "./chatbot.js";



function getQuestions() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const QUESTIONS = JSON.parse(REQUEST.responseText);
    const NUM_OF_QUESTIONS = QUESTIONS.length;
    const ACTIONS = [];

    for (let i=0; i < NUM_OF_QUESTIONS; i++) {
      ACTIONS.push({
        'text': QUESTIONS[i],
        'value': undefined
      });
    }

    BOT_UI.action.button({
      delay: 3000, // previous responses had a delay of 1000 and 2000 ms
      action: ACTIONS
    }).then(function (response) {
      getAnswerToQuestion(response.text);
    });
  });

  REQUEST.open('POST', '/thermal-qna/questions');
  REQUEST.send();
};

function getAnswerToQuestion(question) {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    BOT_UI.message.add({
      delay: 1000,
      type: 'text',
      content: REQUEST.responseText
    });
  });

  REQUEST.open('POST', '/thermal-qna/answers');
  REQUEST.setRequestHeader('content-type', 'application/json');
  REQUEST.send(JSON.stringify(question));
};

function startThermalQnA() {
  getQuestions();
};



export {
  startThermalQnA
};