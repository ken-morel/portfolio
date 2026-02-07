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
  width: 100%
  text-align: center
  & > button
    width: 100%
    display: block
    font-size: 25px
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
      background-color: #050a03
      border-radius: 5px
      padding: 5px
      & > button
        display: inline-block
        width: 100px
        height: 100px
        border-radius: 10px
        margin: 3px 3px
        & > img
          width: 50px
          margin: auto
        &:hover
          background-color: #5553

</style>
