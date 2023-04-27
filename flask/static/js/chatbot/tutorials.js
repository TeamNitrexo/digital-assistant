import { BOT_UI } from "./chatbot.js";



function getTutorial() {
  let path_to_tutorial_video = '/';

  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const SUBDIRECTORIES = JSON.parse(REQUEST.response);
    const NUM_OF_SUBDIRECTORIES = SUBDIRECTORIES.length;
  });

  REQUEST.open('POST', '/tutorials');
  REQUEST.send();

  return path_to_tutorial_video;
};

export {
  getTutorial
};