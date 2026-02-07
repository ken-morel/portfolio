<script lang="ts">
  import FishRepl, { type ReplMessage } from "$lib/components/FishRepl.svelte";

  const messages: ReplMessage[] = [
    {
      prompt: "batcat ~/.config/user/bio.md",
      cwd: null,
      output: `

**Ken Morel Engon**
* Junior system dev | Junior Back-End Developer | Lead @ J-Tech*

I am a developer driven by **logic, automation, and system efficiency.** I don't just write apps; I build the underlying toolchains that make development possible. My work is centered on low-level performance and cross-platform architecture.


      `,
    },
    {
      prompt: "veryslowfetch",
      output: `
\`\`\`
      /\\        kenmorel@jealomy
     /  \\       ------------------
    /    \\      Host: Jaof Higher Institute of Science (JHIS)
   /      \\     Uptime: 17 years, 4 months
  /   ,,   \\    Packages: 5 (active projects)
 /   |  |   \\   Shell: fish 3.7.1
/_-''    ''-_\\  Resolution: 1920x1080 (Strictly Orthogonal)
                CPU: Software Engineer
                Memory: Stack-first, Heap-less or preallocated

\`\`\`

      `,
      cwd: null,
    },
  ];
</script>

<div>
  <FishRepl typespeed={5} outputspeed={100} promptinterval={2000} {messages} />
</div>

<style lang="sass"></style>
