<script setup lang="ts">
type ButtonStyle = 'primary' | 'secondary' | 'create-list' | 'notification'
type ImgStyle = 'create-list'

interface ButtonProps {
    themeimg?: ImgStyle
    theme: ButtonStyle
    text: string
    imageSrc?: string
    size?: 'large' | 'medium'
}
const props = withDefaults(defineProps<ButtonProps>(), {
        size: 'large'
})
</script>

<template>
    <button :class="[`button-${props.theme}`, `button-${props.size}`]" >
        <img :class="`image-${props.themeimg}`" v-if="props.imageSrc" :src="props.imageSrc" />
        {{props.text}}
    </button>
</template>


<style>
.image-create-list {
    width: 24px;
    height: 24px;
    margin: 0;
    padding-left: 10px;
}
.button-large {
    height: 48px;
}
.button-medium {
    height: 40px;
}
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
.button-create-list {
    display: flex;
    outline: none;
    border: none;
    border-radius: 16px;
    border: 1px solid transparent;
    font-size: 15px;
    width: 198px;
    justify-content: space-between;
    align-items: center;
    padding-right: 35px;
    margin: 16px 0px;
    box-sizing: border-box;
    font-family: Inter;
}
.button-create-list:hover {
    cursor: pointer;
    border: 1px solid  rgb(51, 51, 51);
}
</style> 
