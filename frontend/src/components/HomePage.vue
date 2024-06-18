<script setup lang="ts">
import logoUrl from '../assets/logotype.svg?url';
import Button from './Button.vue';
import buttonIconUrl from '../assets/button-icon.svg?url';
import ButtonNotification from '../assets/notification-icon.svg?url';
import peopleIcon from '../assets/people-icon.svg?url';
import arrowIcon from '../assets/arrow-icon.svg?url';
import ProductListCard from './ProductListCard.vue';
import ProfileUser from './AccountMenu.vue';

import axios from 'axios';
import { ref, onMounted } from 'vue';

import { authStore } from '../auth';
import { getEndpointUrl } from '../api';

const productLists = ref<any>([]);
const profile = ref(false)

onMounted(async () => {
    const config = {
        headers: {
            'Authorization': `Bearer ${authStore.accessToken}`
        }
    };

    const response = await axios.get(getEndpointUrl('/product-lists'), config);
    productLists.value = response.data;
    console.log(productLists.value)
});
</script>

<template>
    <div class="container-home-wrapper" @click="() => {profile=false}">
        <div class="header-nav-home-wrapper">
            <header class="header-nav-home"> 
                <img class="logo-home" :src="logoUrl">
                <Button themeimg="create-list" class="add-list" size="medium" theme="create-list" text="Новый список" :imageSrc = "buttonIconUrl"/>
                <div class="info-people">
                    <img class="notification-icon" :src="ButtonNotification">
                    <img class="people-icon" :src="peopleIcon">
                    <p class="people-name">Даник</p>
                    <div class="arrow-icon-wrapper" @click="(e) => {profile=!profile; e.stopPropagation(); console.log(1)}">
                        <img class="arrow-icon" :src="arrowIcon"> 
                    </div>
                    <ProfileUser v-if="profile" class="profile-user"/>
                </div>
            </header>
        </div>
        <div class="container-home">   
            <div class="container-product-list">
                <div class="container-product-wrapper">
                    <div class="container-product" v-for="list in productLists" :key="list.id">
                        <ProductListCard :name="list.name" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.arrow-icon-wrapper {
    display: flex;
    cursor: pointer;
    margin-right: 33px;
}
.header-nav-home-wrapper {
    display: flex;
    max-width: 1200px;
}
.info-people-wrapper {
    display: flex;
}
.profile-user {
    display: flex;
    box-shadow: 6px 0px 20px rgba(51, 56, 63, 0.08);
    box-sizing: border-box;
    justify-content: space-between;
    border-radius: 20px;
    margin-top: 165px;
    height: 104px;
    position: absolute;
    flex-direction: column;
    cursor: default;
}
.container-product-wrapper {
    display: flex;
    flex-grow: 1;
    max-width: 928px;
}
.container-product {
    display: flex;
    flex-wrap: wrap;
    padding-left: 32px;
}
.container-product-list {
    display: flex;
    justify-content: space-around;
    margin-top: 64px;
}
.container-home {
    flex-grow: 1;
    max-width: 1200px;
    width: 100%;
    padding-top: 64px;
}
.header-nav-home {
    display: flex;
    justify-content: space-between;
    position: fixed;
    width: 100%;
    max-width: 1200px;
    background-color: white;
}
.logo-home {
    display: flex;
    padding: 24px 0px;
    margin-left: 24px;
    width: 119px;
    height: 24px;
}
.container-home-wrapper {
    display: flex;
    justify-content: center;
    height: 100vh;
}
.info-people {
    display: flex;
    align-items: center;
    max-height: 24px;
    margin-top: 24px;
}
.notification-icon {
    background-color: white;
    display: flex;
    outline: none;
    border: none;
    width: 24px;
    height: 24px;
    justify-content: center;
    padding-right: 24px;
}
.arrow-icon {
    background-color: white;
    display: flex;
    outline: none;
    border: none;  
    width: 10px;
    height: 5px;
    justify-content: center;
    align-items: center;
}
.people-icon {
    display: flex;
    outline: none;
    border: none;
    width: 24px;
    height: 24px; 
}
.people-name {
    font-family: Inter;
    max-width: 44px;
    padding-right: 19px;
    padding-left: 14px;
}
</style>