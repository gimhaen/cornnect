<template>
  <div>
    <TalkCreate :tmdb_id="tmdb_id" />
    <ul  class="talk-list">
      <TalkList
        v-for="talk in talks"
        :key="talk.id"
        :talk="talk"
      />
    </ul>
  </div>
</template>
  
<script setup>
  import TalkCreate from '../components/TalkCreate.vue';
  import TalkList from '../components/TalkList.vue';
  import { ref, onMounted, computed } from 'vue';
  import { useRouter, useRoute } from 'vue-router';
  import { useMovieStore } from '../stores/movie';
  import { useAuthStore } from '../stores/auth';
  import { useTalkStore} from '../stores/talks';
  const authStore = useAuthStore()
  // const router = useRouter()
  const route = useRoute()
  const talkStore = useTalkStore()
  const tmdb_id = route.params.tmdb_id;
  const talks = computed(()=>talkStore.talks)

  
  onMounted(async () => {
    await talkStore.getTalks(tmdb_id);
    console.log(talkStore.talks)
  });
</script>

<style scoped>
.talk-list {
  list-style: none;
  padding: 0;
}

.talk-item {
  font-size: 14px;
  margin-bottom: 10px;
}

.talk-id {
  font-weight: bold;
  margin-right: 5px;
}

.talk-content {
  margin-left: 5px;
}
</style>

