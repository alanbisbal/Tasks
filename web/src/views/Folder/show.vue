<template>
<div>

  <folder_show></folder_show>

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


import folder_show from "@/components/Folder/show.vue";
export default {
  name: 'App',
  components: {
    folder_show,
  },

};
</script>

