<script lang="ts" module>
  import { onMount } from "svelte";
  import FishReplMessage from "./FishReplMessage.svelte";
  export type ReplMessage = {
    prompt: string;
    output: string;
    cwd: string | null;
  };
</script>

<script lang="ts">
  let {
    messages,
    typespeed,
    outputspeed,
    promptinterval,
  }: {
    messages: ReplMessage[];
    typespeed: number;
    outputspeed: number;
    promptinterval: number;
  } = $props();
  let showmessages: ReplMessage[] = $state([]);
  function nextMessage() {
    showmessages = showmessages.concat(messages.splice(0, 1));
  }
  onMount(() => {
    nextMessage();
  });
</script>

<div class="repl-messages">
  {#each showmessages as message}
    <FishReplMessage
      {message}
      {typespeed}
      {outputspeed}
      {promptinterval}
      onFinish={nextMessage}
    />
  {/each}
</div>

<style lang="sass">

div.repl-messages
  font-family: "FiraCode Nerd Font Mono"
</style>
