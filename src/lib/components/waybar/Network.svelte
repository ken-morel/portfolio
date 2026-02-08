<script lang="ts">
  import { onMount } from "svelte";

  let isOnline = $state(true);

  onMount(() => {
    isOnline = navigator.onLine;

    const goOnline = () => (isOnline = true);
    const goOffline = () => (isOnline = false);

    window.addEventListener("online", goOnline);
    window.addEventListener("offline", goOffline);

    return () => {
      window.removeEventListener("online", goOnline);
      window.removeEventListener("offline", goOffline);
    };
  });
</script>

<div
  class="network-status"
  title={isOnline ? "Network: Online" : "Network: Offline"}
>
  {#if isOnline}
    <span class="online-icon">🌐</span>
  {:else}
    <span class="offline-icon">🚫</span>
  {/if}
</div>

<style lang="sass">
  .network-status
    text-align: center
    padding: 4px 0
    font-size: 16px


  .online-icon
    color: #8fbcbb // Cyan/Green for online


  .offline-icon
    color: #bf616a // Red for offline

</style>
