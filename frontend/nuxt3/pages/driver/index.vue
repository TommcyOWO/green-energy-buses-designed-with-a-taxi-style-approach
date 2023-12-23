<template>
  <div class="abs top:50% left:50% translate(-50%,-50%)">
    <section>
      <div>
        
      </div>
      <button class="btn">搜尋乘客</button>
    </section>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import conf from '@/assets/conf'

const get_passenger =async() => {
  const responses = axios.get(conf.urls+'')
}
</script>
