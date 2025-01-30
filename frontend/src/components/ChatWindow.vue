<template>
  <div class="chat-window">
    <div class="messages" ref="messagesContainer">
      <div v-if="messages.length === 0" class="welcome-screen">
        <h1>What can I help with?</h1>
      </div>
      <template v-else>
        <div v-for="message in messages" :key="message.id" class="message" :class="message.role">
          <div class="message-content">{{ message.content }}</div>
        </div>
      </template>
    </div>
    <div class="input-area">
      <textarea 
        v-model="newMessage" 
        @keydown.enter.prevent="sendMessage"
        placeholder="Type a message..."
        rows="1"
        ref="messageInput"
      ></textarea>
      <button @click="sendMessage" :disabled="!newMessage.trim()">Send</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatWindow',
  props: {
    messages: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      newMessage: '',
    }
  },
  methods: {
    async sendMessage() {
      if (!this.newMessage.trim()) return

      const message = this.newMessage.trim()
      this.newMessage = ''
      this.$emit('send-message', message)
    }
  },
  watch: {
    messages: {
      handler() {
        this.$nextTick(() => {
          const container = this.$refs.messagesContainer
          container.scrollTop = container.scrollHeight
        })
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.chat-window {
  flex: 1;
  background: #fff;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
}

.welcome-screen {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.welcome-screen h1 {
  color: #374151;
  font-size: 40px;
  font-weight: 500;
  opacity: 0.8;
}

.message {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  padding: 0;
  margin-bottom: 1rem;
  padding-left: 4rem;
  padding-right: 4rem;
  margin-left: 6rem;
  margin-right: 6rem;
}

.message.user {
  background-color: #efefef;
  border-radius: 16px;
  max-width: 60%;
  width: fit-content;
  display: inline-flex;
  flex-direction: column;
  justify-content: flex-end;
}

.message.assistant {
  background-color: #ffffff;
  margin-left: auto;
}

.message-content {
  display: flex;
  flex-direction: column;
  width: auto;
  margin: 0;
  padding: 8px;
  color: #374151;
  line-height: 1.6;
  word-break: break-word;
}

.input-area {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20px;
  background-color: #ffffff;
  border-top: 1px solid #e5e5e5;
  display: flex;
  justify-content: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.input-area textarea {
  width: 100%;
  max-width: 800px;
  background-color: #ffffff;
  border: 1px solid #e5e5e5;
  color: #374151;
  padding: 12px 45px 12px 12px;
  border-radius: 8px;
  resize: none;
  min-height: 52px;
  line-height: 1.5;
  font-size: 14px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.input-area textarea:focus {
  border-color: #10a37f;
  box-shadow: 0 2px 6px rgba(16, 163, 127, 0.1);
}

.input-area button {
  position: absolute;
  right: calc(50% - 380px);
  top: 50%;
  transform: translateY(-50%);
  padding: 8px 16px;
  background-color: #10a37f;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.2s;
}

.input-area button:hover {
  background-color: #0e906f;
}

.input-area button:disabled {
  background-color: #e5e5e5;
  cursor: not-allowed;
}

@media (max-width: 800px) {
  .input-area {
    padding: 24px 16px;
  }
  
  .input-area button {
    right: 30px;
  }
}
</style> 