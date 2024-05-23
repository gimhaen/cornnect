<template>
    <form @submit.prevent="createTalk">
      <label for="content">댓글 : </label>
      <input type="text" name="content" id="content" v-model="content">
      <button type="submit">입력</button>
    </form>
  </template>
  
  <script setup>
  import { useTalkStore } from '@/stores/talks.js'
  import { ref, defineProps } from 'vue';

  const store = useTalkStore()
  const props = defineProps({
    tmdb_id: Number
  })
  const content = ref('')
  const createTalk = async () => {
    console.log(props.tmdb_id);
    try {
        await store.talkCreate(props.tmdb_id, content.value);
        content.value = ''; // Clear the input after submitting
        // Fetch the updated talk list if necessary
        await store.getTalks(props.tmdb_id);
    } catch (error) {
        console.error('Error creating comment:', error);
    }
    };
  </script>
  
  <style lang="scss" scoped>
  
  </style>