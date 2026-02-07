import { mdsvex } from 'mdsvex';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import adapter from '@sveltejs/adapter-node';


/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: { adapter: adapter() },
	preprocess: [mdsvex(), vitePreprocess()],
	extensions: ['.md', '.svelte', '.svx']
};

export default config;
