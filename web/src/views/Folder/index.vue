<template>

  <div>
  <folder_index></folder_index>


    <div class="form-inline">
      <div class="col-auto my-1">
        <b-button variant="primary" :to="{ name: 'folder_new' }"
          >New Folder</b-button
        >
        
      </div>
    </div>   
  </div>
</template>

<script>


import folder_index from "@/components/Folder/index.vue";
export default {
  name: 'App',
  components: {
    folder_index,

  },

};
</script>

