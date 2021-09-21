<template>
  <b-container fluid>
    <div class="container col-md-8 col-sm-12">
      <b-card-group deck>
        <b-card
          bg-variant="ligth"
          header="New Folder"
          class="text-center"
          header-tag="header"
          header-bg-variant="primary"
          header-text-variant="white"
          style="max-width: 50rem;"
          align="center"
        >
          <b-form @submit="onSubmit" @reset="onReset" >
            <b-form-group label="Name:">
              <b-form-input
                v-model="form.name"
                type="text"
                required
                placeholder="Name..."
              ></b-form-input>
            </b-form-group>

          </b-form>
        </b-card>
      </b-card-group>
    </div>
  </b-container>
</template>

<script>

import axios from 'axios';
export default {
  name: 'folder_new',
  data() {
    return {
      form: {
        name: '',
      },
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      const url =
        'http://127.0.0.1:5000/api/1/folders/create';
      axios({
        method: 'POST',
        url,
        headers: {
          'Content-Type': 'application/json',
        },
        data: JSON.stringify(this.form),
      })
        .then((response) => {
          console.log(response);
          this.flash(
            'Success!',
            'success'
          );
          this.$router.push({ name: 'home' });
        })
        .catch((error) => {
          if (error.response) {
            console.log('Error! response:', error.response.data);
            this.flash(error.response.data, 'error');
          }
        });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = '';
      },
  },
};
</script>

