<script lang="ts">
  import { onMount } from "svelte";

  const icons = ["󰂎", "󰁺", "󰁻", "󰁼", "󰁽", "󰁾", "󰁿", "󰂀", "󰂁", "󰂂", "󰁹"];
  let batteryLevel = $state(0);
  let batteryCharging = $state(false);
  let batteryHours = $state(0);
  let batteryMinutes = $state(0);
  onMount(() => {
    //TODO: Listen to battery events instead of fetching the battery
    // @ts-ignore
    navigator.getBattery?.().then((battery: any) => {
      const update = () => {
        batteryLevel = battery.level * 100;
        batteryCharging = battery.charging;
        console.log(battery);
        try {
          const time: Date = battery.dischargTime ?? battery.chargingTime;
          batteryHours = time.getHours();
          batteryMinutes = time.getMinutes();
        } catch (e) {
          batteryHours = batteryMinutes = 0;
        }
      };
      update();
      battery.onchargingchange = update;
      battery.onchargingtimechange = update;
      battery.ondischargingtimechange = update;
      battery.onlevelchange = update;
    });
  });
</script>

<div
  class="battery"
  class:charging={batteryCharging}
  class:low={!batteryCharging && batteryLevel < 10}
  title={`${batteryHours} hour${batteryHours == 1 ? "" : "s"} and ${batteryMinutes} minute${batteryMinutes == 1 ? "" : "s"} remaining`}
>
  <span>
    {icons[Math.floor(icons.length * (batteryLevel / 100))]}
  </span>
</div>

<style lang="sass">
div.battery
  font-family: "FiraCode Nerd Font Mono"
  font-size: 18px
  padding: 0 10px
  display: flex
  align-items: center
  height: 100%

  &.charging
    color: #b8bb26 // Gruvbox Green
  &.low
    color: #fb4934 // Gruvbox Red
</style>
