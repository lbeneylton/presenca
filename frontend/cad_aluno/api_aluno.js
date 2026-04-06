import { API_BASE_URL } from "../shared/config.js";
import { POST } from "../shared/objetos.api.js";

export async function cadastrar_aluno(payload) {
    try {
        const response = await fetch(`${API_BASE_URL}/aluno/cadastrar`, POST(payload));
        const data = await response.json();

        // Se a resposta n for 2xx
        if (!response.ok) {
            const errorMessage = data?.detail || "Erro no cadastro";
            return { sucesso: false, mensagem: errorMessage };
        };

        return { sucesso: true, mensagem: data };

    } catch (error) {
        return { sucesso: false, mensagem: `Erro de conexão ${error}` };
    };
};
