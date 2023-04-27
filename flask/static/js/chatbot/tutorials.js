import {
  BOT_UI,
  provideSuggestionsAgain
} from "./chatbot.js";



let path_to_tutorial_video = '';

function getTutorial() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const OPTIONS = JSON.parse(REQUEST.responseText);
    const NUM_OF_OPTIONS = OPTIONS.length;

    const ACTIONS = [{
      'text': 'Go back',
      'value': 'return'
    }];

    for (let i=0; i < NUM_OF_OPTIONS; i++) {
      const OPTION = OPTIONS[i];

      ACTIONS.push({
        'text': OPTION,
        'value': OPTION
      });
    }

    if (ACTIONS.length > 0) {
      BOT_UI.action.button({
        action: ACTIONS
      }).then(function (response) {
        if (response.value === 'return') {
          if (path_to_tutorial_video.length === 0) {
            provideSuggestionsAgain();
          }
          else {
            const INDEX_OF_LAST_SLASH = path_to_tutorial_video.lastIndexOf('/');

            // resets path to the previous one
            path_to_tutorial_video = path_to_tutorial_video.substring(0, INDEX_OF_LAST_SLASH);

            getTutorial();
          }
        }
        else {
          path_to_tutorial_video += '/' + response.value;

          if (/.mp4$/.test(path_to_tutorial_video)) {
            // removes existing videos
            const EXISTING_VIDEOS = document.getElementsByTagName('video');
            const NUM_OF_EXISTING_VIDEOS = EXISTING_VIDEOS.length;

            for (let i=0; i < NUM_OF_EXISTING_VIDEOS; i++) {
              const VIDEO = EXISTING_VIDEOS[i];

              VIDEO.pause();
              VIDEO.removeAttribute('src');
              VIDEO.load();
              VIDEO.parentElement.parentElement.remove();
            }

            // loads in new video
            BOT_UI.message.add({
                type: 'html',
                content: `<video src="static/tutorials/${path_to_tutorial_video}" height="200" width="300" controls></video>`
            });

            path_to_tutorial_video = '';

            provideSuggestionsAgain();
          }
          else {
            getTutorial();
          }
        }
      });
    }
    else {
      BOT_UI.message.add({
        delay: 1000,
        type: 'text',
        content: 'Unfortunately, there are no tutorial videos for this topic.'
      });

      provideSuggestionsAgain();
    }
  });

  REQUEST.open('POST', '/tutorials');
  REQUEST.setRequestHeader('content-type', 'application/json');
  REQUEST.send(JSON.stringify(path_to_tutorial_video));
};

export {
  getTutorial
};