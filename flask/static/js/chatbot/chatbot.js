import "https://cdn.jsdelivr.net/npm/botui/build/botui.js";



const BOT_UI = new BotUI('nitrexo-bot');

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
                // BOT_UI.message.add({
                //     type: 'html',
                //     content: `<video src="static/tutorials/file.mp4" height="200" width="300" controls></video>`
                // });



                const REQUEST = new XMLHttpRequest();

                REQUEST.addEventListener('load', function (_) {
                  const SUBDIRECTORIES = JSON.parse(REQUEST.response);
                });

                REQUEST.open('POST', '/tutorials');
                REQUEST.send();
            }
        });
    }, delay);
};

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