<template>
  <div v-if="articleStore.showModal" class="modal-overlay" @click.self="closeModal">
    <div class="modal-container">
      <div class="modal-header">
        <button class="close-button" @click="closeModal">×</button>
      </div>
      <div class="modal-content">
        <input
          type="text"
          v-model="title"
          placeholder="제목을 입력하세요"
          class="input-title"
        />
        <textarea
          v-model="content"
          placeholder="내용을 입력하세요"
          class="input-content"
        ></textarea>
        <button @click="submitPost" class="submit-button">게시</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useArticleStore } from '@/stores/article.js';

const articleStore = useArticleStore();
const title = ref('')
const content = ref('')

const closeModal = () => {
  articleStore.showModal = false
};

const submitPost = () => {
  // Post submission logic here
  console.log('Title:', title.value);
  console.log('Content:', content.value);
  closeModal();
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-container {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  width: 500px;
  max-width: 100%;
}

.modal-header {
  display: flex;
  justify-content: flex-end;
  padding: 10px;
  border-bottom: 1px solid #e6e6e6;
}

.close-button {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.modal-content {
  padding: 20px;
}

.input-title,
.input-content {
  width: 95%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.input-content {
  min-height: 100px;
  resize: vertical;
}

.submit-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>
