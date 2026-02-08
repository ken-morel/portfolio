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
  height: 100%
  width: 40px
  display: inline-block
  position: fixed
  top: 0
  left: 0
.workspace-content
  padding-left: 40px
  width: 100%
  height: 100vh
  margin: 0
  padding: 0
</style>
