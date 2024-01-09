function submitForm() {
    const textForm = document.getElementById("textForm");
    const imageContainer = document.getElementById("imageContainer");
    const textInput = document.getElementById("text").value;

    const formData = new FormData();
    formData.append("text", textInput);

    fetch("http://127.0.0.1:8000/process_text", {
        method: "POST",
        body: formData,
    })
    .then(response => response.blob())
    .then(blob => {
        const imageUrl = URL.createObjectURL(blob);
        const image = new Image();
        image.src = imageUrl;
        imageContainer.innerHTML = "";
        imageContainer.appendChild(image);
    })
    .catch(error => console.error("Error:", error));
}
