<script setup lang="ts">
import logoUrl from '../assets/logotype.svg?url';
import Button from './Button.vue';
import InputField from './InputField.vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import axios from 'axios';

import { authStore } from '../auth';
import { getEndpointUrl } from '../api';

const router = useRouter();

const email = ref('');
const username = ref('');
const password = ref('');

async function signUp() {
    const data = new URLSearchParams();
    data.append('email', email.value);
    data.append('username', username.value);
    data.append('password', password.value);

    const config = {
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    }

    const response = await axios.post(getEndpointUrl('/auth/sign-up'), data.toString(), config);
    authStore.accessToken = response.data['access_token'];
    
    router.push({ name: 'Root' });
}
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
            <InputField label="E-mail"
                :text="email" 
                @change="(value) => email = value" 
            />
            <InputField label="Имя пользователя"
                :text="username" 
                @change="(value) => username = value" 
            />
            <InputField label="Пароль"
                :text="password"
                input-type="password"
                @change="(value) => password = value" 
            />
            <Button class="button-register" 
                theme="primary" 
                text="Зарегистрироваться" 
                @click="signUp"
            />
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