<script lang="ts">
  import { workspaces, currentWorkspace } from "$lib/workspaces";
</script>

<div class="workspaces-container">
  {#each workspaces as workspace}
    <button class:active={$currentWorkspace == workspace} class="button"
      >{workspace}</button
    >
  {/each}
</div>

<style lang="sass">
.workspaces-container
  border-top: 1px solid #242;
  border-bottom: 1px solid #242;
  margin-top: 5px;
  margin-bottom: 5px;
  padding-top: 0px;
  padding-bottom: 0px;

  border:
    top: 1px white solid
    bottom: 1px white solid
  button
    display: inline-block
    width: 100%
    text-align: center
    color: #88c0d0
    padding: 0px 0px;
    margin: 0 !important
    border-radius: 0%;
    font-size: 15px;
    font-family: "Firacode Nerd Font Mono", "Font Awesome 6 Free", "Font Awesome";
    &.active
      color: #81a1c1
      background-color: #3b4252;
    &.urgent
      color: #bf616a
      animation: urgent-flash 1s infinite;
    &:hover
      background-color: #7b8292;
</style>
