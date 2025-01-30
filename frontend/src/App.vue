<script>
import ChatSidebar from './components/ChatSidebar.vue'
import ChatWindow from './components/ChatWindow.vue'

export default {
  name: 'App',
  components: {
    ChatSidebar,
    ChatWindow
  },
  data() {
    return {
      chats: [],
      currentChatId: null,
      chatCounter: 0
    }
  },
  created() {
    // Create initial chat
    this.createNewChat()
  },
  methods: {
    handleChatSelect(chatId) {
      this.currentChatId = chatId
    },
    createNewChat() {
      this.chatCounter++
      const newChat = {
        id: Date.now(),
        title: `Chat ${this.chatCounter}`,
        messages: []
      }
      this.chats.push(newChat)
      this.currentChatId = newChat.id
      return newChat
    },
    handleNewChat() {
      this.createNewChat()
    },
    async handleNewMessage(message) {
      let currentChat = this.chats.find(chat => chat.id === this.currentChatId)
      
      // If no current chat, create one
      if (!currentChat) {
        currentChat = this.createNewChat()
      }

      // Add user message
      currentChat.messages.push({
        id: Date.now(),
        role: 'user',
        content: message
      })

      try {
        // Simulate API call - replace with actual API call
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            message: message
          })
        })

        const data = await response.json()
        
        // Add assistant message
        currentChat.messages.push({
          id: Date.now() + 1,
          role: 'assistant',
          content: data.response
        })
      } catch (error) {
        console.error('Error:', error)
        // Handle error appropriately
      }
    }
  }
}
</script>

<template>
  <ChatSidebar 
    :chats="chats"
    :currentChatId="currentChatId"
    @chat-selected="handleChatSelect"
    @new-chat="handleNewChat"
  />
  <ChatWindow 
    :messages="currentChatId ? (chats.find(c => c.id === currentChatId)?.messages || []) : []"
    @send-message="handleNewMessage"
  />
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
}

#app {
  display: flex;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
}

::-webkit-scrollbar {
  width: 0.5rem;
}

::-webkit-scrollbar-track {
  background: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: #d1d5db;
  border-radius: 0.25rem;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #9ca3af;
}

textarea:focus {
  outline: none;
}
</style>
