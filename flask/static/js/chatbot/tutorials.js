import {
  BOT_UI,
  suggestedResponses
} from "./chatbot.js";



let path_to_tutorial_video = '';

function getTutorial() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const OPTIONS = JSON.parse(REQUEST.responseText);
    const NUM_OF_OPTIONS = OPTIONS.length;

    const ACTIONS = [];

    for (let i=0; i < NUM_OF_OPTIONS; i++) {
      const OPTION = OPTIONS[i];

      ACTIONS.push({
        'text': OPTION,
        'value': OPTION
      });
    }

    BOT_UI.action.button({
      action: ACTIONS
    }).then(function (response) {
      path_to_tutorial_video += '/' + response.value;

      if (/.mp4$/.test(path_to_tutorial_video)) {
        BOT_UI.message.add({
            type: 'html',
            content: `<video src="static/tutorials/${path_to_tutorial_video}" height="200" width="300" controls></video>`
        });

        BOT_UI.message.add({
          delay: 1000,
          type: 'text',
          content: 'Anything else?'
        });

        suggestedResponses(2000);
      }
      else {
        getTutorial();
      }
    });
  });

  REQUEST.open('POST', '/tutorials');
  REQUEST.setRequestHeader('content-type', 'application/json');
  REQUEST.send(JSON.stringify(path_to_tutorial_video));
};

export {
  getTutorial
};