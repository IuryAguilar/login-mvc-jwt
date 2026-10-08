const elements = {
    login_form: document.getElementById('loginForm'),
    email_input: document.getElementById('emailI'),
    senha_input: document.getElementById('senhaI'),
    error_msg: document.getElementById('error'),
    login_button: document.getElementById('loginBtn')
};

elements.login_form.addEventListener("submit", async (event) => {
    event.preventDefault();

    elements.error_msg.textContent = "";
    
    const email = elements.email_input.value.trim();
    const senha = elements.senha_input.value.trim();

    if (!validar_email(email)) {
        elements.error_msg.textContent = "E-mail inválido.";
        return;
    };

    const resposta = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'email': email,
            'senha': senha
        })
    });

    const dados = await resposta.json();

    if (dados.sucesso) {
        localStorage.setItem("token", dados.token);
        window.location.href = "perfil.html";
    } else {
        elements.error_msg.textContent = dados.detail;
    };
});

function validar_email(email){
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}