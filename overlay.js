document.addEventListener("DOMContentLoaded", (event) => {
  const pyOverlay = document.querySelectorAll(".py-overlay")[1];
  const myOverlay = document.querySelector(".my-overlay");
  const plot = document.querySelector("#plot");

  // Set default pyScript loading overlay to display: none.
  pyOverlay.classList.add("hidden");

  // Create mutation observer to hide my-overlay when triggered
  observer = new MutationObserver(function (mutationsList, observer) {
    console.log(mutationsList);
    myOverlay.classList.toggle("hidden");
  });

  // Set observer to observe .plot div for changes in child list.
  observer.observe(plot, {
    characterData: false,
    childList: true,
    attributes: false,
  });
});
