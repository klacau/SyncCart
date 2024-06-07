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
    line-height: 48px;
}

.button-secondary {
    background-color: white;
    outline: none;
    border: none;  
    line-height: 48px;
    border: 1px solid #F2F5FB;
}
</style> 
