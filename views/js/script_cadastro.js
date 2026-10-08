const elements = {
    cadastro_form:document.getElementById('cadastroForm'),
    usuario_input: document.getElementById('usuarioI'),
    email_input: document.getElementById('emailI'),
    senha_input: document.getElementById('senhaI'),
    confirmarSenha_input: document.getElementById('confirmarSenhaI'),
    error_msg: document.getElementById('error'),
    cadastrar_button: document.getElementById('cadastroBTn')
};

elements.cadastro_form.addEventListener("submit", async (event) => {
    event.preventDefault();

    elements.error_msg.textContent = "";

    const usuario = elements.usuario_input.value.trim();
    const email = elements.email_input.value.trim();
    const senha = elements.senha_input.value.trim();
    const confirmarSenha = elements.confirmarSenha_input.value.trim();

    if(usuario === ""){
        elements.error_msg.textContent = "Campo de usuário obrigatório.";
        return;
    }

    if(!validar_email(email)) {
        elements.error_msg.textContent = "E-mail inválido.";
        return;
    };

    if(senha === "") {
        elements.error_msg.textContent = "Campo de senha obrigatório.";
        return;
    }

    if(!validar_senha(senha, confirmarSenha)) {
        elements.error_msg.textContent = "As senhas não coicidem.";
        return;
    };

    const resposta = await fetch("http://127.0.0.1:8000/cadastro", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'nome': usuario,
            'email': email,
            'senha': senha
        })
    });

    const dados = await resposta.json();

    if(dados.sucesso) {
        window.location.href = "login.html"
    } else {
        elements.error_msg.textContent = dados.detail;
    }
});

function validar_email(email){
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
};

function validar_senha(senha, confirmarSenha){
    return senha === confirmarSenha;
};