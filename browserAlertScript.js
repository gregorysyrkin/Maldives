callback = () => {
    if (targetNode.textContent === "В эфире") {
        var mp3 = 'https://media.geeksforgeeks.org/wp-content/uploads/20190531135120/beep.mp3';
        for (i = 0; i < 10; i++) {
            setTimeout(function () { (new Audio(mp3)).play() }, i * 1000)
            alert("Не забудьте взять крем от загара.");
        }
    }
}

const observer = new MutationObserver(callback)

const targetNode = document.querySelector(".player__artist.ng-binding");

const observerOptions = {
    childList: true,
    attributes: true,
    characterData: true,
    // Omit (or set to false) to observe only changes to the parent node
    subtree: true
}

observer.observe(targetNode, observerOptions);