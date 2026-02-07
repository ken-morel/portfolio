<script lang="ts">
  import { onMount } from "svelte";
  import { type ReplMessage } from "./FishRepl.svelte";
  import { sleep } from "$lib";
  import { marked } from "marked";
  import { scrollToPerc } from "$lib/ghostty";

  let {
    message,
    onFinish,
    typespeed,
    outputspeed,
    promptinterval,
  }: {
    message: ReplMessage;
    onFinish: () => void;
    typespeed: number;
    outputspeed: number;
    promptinterval: number;
  } = $props();
  let promptmessage = $state("");
  let showcaret = $state(true);
  let renderedOutput = $state("");
  onMount(async () => {
    await sleep(promptinterval);
    let interval: number = 1000 / typespeed;
    let faster = false;

    for (const c of message.prompt) {
      promptmessage += c;
      // we don't type at constant speed
      if (c == " " || c == "|") {
        faster = !faster;
      }
      await sleep(interval + (faster ? -100 : 0));
    }
    showcaret = false;
    scrollToPerc.set(true);
    for (let i = 0; i <= message.output.length; i++) {
      renderedOutput = marked.parse(message.output.slice(0, i), {
        async: false,
      });
      await sleep(1000 / outputspeed);
    }
    scrollToPerc.set(false);
    onFinish();
  });
</script>

<div class="message">
  <div class="prompt">
    <span class="cwd">{message.cwd || "~/.config"} </span>
    <span class="on"> on </span>
    <span class="branch">  arch26v2 </span>
    <span class="git-status">[✘!+?⇡]</span>

    <br />
    <span class="character">❯ </span>
    <span class="input">
      {promptmessage}
      {#if showcaret}
        <span class="caret"></span>
      {/if}
    </span>
  </div>
  <div class="markdown-shell-output">{@html renderedOutput}</div>
</div>

<style lang="sass">
div.message
  & > div.prompt
    & > span
      display: inline

      &.cwd
        font-weight: bold
        color: #33aa88
      &.on
        font-weight: bold
        color: #999
      &.branch
        font-weight: bold
        color: #97a
      &.git-status
        color: #c55
      &.character
        color: #5c5
      &.input
        white-space: nowrap
        & > span.caret
          border: 0.5px solid #ccc

:global(div.output table)
  padding: 5px
  & > thead > *
    padding: 2px
</style>
