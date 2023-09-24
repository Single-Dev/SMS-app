<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container">
      <router-link to="/" class="navbar-brand">Your App Name</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/about" class="nav-link">About</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contact" class="nav-link">Contact</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
/* Custom styles for the Navbar */
.navbar {
  border-radius: 0;
  padding: 20px 0; /* Increase top and bottom padding */
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
}

.navbar-brand {
  font-size: 32px;
  font-weight: bold;
}

.navbar-toggler-icon {
  background-color: #fff;
  border-radius: 4px;
}

.nav-item {
  margin: 0 20px;
}

.nav-link {
  color: #fff;
  font-weight: 600;
  font-size: 18px;
  transition: color 0.3s ease-in-out;
}

.nav-link:hover {
  color: #f8f9fa; /* Lighter color on hover */
}

/* Add a background color change on scroll */
.navbar.scrolled {
  background-color: #fff;
  transition: background-color 0.3s ease-in-out;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
}

.nav-link.scrolled {
  color: #333; /* Change text color on scroll */
}
</style>
