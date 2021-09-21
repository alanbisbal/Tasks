<template>
<div>
   <task_show></task_show>
  </div>
</template>

<script>



import task_show from "@/components/Task/show.vue";
import axios from 'axios';
export default {
  name: 'App',
  components: {
    task_show
  },
  
  data: () => ({
    result: null,
  }),
  created() {
    axios
      .get('http://localhost:5000/api/1/folders/1/tasks')
      .then((result) => {
        this.result = result.data;
      });
  },
};
</script>
