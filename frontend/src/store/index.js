import { writable } from "svelte/store";

export const memeList = writable([]);
export const isModalOpen = writable(false);
export const modalFormData = writable(undefined);
