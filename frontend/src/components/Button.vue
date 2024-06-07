<script setup lang="ts">
type ButtonStyle = 'primary' | 'secondary'

interface ButtonProps {
    theme: ButtonStyle
    text: string
}
const props = defineProps<ButtonProps>()
</script>

<template>
    <button :class="`button-${props.theme}`" >
        {{props.text}}
    </button>
</template>


<style>
.button-primary {
    background-color: #F2F4F8;
    outline: none;
    border: none;  
    line-height: 20px;
    font-family: Inter;
    font-size: 15px;
    display: flex;
    justify-content: center;
    border-radius: 16px;
    align-items: center;
    height: 48px;
}

.button-primary:hover {
    cursor: pointer;
    border: 1px solid  rgb(51, 51, 51);
    box-sizing: border-box;
}

.button-secondary {
    border-radius: 16px;
    background-color: white;
    font-family: Inter;
    color: #1E82DF;
    font-size: 15px;
    display: flex;
    justify-content: center;
    outline: none;
    line-height: 20px;
    border: 1px solid #F2F5FB;
    padding: 14px 0px;
}
.button-secondary:hover {
    cursor: pointer;
    border: 1px solid  rgb(51, 51, 51);
    box-sizing: border-box;
}
</style> 
