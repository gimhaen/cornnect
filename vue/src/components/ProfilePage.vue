<template>
  <div v-if="authStore.showModal" class="modal-overlay" @click.self="closeModal">
    <div class="modal-container">
      <button class="close-button" @click="closeModal">×</button>
      <div class="modal-content">
        <h2>프로필 수정</h2>
        <form @submit.prevent="updateProfile">
          <div class="form-group">
            <label for="username"><h3 class="form-title">Username</h3></label>
            <input type="text" v-model="username" id="username" class="form-control">
          </div>
          <div class="form-group">
            <label for="profile_pic"><h3 class="form-title">User Picture</h3></label>
              <div v-if="user.profile_pic">
                <p class="form-img-content">현재 Picture</p>
                <img
                  :src="'http://127.0.0.1:8000' + user.profile_pic"
                  alt="user img"
                  class="form-img"
                />
              </div>  
              <p v-if="!user.profile_pic" class="form-img-content">현재 설정된 Picture이 없습니다.</p>
            <input type="file" @change="onFileChange" id="profile_pic" class="form-control">
          </div>
          <div v-if="previewImage" class="image-preview">
            <img :src="previewImage" alt="Profile Preview">
          </div>
          <div class="button-group">
            <button type="submit" class="submit-button" @click="articleStore.getReviews">Update</button>
            <button type="button" @click="closeModal" class="cancel-button">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth.js'

const authStore = useAuthStore()
const username = ref('')
const previewImage = ref(null)
const imageFile = ref(null)

import { useArticleStore } from '@/stores/article.js';
const articleStore = useArticleStore();

const user = computed(() => authStore.user);

onMounted(()=> {
  username.value = authStore.user.username
})

const onFileChange = (e) => {
  const file = e.target.files[0]
  imageFile.value = file
  if (file) {
    const reader = new FileReader()
    reader.onload = () => {
      previewImage.value = reader.result
    }
    reader.readAsDataURL(file)
  //   user.value.profile_pic = file
  }
}

const closeModal = () => {
  // username.value = ''
  previewImage.value = null
  // imageFile.value = null
  authStore.profileCloseModal()
}

const updateProfile = () => {
  console.log(profile_pic.value)

  authStore.updateUser(username.value, imageFile.value).then(() => {
    closeModal()
  })  
}
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
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  position: relative;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.modal-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-bottom: 30px;
}

.form-title {
  margin: 0;
  padding: 0;
}

.form-img-content {
  margin: 0;
  padding: 0;
}

.form-img {
  border: 1px solid #ccc;
  width: 200px;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.submit-button, .cancel-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.submit-button {
  background-color: #007bff;
  color: white;
}

.cancel-button {
  background-color: #6c757d;
  color: white;
}

.image-preview {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.image-preview img {
  max-width: 100%;
  max-height: 200px;
  border-radius: 4px;
}
</style>
