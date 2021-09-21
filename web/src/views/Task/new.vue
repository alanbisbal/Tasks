<template>
 <new_form/>
</template>

<script>

import axios from 'axios';
import new_form from '@/components/Task/new.vue';
export default {

name: 'index',
  components: {
    new_form,
  },
  
  data: () => ({
    result: null,
  }),
  
  created() {
    axios
      .get('')
      .then((result) => {
        this.result = result.data;
      });
  },
};
</script>

<style scoped lang="scss"></style>
