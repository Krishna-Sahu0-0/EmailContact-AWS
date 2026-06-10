async function sendMessage() {

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value
    };

    const response = await fetch(
        "https://x8052djvfc.execute-api.ap-south-1.amazonaws.com/contact-us",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );

    const result = await response.json();

    document.getElementById("status").innerText =
        result.message || result.error;
}