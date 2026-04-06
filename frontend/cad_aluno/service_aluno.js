import { cadastrar_aluno } from "./api_aluno.js";


// Formulario e btn
const form = document.getElementById("cadastro-aluno");
const btnCadastrar = document.getElementById("btn-cadastrar");


// -----------------------------
// Evento de submit do formulário
// -----------------------------
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    if (btnCadastrar.disabled) return;

    btnCadastrar.disabled = true;

    try {
        processarCadastro();

    } catch (error) {
        alert("Erro inesperado");
        console.error("Erro inesperado: ", error);

    } finally {
        btnCadastrar.disabled = false;
    }
});



async function processarCadastro() {
    const payload = getFormData();
    console.log("payload: ", payload)
    const response = await cadastrar_aluno(payload);
    handleResponse(response);
};


// Return payload
function getFormData() {
    // pega a string do input, ex: "2026-04-05"
    const dataInput = document.getElementById("data-matricula").value;

    // garante que fique no formato YYYY-MM-DD
    const dataMatricula = new Date(dataInput).toISOString().split('T')[0];

    return {
        nome: document.getElementById("name").value,
        contato: document.getElementById("contato").value,
        data_matricula: dataMatricula, // formato YYYY-MM-DD
        tipo: document.getElementById("tipo").value,
        turno: document.getElementById("turno").value,
        outro_curso: document.getElementById("outro-curso").checked
    };
};


function handleResponse(response) {
    console.log(response)
    if (!response.sucesso) {
        alert("Falha no Cadastro")
        return;
    }

    alert("Sucesso no Cadastro")
};

