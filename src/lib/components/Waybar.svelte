<script lang="ts">
  import Time from "./waybar/Time.svelte";
  import Workspaces from "./waybar/Workspaces.svelte";
  import Spotify from "./waybar/Spotify.svelte";
  import NWGBar from "./waybar/NWGBar.svelte";
  import Battery from "./waybar/Battery.svelte";
  import Network from "./waybar/Network.svelte";
  import WindowTitle from "./waybar/WindowTitle.svelte"; // Import the new component
  import { onMount } from "svelte";
  import { windowTitle } from "./waybar/WindowTitle.svelte";
  onMount(() => {
    windowTitle.set("kenmorel@jealomy: ~");
  });
</script>

<div class="waybar">
  <div class="left">
    <Workspaces />
  </div>
  <div class="center">
    <WindowTitle />
  </div>
  <div class="right">
    <Spotify />
    <Battery />
    <Network />
    <NWGBar />
    <Time />
  </div>
</div>

<style lang="sass">
.waybar
  background-color: #1e1e2e; // As per new spec
  color: #dcd7ba;
  padding: 0
  border-radius: 0; // Removed border-radius
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)
  width: 100%; // Horizontal bar
  height: 32px; // Fixed height as per new spec
  margin: 0; // Removed top margin
  text-align: center
  display: flex;
  flex-direction: row; // Horizontal bar
  justify-content: space-between;
  align-items: center; // Vertically center items

  div.left,
  div.center,
  div.right
    display: flex; // Use flex for internal alignment
    align-items: center;
    // width: auto; // Let content dictate width
    height: 100%; // Fill Waybar height
</style>
