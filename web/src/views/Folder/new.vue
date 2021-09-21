<template>
 <new_form></new_form>
</template>

<script>

import axios from 'axios';
import new_form from '@/components/Folder/new.vue';
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
      .get('http://localhost:5000/api/1/folders')
      .then((result) => {
        this.result = result.data;
      });
  },
};
</script>

<style scoped lang="scss"></style>
