document.addEventListener("DOMContentLoaded", function () {
    // Envio do arquivo
    document.getElementById("uploadForm").addEventListener("submit", function (event) {
        event.preventDefault();
        const fileInput = document.getElementById("fileInput").files[0];
        if (!fileInput) {
            alert("Por favor, selecione um arquivo.");
            return;
        }

        const formData = new FormData();
        formData.append("file", fileInput);

        fetch("http://127.0.0.1:8000/cnab/enviar_cnab", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            alert("Arquivo enviado com sucesso!");
            consultar_cnab(); // Atualiza a tabela após envio
        })
        .catch(error => console.error("Erro ao enviar arquivo:", error));
    });

    // Função para carregar transações da API
    function consultar_cnab() {
        fetch("http://127.0.0.1:8000/cnab/consultar_cnab")
            .then(response => response.json())
            .then(data => {
                const tabela = document.getElementById("transacoes");
                tabela.innerHTML = ""; // Limpa a tabela antes de preencher

                data.forEach(transacao => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${transacao.tipo_transacao}</td>
                        <td>${transacao.data_transacao}</td>
                        <td>R$ ${transacao.valor_transacao.toFixed(2)}</td>
                        <td>${transacao.cpf_transacao}</td>
                        <td>${transacao.cartao_transacao}</td>
                        <td>${transacao.hora_transacao}</td>
                        <td>${transacao.dono_da_loja}</td>
                        <td>${transacao.nome_da_loja}</td>
                    `;
                    tabela.appendChild(row);
                });
            })
            .catch(error => console.error("Erro ao carregar transações:", error));
    }

});
