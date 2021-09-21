<template>
<div>
    <div class="content">
    <div v-for="item in this.result.folders" :key="item.id">     
        {{item.name}} 
       
    </div>
    </div>
    
  </div>

</template>

<script>






import axios from 'axios';


export default {
  name: 'App',
  components: {
  },
  data: () => ({
    result: null,
  }),
  created() {
    axios
      .get('http://localhost:5000/api/1/folders')
      .then((result) => {
        this.result = result.data;
        console.log(this.result)
      });
  },
 
};
</script>
