<template>
    <v-app id="app">
        <Nav/>

        <transition enter-active-class="animated fadeIn" leave-active-class="animated fadeOut" mode="out-in">
            <router-view style="flex:1 1 auto; "></router-view>
        </transition>
        <Modal v-if="$store.state.modalStatus"/>
    </v-app>
</template>

<script>
    const Modal = () => import('@/components/Layout/Modal')
    const Nav = () => import('@/components/Layout/Nav')

    export default {
        name: 'App',
        components: {
            Modal, Nav
        },

    }
</script>

<style lang="scss">
    #app {
        font-family: 'Poppins', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        background: #F4F4F4;
        padding: 0;
        margin: 0;
        width: 100vw;
        min-height: 100vh;
        display: flex;
    }

    input:focus {
        border: 1px solid #08BA4D !important;
        box-shadow: 0 0 1px #08BA4D;
        outline:none;
    }
</style>