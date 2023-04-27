// BOT_UI.message.add({
//     type: 'html',
//     content: `<video src="static/tutorials/file.mp4" height="200" width="300" controls></video>`
// });



function getTutorial() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const SUBDIRECTORIES = JSON.parse(REQUEST.response);
    const NUM_OF_SUBDIRECTORIES = SUBDIRECTORIES.length;

    const ACTIONS = [];

    for (let i=0; i < NUM_OF_SUBDIRECTORIES; i++) {
      ACTIONS.push({
        'text': SUBDIRECTORIES[i],
        'value': 'tuts'
      });
    }

    BOT_UI.action.button({
        action: ACTIONS
    });
  });

  REQUEST.open('POST', '/tutorials');
  REQUEST.send();
};

export {
  getTutorial
};