<script setup lang="ts">

interface FieldProps {
    inputType?: InputType
    label: string
    text: string
}
type InputType = 'text' | 'password'

const props = withDefaults(defineProps<FieldProps>(), {
    inputType: 'text'
});

const emit = defineEmits<{
    change: [value: string]
    }>();
</script>

<template>
    <div class="field">
        <p class="field-header">
            {{props.label}}
        </p>
        <input class="field-input"
            :type="props.inputType"
            :value="props.text"
            @input="event => $emit('change', (event.target as HTMLInputElement).value)"
        ></input>
    </div>
</template>

<style>
    .field{
        width: 100%;
        margin-bottom: 16px;
    }
    .field-input{
        height: 40px;
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
        border: 1px solid #E2E3E7;
        border-radius: 12px;
    }
    .field-header{
        line-height: 16px;
        font-family: Inter;
        font-size: 13px;
        color: #6E7C89;
    }
</style>