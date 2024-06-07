<script setup lang="ts">
import LogoIcon from '../assets/logo.svg';
import Button from './Button.vue'
</script>

<template>
    <div class="container-wrapper">
        <div class="container"> 
            <div class="container-logo">       
                <LogoIcon class="logo-icon"/>
                <p class="title-project">SyncCart</p>
            </div>
            <div class="container-action">
                <Button theme="primary" text="Регистрация" class="button-login"/>    
                <Button theme="secondary" text="Войти" class="button-register"/>
            </div>
        </div>
    </div>
</template>


<style>
.logo-icon {
    width: 120px;
    height: 112px;
}
.title-project {
    font-family: Inter;
    font-size: 36px;
    font-weight: bold;
    line-height: 44px;
    margin: 0;
    padding-top: 31px;
}
.container-logo {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 60px;
}
.container {
    display: flex;
    flex-direction: column;
    max-width: 360px;
    flex-grow: 1;
    justify-content: center;
    height: 100vh;
}
.container-action {
    display: flex;
    flex-direction: column;
}
.button-login {
    font-family: Inter;
    font-size: 15px;
    display: flex;
    justify-content: center;
    border-radius: 16px;
    padding: 0;
}
.button-login:hover {
    cursor: pointer;
    background-color:  rgb(51, 51, 51);
    color: white;
}
.button-register {
    font-family: Inter;
    color: #1E82DF;
    font-size: 15px;
    display: flex;
    justify-content: center;
    border-radius: 16px;
    margin-top: 16px;
    padding: 0;
}
.button-register:hover {
    cursor: pointer;
    background-color:  rgb(51, 51, 51);
    color: white;
}
    
.container-wrapper {
    display: flex;
    justify-content: space-around;
}
</style>