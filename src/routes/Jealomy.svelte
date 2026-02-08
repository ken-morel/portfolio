<script lang="ts">
  import Waybar from "$lib/components/Waybar.svelte";
  import Workspace from "./Workspace.svelte";
  import Background from "$lib/components/Background.svelte"; // Import the new component

  let { children } = $props();
</script>

<Background />
<div class="waybar-container">
  <Waybar />
</div>
<div class="workspace-content">
  <Workspace {children} />
</div>

<style lang="sass">
.waybar-container
  height: 32px; // Fixed height of the horizontal Waybar
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10; // Ensure Waybar is on top

.workspace-content
  padding-top: 32px; // Offset for the horizontal Waybar
  width: 100%;
  height: 100vh; // Take full viewport height
  margin: 0;
  padding: 0; // Reset existing padding
</style>
