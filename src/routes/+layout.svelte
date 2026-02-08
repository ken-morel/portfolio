<script lang="ts">
	import { page } from "$app/stores";
	import { locales, localizeHref } from "$lib/paraglide/runtime";
	import favicon from "$lib/assets/favicon.svg";
	import Jealomy from "./Jealomy.svelte";
	import "./layout.sass"; // Re-import the global stylesheet
	import { browser } from "$app/environment"; // Import browser
	import { windowTitle } from "$lib/components/waybar/WindowTitle.svelte";

	let { children } = $props();

	// Dynamically update window title based on current path
	$effect(() => {
		if (browser) {
			// Only run this in the browser
			const path = $page.url.pathname;
			if (path.startsWith("/workspaces/1")) {
				windowTitle.set("kenmorel@jealomy: ~");
			} else if (path.startsWith("/workspaces/2")) {
				windowTitle.set("kenmorel@jealomy: Achievements");
			} else if (path.startsWith("/workspaces/3")) {
				windowTitle.set("kenmorel@jealomy: Projects");
			} else if (path.startsWith("/workspaces/4")) {
				windowTitle.set("kenmorel@jealomy: AI Shell");
			} else {
				windowTitle.set("kenmorel@jealomy: Welcome");
			}
		}
	});
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div style="display:none">
	{#each locales as locale}
		<a href={localizeHref($page.url.pathname, { locale })}>
			{locale}
		</a>
	{/each}
</div>

<Jealomy {children} />
