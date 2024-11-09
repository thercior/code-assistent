document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        scroollBotom();
    }, 1000)
})

const messagesList = document.getElementById('messagesList');
const messageForm = document.getElementById('messageForm');
const messageInput = document.getElementById('messageInput');

messageForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (!message) return;

    // Add user message
    addMessageToChat(message, 'Você', 'end');

    messageInput.value = '';

    try {
        const response = await fetch('', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                'csrfmiddlewaretoken': document.querySelector('[name="csrfmiddlewaretoken"]').value,
                'message': message
            })
        });
    
        const data = await response.json();
        addMessageToChat(data.response, 'Ai Chatbot', 'start');
    } catch (error) {
        console.error('Erro ao enviar a mensagem: ', error);
    }
    
});

function scroollBotom() {
    // messagesList.scrollTop = messagesList.scrollHeight;
    messagesList.scrollTo({
        top: messagesList.scrollHeight,
        behavior: 'smooth'
    });
}

function addMessageToChat(content, sender, align) {
    const messageItem = document.createElement('div');
    messageItem.classList.add('flex', align === 'end' ? 'justify-end' : 'justify-start');

    messageItem.innerHTML = `
        <div class="bg-${align === 'end' ? 'blue-300' : 'gray-900'} bg-${align === 'end' ? 'opacity-100' : 'opacity-50'} text-${align === 'end' ? 'gray-800' : 'gray-400'} p-3 rounded-lg w-auto max-w-screen-md text-justify shadow-sm">
            <div><strong>${sender}</strong></div>
            <div class="markdown-content">
                ${content}
            </div>
        </div>
    `;

    messagesList.appendChild(messageItem);
   scroollBotom();  // Scroll to the latest message
}
