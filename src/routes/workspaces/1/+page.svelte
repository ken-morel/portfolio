<script lang="ts">
  import { onMount } from "svelte";
  import FishRepl, { type ReplMessage } from "$lib/components/FishRepl.svelte";
  import { windowTitle } from "$lib/components/waybar/WindowTitle.svelte";

  onMount(() => {
    windowTitle.set("kenmorel@jealomy: ~");
  });

  const messages: ReplMessage[] = [
    {
      prompt: "whoami | batcat",
      cwd: null,
      output: `

**Ken Morel Engon**

Mbollo from \`ama\` a Junior system developer, aiming to build software, aiming for speed,
safety and fault tolerance.
      `,
    },
    {
      prompt: "veryslowfetch; and env",
      output: `
\`\`\`
      /\\        kenmorel@jealomy
     /  \\       ------------------
    /    \\      Host: Jaof Higher Institute of Science (JHIS)
   /      \\     Uptime: 17 years, 4 months
  /   ,,   \\    Packages: 5 (active projects)
 /   |  |   \\   Shell: fish 3.7.1
/_-''    ''-_\\  Resolution: (expanded horizon)x(elevated perspective) (quick frequency)
                CPU: DeveloperCore AI-X9 "Genius" (Socket AM6)brain + gemini combo
EDITOR=helix
BROWSER=qutebrowser
TERM=ghostty
PAGER=batcat
FILE_MANAGER=yazi
SHELL=fish
\`\`\`
      `,
      cwd: null,
    },
    {
      prompt: "exa -l ~/projects",
      output: `
| \`          \` | \`       \` | \`                                  \` |
| :-                | :-              |   :-                                              |
| \`10 Feb \` | \` alat/    \` | \`Native cross-device service mesh (Go -> Rust)\` |
| \`05 Feb \` | \` gama/    \` | \`Cross-platform C toolchain for students      \` |
| \`12 Feb \` | \` arb-util/\` | \`Parallelized i10n & Llama.cpp translation for flutter    \` |
| \`03 Feb \` | \` efus.jl/ \` | \`Reactive UI components via Julia macros      \` |
| \`07 Feb \` | \` rrr/     \` | \`Remote REPL Runner for editor-sync           \` |

Click on a project for more information.
      `,
      cwd: null,
    },
  ];
</script>

<div>
  <!--  <FishRepl typespeed={5} outputspeed={100} promptinterval={2000} {messages} /> -->
  <FishRepl
    typespeed={100}
    outputspeed={1000}
    promptinterval={200}
    {messages}
  />
</div>

<style lang="sass"></style>
