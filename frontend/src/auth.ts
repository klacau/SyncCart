import { reactive } from 'vue';

interface AuthStore {
    accessToken?: string;
}

export const authStore = reactive<AuthStore>({});