# 💬 Automação de mensagens no WhatsApp para lembrar meu supervisor

Criei esse projeto porque tinha um problema simples, mas chato:  
eu sempre esquecia de lembrar meu supervisor sobre projetos que estavam esperando aprovação.

Eu precisava mandar mensagem manual todo dia pelo WhatsApp, e com a correria acabava esquecendo ou mandando tarde demais.

Então pensei:  
**"Por que não automatizar isso?"**

---

## ✅ O que o script faz

- Lê uma planilha (`messages.csv`) com os projetos e mensagens
- Envia mensagens automáticas via WhatsApp Web usando o navegador Edge
- Usa o Selenium para automatizar o envio
- É executado todos os dias automaticamente no horário definido
- Para de enviar quando o status do projeto muda para "Aprovado"

---

## 🛠️ Tecnologias usadas

- Python
- Selenium
- Microsoft Edge WebDriver
- Agendador de Tarefas do Windows

