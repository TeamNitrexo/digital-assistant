function getTutorial() {
  const REQUEST = new XMLHttpRequest();

  REQUEST.addEventListener('load', function (_) {
    const SUBDIRECTORIES = JSON.parse(REQUEST.response);
    const NUM_OF_SUBDIRECTORIES = SUBDIRECTORIES.length;
  });

  REQUEST.open('POST', '/tutorials');
  REQUEST.send();
};

export {
  getTutorial
};