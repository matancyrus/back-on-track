//Constants
const getButton = document.getElementById("show-get");
const setButton = document.getElementById("show-set");
const addSection = document.getElementById("set-section");
const getSection = document.getElementById("get-section");
const getForm = document.getElementById("get-form");
const setForm = document.getElementById("set-form");
const getSnippetKey = document.getElementById("get-snippetkey");
const setSnippetKey = document.getElementById("set-snippetkey");
const setSnippetvalue = document.getElementById("set-snippetvalue");
const resultBox = document.getElementById("result-box");

setButton.addEventListener("click", function () {
    addSection.classList.remove("hidden")
    getSection.classList.add("hidden")
    resultBox.classList.add("hidden")
});

getButton.addEventListener("click", function () {
    getSection.classList.remove("hidden")
    addSection.classList.add("hidden")
});


getForm.addEventListener("submit", async function (event) {
  event.preventDefault();
  const key = getSnippetKey.value;
  const response = await fetch(`/api/get/${encodeURIComponent(key)}`);
  const data = await response.json();

  resultBox.classList.remove("hidden");
  resultBox.textContent = data.value;
});


setForm.addEventListener("submit", async function (event) {
  event.preventDefault();
  const key = setSnippetKey.value;
  const data = setSnippetvalue.value
  const response = await fetch(`/api/set?key=${encodeURIComponent(key)}&value=${encodeURIComponent(data)}`, {method: 'POST'});

});
