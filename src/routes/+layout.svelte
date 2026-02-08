<script lang="ts">
	import { page } from "$app/state";
	import { locales, localizeHref } from "$lib/paraglide/runtime";
	import favicon from "$lib/assets/favicon.svg";
	import Jealomy from "./Jealomy.svelte";
	import "./layout.sass";

	let { children } = $props();
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div style="display:none">
	{#each locales as locale}
		<a href={localizeHref(page.url.pathname, { locale })}>
			{locale}
		</a>
	{/each}
</div>

<div class="all">
	<Jealomy {children} />
</div>

<style lang="sass">
div.all
	position: fixed
	width: 100%
	height: 100%
	padding: 0
	margin: 0
	display: inline-block
</style>
