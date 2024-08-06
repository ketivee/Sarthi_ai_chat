document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const message = chatInput.value.trim();
        if (message) {
            // Display user's message
            const userMessage = document.createElement('p');
            userMessage.textContent = `You: ${message}`;
            chatMessages.appendChild(userMessage);

            // Clear input
            chatInput.value = '';

            // Simulate AI response
            setTimeout(() => {
                const aiMessage = document.createElement('p');
                aiMessage.textContent = `AI: This is a response to "${message}"`;
                chatMessages.appendChild(aiMessage);
                chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to bottom
            }, 1000);
        }
    });
});
