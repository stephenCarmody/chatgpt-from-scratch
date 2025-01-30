<template>
  <div class="chat-sidebar">
    <div class="new-chat">
      <button @click="startNewChat">New Chat</button>
    </div>
    <div class="chat-list">
      <div 
        v-for="chat in chats" 
        :key="chat.id" 
        @click="selectChat(chat.id)"
        :class="['chat-item', { active: currentChatId === chat.id }]"
      >
        {{ chat.title }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatSidebar',
  props: {
    chats: {
      type: Array,
      required: true
    },
    currentChatId: {
      type: Number,
      default: null
    }
  },
  methods: {
    startNewChat() {
      this.$emit('new-chat')
    },
    selectChat(chatId) {
      this.$emit('chat-selected', chatId)
    }
  }
}
</script>

<style scoped>
.chat-sidebar {
  width: 260px;
  background: #f7f7f8;
  border-right: 1px solid #e5e5e5;
  padding: 1rem;
  text-align: center;
}

.new-chat {
  margin-bottom: 20px;
}

.new-chat button {
  width: 100%;
  padding: 12px;
  background-color: #10a37f;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
}

.new-chat button:hover {
  background-color: #0e906f;
}

.chat-list {
  flex: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.chat-item {
  padding: 12px 8px;
  cursor: pointer;
  border-radius: 6px;
  transition: background-color 0.2s;
  font-size: 14px;
  color: #4b5563;
}

.chat-item:hover {
  background-color: #e5e7eb;
}

.chat-item.active {
  background-color: rgba(16, 163, 127, 0.1);
  color: #10a37f;
  font-weight: 500;
}
</style> 