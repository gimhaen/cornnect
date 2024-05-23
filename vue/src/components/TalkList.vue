<template>
    <div  v-if="talk" class="talk-item">
      <span class="talk-author">{{ talk.user.username }} | </span>
      <span class="talk-content">{{ talk.content }}</span>
      <button 
        v-if="talk.user.username === authStore.user.username"
        @click="talkDelete"
      >
        🗑
      </button>
    </div>
  </template>
  
  <script setup>
  import { useTalkStore } from '../stores/talks.js';
  import { useAuthStore } from '../stores/auth.js';
  import { defineProps } from 'vue';

  const authStore = useAuthStore()
  const store = useTalkStore()
  const props = defineProps({
    talk: Object,
    tmdb_id: Number,
    talk_id: Number
  })
  console.log("Delete",props.target)
 const talkDelete = async () => {
    try {
        await store.talkDelete(props.tmdb_id, props.talk_id);
        // Fetch the updated talk list if necessary
        await store.getTalks(props.tmdb_id);
    } catch (error) {
        console.error('Error deleting comment:', error);
    }
    };
  </script>
  
  <style scoped>
  .talk-author {
  font-weight: bold;
  margin-right: 5px;
}
.talk-content {
  margin-left: 5px;
}
  </style>