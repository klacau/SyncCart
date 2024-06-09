<script setup lang="ts">
import logoUrl from '../assets/logotype.svg?url'
import Button from './Button.vue'
import InputField from './InputField.vue'
import {useRouter} from 'vue-router'
const router = useRouter();
</script>

<template>
    <div class="sign-up-content-wrapper">
        <div class="sign-up-content">
            <header class="header-nav">
                <div class="header-nav-logo" @click="() => router.push({name:'Welcome'})">
                    <img class="header-logo__img" :src="logoUrl" alt="logo">
                </div>
            </header>
        </div>
    </div>
    <div class="sign-up-main-content-wrapper">
        <div class="sign-up-main-content">
            <h2 class="sign-up-main-content-h2">Регистрация</h2>
            <InputField label="E-mail"/>
            <InputField label="Имя"/>
            <InputField label="Пароль"/>
            <Button theme="primary" text="Зарегистрироваться" class="button-register"/>
        </div>
    </div>    
</template>

<style>
    .header-logo__img{
        cursor: pointer;
    }
    .sign-up-content-wrapper{
        display: flex;
        justify-content: space-around;
    }
    .sign-up-content{
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        max-width: 1200px;
    }
    .header-nav{
        display: flex;
        position: fixed;
    }
    .header-nav-logo{
        display: flex;
        padding: 24px;
    }
    .sign-up-main-content-wrapper{
        display: flex;
        justify-content: space-around;
        margin-top: 20vh;
    }
    .sign-up-main-content-h2{
        justify-content: center;
        padding: 40px;
        line-height: 28px;
        font-family: Inter;
        font-size: 24px;
        font-weight: bold;
    }
    .sign-up-main-content{
        flex: 1;
        max-width: 400px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 24px;
    }
    .button-register{
        width: 100%;
    }
</style>