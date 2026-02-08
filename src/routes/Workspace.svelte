<script lang="ts">
  import { onMount } from "svelte";
  let { children } = $props();
  import Ghostty from "$lib/components/Ghostty.svelte";
  let showghostty: boolean = $state(false);
  onMount(() => {
    setTimeout(() => (showghostty = true), 1000);
  });
</script>

<div class="workspace-content">
  {#if showghostty}
    <Ghostty {children} />
  {/if}
</div>

<style lang="sass">
div.workspace-content
  display: flex
  width: 100%
  height: 100vh
  justify-content: center
  align-items: center
  padding: 10px
  box-sizing: border-box
</style>
