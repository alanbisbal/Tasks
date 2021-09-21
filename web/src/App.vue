<template>
  <div id="app">
    <div id="nav">
      <b-navbar toggleable="md" variant="dark">
        <b-container>
          <b-collapse id="nav-collapse" is-nav>
              <b-nav-item :to="{ name: 'home' }" exact>Home</b-nav-item>
              <b-nav-item :to="{ name: 'folder_index' }" exact>Folders</b-nav-item>
            </b-collapse>
        </b-container>
      </b-navbar>
    </div>

    <flash-message
      transitionIn="animated swing"
      class="myCustomClass"
    ></flash-message>
    <router-view />

    <footer class="footer-copyright text-center py-3">
      <p class="p-1">
        ToDoTask &copy; Bisbal, Alan |
      </p>
    </footer>
  </div>
</template>

<script>
require('vue-flash-message/dist/vue-flash-message.min.css');
</script>
