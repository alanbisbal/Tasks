<template>

  <div>
  <task_index></task_index>


    <div class="form-inline">
      <div class="col-auto my-1">
        <b-button variant="primary" :to="{ name: 'task_new' }"
          >Task Folder</b-button
        >
        
      </div>
    </div>   
  </div>
</template>

<script>


import task_index from "@/components/Task/index.vue";
export default {
  name: 'App',
  components: {
    task_index,

  },

};
</script>

