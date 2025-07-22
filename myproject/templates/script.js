function openCamera() {
    fetch("/start")
    .then(response => response.text())
    .then(data => alert(data));
      // Replace with your IP Webcam stream URL
};