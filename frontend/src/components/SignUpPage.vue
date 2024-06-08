<script setup lang="ts">
import logoUrl from '../assets/logotype.svg?url'
</script>

<template>
    <div class="sign-up-content-wrapper">
        <div class="sign-up-content">
            <header class="header-nav">
                <div class="header-nav-logo">
                    <img :src="logoUrl" alt="logo">
                </div>
            </header>
        </div>
    </div>
</template>

<style>
    .sign-up-content-wrapper{
        display: flex;
        justify-content: space-around;
    }
    .sign-up-content{
        flex-grow: 1;
        max-width: 1200px;
    }
    .header-nav{
        display: flex;
    }
    .header-nav-logo{
        display: flex;
        padding: 24px;
    }
</style>