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
                'text':'Thermo-elastic Verification',
                'value':'tev'
                },
                {
                'text':'Can you perform Temperature Mapping?',
                'value':'perf-tmp'
                },
                {
                'text':'Thermal Model Reduction',
                'value':'tmr'
                },
                {
                'text':'Can you perform Thermal Model Reduction?',
                'value':'perf-tmr'
                },
                {
                'text':'Can I view the tutorials?',
                'value':'tuts'
                },
            ]
        }).then(function (response) {
            if (response.value === 'tuts') {
              const PATH_TO_TUTORIAL_VIDEO = getTutorial();

              console.log(PATH_TO_TUTORIAL_VIDEO);

              // BOT_UI.message.add({
              //     type: 'html',
              //     content: `<video src="static/tutorials/${PATH_TO_TUTORIAL_VIDEO}" height="200" width="300" controls></video>`
              // });
            }
        });
    }, delay);
};



export {
  BOT_UI
};