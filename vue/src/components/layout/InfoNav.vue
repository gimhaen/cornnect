<template>
    <nav class="info-nav-ver">
        <div class="info-nav-container">
            <BoxOffice class="box-office" />
            <TalkList class="talklist" />   
        </div>        
    </nav>

  </template>
  
  <script setup>
  import BoxOffice from '@/components/BoxOffice.vue'
  import TalkList from '@/components/TalkList.vue'
  </script>
  
  <style scoped>
    .info-nav-ver {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;

    border: 1px solid #ccc; /* 선택 사항: 게시글 영역에 테두리 추가 */
  }

  .info-nav-container {
    display: flex;
    flex-direction: column;
  }
  
  .box-office {
  }
  
  .talklist {
  }
  </style>
  