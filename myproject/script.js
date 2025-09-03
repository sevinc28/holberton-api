const messageBtn = document.getElementById("messageBtn");
const messageDisplay = document.getElementById("messageDisplay");
const messageText = document.getElementById("messageText");
const closeMessage = document.getElementById("closeMessage");

const messages = [
    "Səni hər şeydən çox sevirəm 💖",
    "Sən mənim günəşimsən ☀️",
    "Sənsiz həyatın rəngi yoxdur 🌈",
    "Sənin gülüşün ürəyimi isidir 😊"
];

messageBtn.addEventListener("click", () => {
    let index = parseInt(messageBtn.getAttribute("data-message"));
    messageText.textContent = messages[index];
    messageDisplay.style.display = "block";

    index = (index + 1) % messages.length;
    messageBtn.setAttribute("data-message", index.toString());
});

closeMessage.addEventListener("click", () => {
    messageDisplay.style.display = "none";
});
