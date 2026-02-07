<script lang="ts">
  import { scale } from "svelte/transition";
  let { children } = $props();
</script>

<div class="ghostty-window" transition:scale>
  <div class="content">
    {@render children?.()}
  </div>
</div>

<style lang="sass">
.ghostty-window
  color: #ccc
  border-radius: 10px
  background-color: #2228
  border: 1px #444a solid
  padding: 0
  margin: auto
  min-width: 800px;
  max-width: 80%;
  height: fit-content
  width: fit-content;
  min-height: 200px
  max-height: 80%
  overflow-y: scroll
  backdrop-filter: blur(10px)

  letter-spacing: .05em


  .content
    width: 100%
    height: 100%
    padding: 7px

</style>
