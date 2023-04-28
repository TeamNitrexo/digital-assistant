import {
  BOT_UI,
  provideSuggestionsAgain
} from "./chatbot.js";



function getQuestions() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const QUESTIONS = JSON.parse(REQUEST.responseText);
    const NUM_OF_QUESTIONS = QUESTIONS.length;
    const ACTIONS = [{
      'text': 'Go back',
      'value': 'return'
    }];

    for (let i=0; i < NUM_OF_QUESTIONS; i++) {
      ACTIONS.push({
        'text': QUESTIONS[i],
        'value': 'question'
      });
    }

    BOT_UI.action.button({
      delay: 3000, // previous responses had a delay of 1000 and 2000 ms
      action: ACTIONS
    }).then(function (response) {
      if (response.value === 'question') {
        getAnswerToQuestion(response.text);
      }
      else if (response.value === 'return') {
        provideSuggestionsAgain();
      }
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

    BOT_UI.message.add({
      delay: 2000,
      type: 'text',
      content: 'What else do you want to know?'
    });

    getQuestions();
  });

  REQUEST.open('POST', '/thermal-qna/answers');
  REQUEST.setRequestHeader('content-type', 'application/json');
  REQUEST.send(JSON.stringify(question));
};



export {
  getQuestions
};