<script setup lang="ts">
import logoUrl from '../assets/logotype.svg?url';
import Button from './Button.vue';
import buttonIconUrl from '../assets/button-icon.svg?url';
import ButtonNotification from '../assets/notification-icon.svg?url';
import peopleIcon from '../assets/people-icon.svg?url';
import arrowIcon from '../assets/arrow-icon.svg?url';
import ProductListCard from './ProductListCard.vue';

import axios from 'axios';
import { ref, onMounted } from 'vue';

import { authStore } from '../auth';
import { getEndpointUrl } from '../api';

const productLists = ref<any>([]);

onMounted(async () => {
    const config = {
        headers: {
            'Authorization': `Bearer ${authStore.accessToken}`
        }
    };

    const response = await axios.get(getEndpointUrl('/product-lists'), config);
    productLists.value = response.data;
});
</script>

<template>
    <div class="container-home-wrapper">
        <div class="container-home">    
            <header class="header-nav-home"> 
                <img class="logo-home" :src="logoUrl">
                <Button themeimg="create-list" class="add-list" size="medium" theme="create-list" text="Новый список" :imageSrc = "buttonIconUrl"/>
                <div class="info-people">
                    <img class="notification-icon" :src="ButtonNotification">
                    <img class="people-icon" :src="peopleIcon">
                    <p class="people-name">Даник</p>
                    <img class="arrow-icon" :src="arrowIcon">
                </div>
            </header>
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
}
.header-nav-home {
    display: flex;
    justify-content: space-between;
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
    justify-content: space-around;
}
.info-people {
    display: flex;
    align-items: center;
    max-height: 24px;
    margin-top: 24px;
}
.info-people:hover {
    cursor: pointer;
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
    padding-right: 33px;
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