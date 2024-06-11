<script setup lang="ts">

interface ProductListCardProps {
    name: string;
    // items: readonly ProductListItem[];
}

const props = defineProps<ProductListCardProps>();
</script>

<template>
    <ul class="product-list">
        <div class="product-list__inner">
            <li class="first-row" :style="{backgroundColor: '#EDF5FF'}"><h3>{{ props.name }}</h3></li>
            <li class="second-row"><p>Бананы</p></li>
            <li><p>Даники</p></li>
        </div>
    </ul>
</template>

<style>
.product-list__inner {
    box-shadow: 6px 0px 20px rgba(51, 56, 63, 0.08);
    box-sizing: border-box;
    border-radius: 20px;
}
.second-row {
    display: flex;
    padding-top: 20px;
}
li:first-child {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}
li:last-child {
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
}
.product-list li p {
    display: flex;
    padding-bottom: 12px;
    font-size: 15px;
}
.product-list li {
    padding-left: 24px;
}
.first-row {
    background-color: #EDF5FF;
    padding: 20px 0px;
    font-size: 16px;
    font-weight: bold;
}
.product-list {
    font-family: Inter;
    display: flex;
    flex-direction: column;
    width: 288px;
    max-height: 308px;
    padding-right: 32px;
    padding-bottom: 32px;
}
</style>