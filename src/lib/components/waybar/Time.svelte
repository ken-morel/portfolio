<script lang="ts">
  import { onMount } from "svelte";

  let hours: number = $state(0),
    minutes: number = $state(0);

  function setTime() {
    let now = new Date(Date.now());
    hours = now.getHours();
    minutes = now.getMinutes();
  }
  setTime();

  onMount(() => {
    const interval = setInterval(setTime, 1000);
    return () => {
      clearInterval(interval);
    };
  });
</script>

<div class="waybar-time">
  <span>{hours.toString().padStart(2, "0")}</span>
  <span>{minutes.toString().padStart(2, "0")}</span>
</div>

<style lang="sass">
div.waybar-time
  span
    color: #aa77aa
    margin: 0px 2px 0px 2px;
    font-family: "Firacode Nerd Font Mono";
    font-weight: bold;
    font-size: 18px;
</style>
