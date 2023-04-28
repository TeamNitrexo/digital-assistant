import "https://cdn.jsdelivr.net/npm/botui/build/botui.js";
import { getTutorial } from "./tutorials.js";



const BOT_UI = new BotUI('nitrexo-bot');

function init_chatbot() {
  BOT_UI.message.add({
    content: 'Hi, I am Nitrexo\'s Digital Assistant'
  }).then(function () {
    BOT_UI.message.add({
      delay: 1000,
      content: 'How can I help you?'
    });

    suggestedResponses(2000);
  });
};
init_chatbot();

function suggestedResponses(delay) {
  setTimeout(() => {
    BOT_UI.action.button({
      action: [
        {
          'text': 'What is Thermo-elastic Verification?',
          'value': 'tev'
        },
        {
          'text': 'Can you perform Temperature Mapping using SINAS?',
          'value': 'perf-tmp'
        },
        {
          'text': 'What is Thermal Model Reduction?',
          'value': 'tmr'
        },
        {
          'text': 'Can you perform Thermal Model Reduction using PythonOCC?',
          'value': 'perf-tmr'
        },
        {
          'text': 'Can I see the tutorials?',
          'value': 'tuts'
        },
      ]
    }).then(function (response) {
      if (response.value === 'tuts') {
        getTutorial();
      }
    });
  }, delay);
};

function provideSuggestionsAgain() {
  BOT_UI.message.add({
    delay: 1000,
    type: 'text',
    content: 'Anything else?'
  });

  suggestedResponses(2000);
};



export {
  BOT_UI,
  provideSuggestionsAgain
};