<template>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
 >
   {{name}}
   List tasks: 
   <task_index></task_index>
  </div>
</template>

<script>

import task_index from "@/components/Task/index.vue";

export default {
  name: 'App',
  components: {
    task_index
  },
  props: {
    name: String
     
    }
};
</script>
