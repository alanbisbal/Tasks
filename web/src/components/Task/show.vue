<template>
  <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
 >
    <div class="container mt-4 text-center">
      <p>
         {{name}} 
      </p>
      show tasks
    </div>
    <myMap />
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
      .get('http://localhost:5000/api/1/folders/1/tasks')
      .then((result) => {
        this.result = result.data;
      });
  },
};
</script>

