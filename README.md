# edcp
Editor de código simples

<img width="953" height="892" alt="Captura de tela 2025-08-09 003359" src="https://github.com/user-attachments/assets/e61443cb-6ac2-4cf2-b0e3-2990b2759ec3" />

## 🛠️ Funcionalidades Principais

| Funcionalidade | Descrição |
|----------------|-----------|
| 🌑 Tema Escuro Moderno | Interface com aparência profissional usando `customtkinter` no modo dark |
| 🔢 Números de Linha | Painel lateral com números de linha sempre atualizados |
| 🔄 Scroll Sincronizado | Rolagem vertical sincronizada entre texto e números de linha |
| 📁 Abrir Arquivo (GUI) | Seleção de arquivos via janela gráfica (`filedialog`) |
| 📥 Abrir via Terminal | Suporte a argumentos: `python edcp.py arquivo.txt` |
| 💾 Salvar com `Ctrl+S` | Atalho rápido para salvar alterações no arquivo atual |
| ➖ Sem Quebra de Linha | `wrap="none"` permite rolagem horizontal (ideal para código) |
| 📦 Leitura em Blocos | Carrega arquivos grandes em pedaços para evitar travamentos |
| 🔤 Codificação UTF-8 | Suporte completo a acentos e caracteres internacionais |
| █ Cursor Visível | Cursor branco e mais largo para melhor visibilidade |
| 🖊️ Destaque da Linha Atual | Número da linha do cursor é exibido em branco (destaque) |
| ↔️ Barra de Rolagem Horizontal | Permite navegar em linhas longas |


---

Este software tem como intuito, ao ser passado o nome de um arquivo qualquer por argumento, o edcp "editor de código simples" ler o conteudo do arquivo. E
ele não é apenas isso mas, sim, ler arquivos grandes de forma eficiente e, não pesar na leitura.



| Biblioteca | Necessita Instalação? | Observações |
|----------|----------------------|-------------|
| `customtkinter` | ✅ Sim | Interface gráfica moderna |
| `tkinter` | ❌ Não | Biblioteca padrão do Python (GUI básica) |
| `os` | ❌ Não | Módulo padrão para operações com sistema |
| `sys` | ❌ Não | Módulo padrão para argumentos da linha de comando |
