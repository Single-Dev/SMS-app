<template >
    <div class="d-flex justify-content-center align-items-center vh-100">
        <form @submit.prevent class="text-center lm-p-2">
        <div class="p-5 card">
            <h2>Login</h2>
            <!-- Email input -->
            <div class="form-outline mb-4">
                <input type="text" id="form2Example1" class="form-control" v-model="username" />
                <label class="form-label" for="form2Example1">Username</label>
            </div>

            <!-- Password input -->
            <div class="form-outline mb-4">
                <input type="password" id="form2Example2" class="form-control" v-model="password" />
                <label class="form-label" for="form2Example2">Password</label>
            </div>

            <!-- 2 column grid layout for inline styling -->
            <div class="row mb-4">
                <div class="col d-flex justify-content-center">
                    <!-- Checkbox -->
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
                        <label class="form-check-label" for="form2Example31"> Remember me </label>
                    </div>
                </div>

                <div class="col">
                    <!-- Simple link -->
                    <a href="#!">Forgot password?</a>
                </div>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-outline-dark btn-block mb-4">Login</button>
        </div>
    </form>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'Login',
    // data() {
    //     return {
    //         username: '',
    //         password: '',
    //     }
    // },
}
</script>
<style ></style>