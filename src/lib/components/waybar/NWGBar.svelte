<script lang="ts">
  import { onMount } from "svelte";

  import HibernationIcon from "./nwgbar/system-hibernate.svg";
  import ShutDownIcon from "./nwgbar/system-shutdown.svg";
  import RebootIcon from "./nwgbar/system-reboot.svg";
  import LockIcon from "./nwgbar/system-lock-screen.svg";
  import LogoutIcon from "./nwgbar/system-log-out.svg";

  let showModal = $state(false);
  let dialog: HTMLDialogElement;
  $effect(() => {
    if (showModal) {
      dialog.showModal();
    } else {
      dialog.close();
    }
  });
  onMount(() => {});
  const buttons: { name: string; icon: string }[] = [
    {
      name: "Lock",
      icon: LockIcon,
    },
    {
      name: "Logout",
      icon: LogoutIcon,
    },
    {
      name: "Reboot",
      icon: RebootIcon,
    },
    {
      name: "Hibernate",
      icon: HibernationIcon,
    },
    {
      name: "Shutdown",
      icon: ShutDownIcon,
    },
  ];
</script>

<dialog bind:this={dialog} onclick={() => (showModal = false)}>
  <div>
    <div>
      {#each buttons as button}
        <button>
          <img src={button.icon} alt={button.name} />
          <span>{button.name}</span>
        </button>
      {/each}
    </div>
  </div>
</dialog>
<div class="nwg-bar">
  <button onclick={() => (showModal = true)}>⏻</button>
</div>

<style lang="sass">
div.nwg-bar
  display: flex
  align-items: center
  height: 100%
  
  & > button
    height: 100%
    padding: 0 12px
    font-size: 20px
    color: #fb4934 // Gruvbox Red for power button
    &:hover
      background-color: #3c3836 // Gruvbox dark grey
      
dialog
  width: 100%
  height: 100%
  background-color: #0000
  &::backdrop
    background-color: #0005
  & > div
    width: 100%
    height: 100%
    display: flex
    align-items: center
    justify-content: center
    & > div
      height: fit-content
      width: fit-content
      background-color: #282828 // Match Gruvbox background
      border: 1px solid #a89984 // Gruvbox border
      border-radius: 0 // Strictly Orthogonal
      padding: 5px
      & > button
        display: inline-block
        width: 100px
        height: 100px
        border-radius: 0 // Strictly Orthogonal
        margin: 3px 3px
        & > img
          width: 50px
          margin: auto
        &:hover
          background-color: #3c3836
</style>
