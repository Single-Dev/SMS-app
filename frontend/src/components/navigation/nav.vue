<template>
    <div class="navbar">
      <div class="logo">
        <router-link to="/" class="a">Free Cash</router-link>
      </div>
      <ul class="nav-links">
        <li><router-link to="/" class="a">Home</router-link></li>
        <li><router-link to="/login" class="a">Sign In</router-link></li>
        <li><router-link to="/sign-up" class="a">Sign Up</router-link></li>
      </ul>
    </div>
  </template>
  
  <style scoped>
  /* Navbar styles */
  .navbar {
    background-color: #333;
    overflow: hidden;
  }
  
  /* Logo styles */
  .logo {
    float: left;
  }
  
  .logo .a {
    display: block;
    color: #fff;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }
  
  /* Navigation links styles */
  .nav-links {
    list-style-type: none;
    margin: 0;
    padding: 0;
    float: right;
  }
  
  .nav-links li {
    display: inline-block;
  }
  
  .nav-links li .a {
    display: block;
    color: #fff;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }
  
  /* Responsive styles */
  @media screen and (max-width: 600px) {
    .navbar {
      display: flex;
      flex-direction: column;
    }
  
    .logo {
      text-align: center;
    }
  
    .nav-links {
      float: none;
      text-align: center;
    }
  
    .nav-links li {
      display: block;
    }
  
    .nav-links li .a {
      padding: 10px 0;
    }
  }
  </style>
  