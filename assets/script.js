async function createAccount() {
    const data = {
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value,
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };
    const res = await fetch("http://127.0.0.1:5000/api/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    const msg = await res.json();
    document.getElementById("message").textContent = msg.message;
}

async function login() {
    const data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value
    };
    const res = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    const msg = await res.json();
    document.getElementById("message").textContent = msg.message;

    if (res.ok && msg.message.startsWith("Connecté")) {
        window.location.href = "../templates/index.html";
    }
}
