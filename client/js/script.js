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

    const tiposOperacao = {
        1: { descricao: "Débito", valor: 1 },
        2: { descricao: "Boleto", valor: -1 },
        3: { descricao: "Financiamento", valor: -1 },
        4: { descricao: "Crédito", valor: 1 },
        5: { descricao: "Recebimento Empréstimo", valor: 1 },
        6: { descricao: "Vendas", valor: 1 },
        7: { descricao: "Recebimento TED", valor: 1 },
        8: { descricao: "Recebimento DOC", valor: 1 },
        9: { descricao: "Aluguel", valor: -1 }
    };
    
    // Função para carregar transações da API
    function consultar_cnab() {
        fetch("http://127.0.0.1:8000/cnab/consultar_cnab")
            .then(response => response.json())
            .then(data => {
                const tabela = document.getElementById("transacoes");
                const saldoElement = document.getElementById("saldo");
                tabela.innerHTML = ""; // Limpa a tabela
                let saldo = 0;
    
                data.forEach(transacao => {
                    const tipo = tiposOperacao[transacao.tipo_transacao] || { descricao: "Desconhecido", valor: 0 };
                    const valor = transacao.valor_transacao * tipo.valor; // Ajusta o valor conforme o tipo
                    saldo += valor;
    
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${tipo.descricao}</td>
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
    
                saldoElement.innerText = `Saldo Total: R$ ${saldo.toFixed(2)}`;
            })
            .catch(error => console.error("Erro ao carregar transações:", error));
    }
    

});
