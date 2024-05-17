<template>
    <div>
        <div class="post">
            <div class="post-container">
                <img src="@/components/뛰는 치이카와.png" alt="user img" class="user-img">
                <div>
                    <h4 class="post-user">유저이름</h4>
                    <p class="post-time">작성 시각</p>
                    <p class="post-content">이 곳은 영화 리뷰를 쓰는 곳입니다.</p>
                    <img src="@/components/치이카와와 하치와레.jpg" alt="post img" class="post-img">
                    <div class="post-actions">
                        <img src="@/components/자기 전 치이카와.png" alt="like img" class="post-icon-img">
                        <span class="post-icon-content">좋아요 n</span>
                        <img src="@/components/자기 전 치이카와.png" alt="comment img" class="post-icon-img">
                        <span class="post-icon-content">댓글 n</span>
                    </div>
                </div>
            </div>
            <hr>
        </div>
    </div>
</template>

<script setup>
// export default {
//   name: 'Post'
// };
</script>

<style scoped>
.post {
  /* background: white;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px; */
}

.post-container {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.post-user {
    /* padding-bottom: 0; */
    margin-bottom: 0;
}

.post-time {
    /* padding-top: 0; */
    margin-top: 0;
    font-size: 13px;
    color: #888;
}

.post-content {
    /* padding-top: 0; */
    margin-top: 0;
}

.user-img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-right: 10px;
    margin-bottom: auto;
    margin-top: 10px;
}

.post-img {
    width: 500px;
    max-height: 500px;
    /* height: 500px; */
    object-fit: contain;
}

.post-icon-img {
    width: 40px;
    height: 40px;
}

.post-icon-content {
    margin-right: 40px;
    font-size: 14px;
    color: #555;
}

.post-user-info {
  display: flex;
  flex-direction: column;
}

.post-content {
  font-size: 1rem;
  margin: 10px 0;
}

.post-actions {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}
</style>