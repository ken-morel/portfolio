<script lang="ts">
  import Time from "./waybar/Time.svelte";
  import Workspaces from "./waybar/Workspaces.svelte";
  import Spotify from "./waybar/Spotify.svelte";
  import NWGBar from "./waybar/NWGBar.svelte";
  import Battery from "./waybar/Battery.svelte";
  import Network from "./waybar/Network.svelte";
</script>

<div class="waybar">
  <div class="left">
    <Time />
    <Spotify />
  </div>
  <div class="center">
    <Workspaces />
  </div>
  <div class="right">
    <Network />
    <Battery />
    <NWGBar />
  </div>
</div>

<style lang="sass">
.waybar
  background-color: transparent
  color: #dcd7ba;
  padding: 0
  border-radius: 5px
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)
  width: 35px
  margin:
    top: 3px
  text-align: center
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  height: 100%

  div.left,
  div.center,
  div.right
    display: inline-block
    width: 100%
</style>
