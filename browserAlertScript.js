callback = () => { if (targetNode.textContent === "В эфире") alert("Время побеждать!!!") }

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