<script lang="ts" module>
  import { writable } from "svelte/store";

  export const windowTitle = writable("kenmorel@jealomy"); // Default title

  // This component subscribes to the store and displays its value
</script>

<div class="window-title">
  {$windowTitle}
</div>

<style lang="sass">
.window-title
  color: #ebdbb2; // Gruvbox foreground
  font-weight: bold;
  padding: 0 10px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
</style>
