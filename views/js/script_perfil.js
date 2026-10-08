const elements = {
    nome_perfil: document.getElementById('nomePerfil'),
    email_perfil: document.getElementById('emailPerfil'),
    sair_botao: document.getElementById('logoutBtn')
};

const token = localStorage.getItem("token");

carregar_perfil()

async function carregar_perfil() {
    if(!token) {
        window.location.href = "login.html"
        return;
    }

    const resposta = await fetch("http://127.0.0.1:8000/perfil", {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    if (resposta.status === 401) {
        localStorage.removeItem("token");
        window.location.href = "login.html";
        return;
    };

    const dados = await resposta.json();

    elements.nome_perfil.textContent = dados.nome;
    elements.email_perfil.textContent = dados.email;

};

elements.sair_botao.addEventListener("click", () => {
    localStorage.removeItem("token");
    window.location.href = "login.html";
});